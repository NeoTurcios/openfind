#[derive(Debug, Clone)]
pub struct AuditResult {
    pub ssl_active: bool,
    pub ssl_issuer: Option<String>,
    pub cloudflare_mode: String,
    pub ns_servers: Vec<String>,
}

pub fn audit_server(_domain: &str, _ip: Option<&str>, raw_whois: Option<&str>) -> AuditResult {
    let ns_servers = if let Some(whois) = raw_whois {
        extract_nameservers(whois)
    } else {
        Vec::new()
    };

    let has_cf_ns = ns_servers.iter().any(|ns| ns.to_lowercase().contains("cloudflare"));
    let cloudflare = if has_cf_ns { "gray" } else { "none" };

    AuditResult {
        ssl_active: false,
        ssl_issuer: None,
        cloudflare_mode: cloudflare.to_string(),
        ns_servers,
    }
}

fn extract_nameservers(whois: &str) -> Vec<String> {
    let mut servers = Vec::new();
    for line in whois.lines() {
        let l = line.trim().to_lowercase();
        if l.starts_with("nserver:") || l.starts_with("name server:") || l.starts_with("nameserver:") {
            let parts: Vec<&str> = l.splitn(2, ':').collect();
            if parts.len() > 1 {
                let mut ns = parts[1].trim().to_string();
                if ns.ends_with('.') {
                    ns.pop();
                }
                if !ns.is_empty() && !servers.contains(&ns) {
                    servers.push(ns);
                }
            }
        }
    }
    servers
}
