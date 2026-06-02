pub mod dns;
pub mod whois;
pub mod ssl_audit;
pub mod generator;
pub mod brand_eval;
pub mod error;

pub use dns::resolve_dns;
pub use whois::{query_whois, parse_whois, WhoisData};
pub use ssl_audit::audit_server;
pub use generator::generate_names;
pub use brand_eval::evaluate_brand;

/// Result of a complete domain check.
#[derive(Debug, Clone)]
pub struct DomainResult {
    pub domain: String,
    pub status: String,
    pub detail: String,
    pub ip: Option<String>,
    pub registrar: Option<String>,
    pub creation_date: Option<String>,
    pub method: String,
    pub ssl_active: bool,
    pub ssl_issuer: Option<String>,
    pub cloudflare: String,
    pub ns_servers: Vec<String>,
    pub brand_score: Option<f32>,
    pub brand_feedback: Option<String>,
}

/// Brand evaluation score.
#[derive(Debug, Clone)]
pub struct BrandScore {
    pub score: f32,
    pub feedback: String,
    pub length_score: f32,
    pub pronounce_score: f32,
    pub memory_score: f32,
    pub tld_score: f32,
}

/// Check a single domain's availability.
pub fn check_domain(domain: &str, do_audit: bool) -> DomainResult {
    let clean = domain.trim().to_lowercase()
        .replace("https://", "")
        .replace("http://", "")
        .replace("www.", "")
        .split('/')
        .next()
        .unwrap_or("")
        .to_string();

    match resolve_dns(&clean) {
        Some(ip) => {
            let mut result = DomainResult {
                domain: clean.clone(),
                status: "taken".into(),
                detail: "Registered (Active via DNS)".into(),
                ip: Some(ip.clone()),
                registrar: None,
                creation_date: None,
                method: "DNS Resolution".into(),
                ssl_active: false,
                ssl_issuer: None,
                cloudflare: "none".into(),
                ns_servers: vec![],
                brand_score: None,
                brand_feedback: None,
            };

            if do_audit {
                let audit = audit_server(&clean, Some(&ip), None);
                result.cloudflare = audit.cloudflare_mode;
                result.ns_servers = audit.ns_servers;
            }

            result
        }
        None => {
            let tld = clean.split('.').last().unwrap_or("");
            let server = get_whois_server(tld);

            let raw_whois = query_whois(&clean, server);
            if raw_whois.starts_with("ERROR:") {
                return DomainResult {
                    domain: clean,
                    status: "unknown".into(),
                    detail: format!("Network error: {}", &raw_whois[6..]),
                    ip: None,
                    registrar: None,
                    creation_date: None,
                    method: "Limit / WHOIS Network".into(),
                    ssl_active: false,
                    ssl_issuer: None,
                    cloudflare: "none".into(),
                    ns_servers: vec![],
                    brand_score: None,
                    brand_feedback: None,
                };
            }

            let final_whois = handle_referral(&clean, &raw_whois);
            let whois_data = parse_whois(&final_whois, tld);

            match whois_data.status.as_str() {
                "available" => DomainResult {
                    domain: clean,
                    status: "available".into(),
                    detail: "Available for registration!".into(),
                    ip: None,
                    registrar: None,
                    creation_date: None,
                    method: "WHOIS Socket 43 Query".into(),
                    ssl_active: false,
                    ssl_issuer: None,
                    cloudflare: "none".into(),
                    ns_servers: vec![],
                    brand_score: None,
                    brand_feedback: None,
                },
                "taken" => {
                    let mut result = DomainResult {
                        domain: clean.clone(),
                        status: "taken".into(),
                        detail: "Registered (Confirmed by WHOIS)".into(),
                        ip: None,
                        registrar: whois_data.registrar.clone(),
                        creation_date: whois_data.creation_date.clone(),
                        method: "WHOIS Socket 43 Query".into(),
                        ssl_active: false,
                        ssl_issuer: None,
                        cloudflare: "none".into(),
                        ns_servers: whois_data.nameservers.clone(),
                        brand_score: None,
                        brand_feedback: None,
                    };

                    if do_audit {
                        let audit = audit_server(&clean, None, Some(&final_whois));
                        result.cloudflare = audit.cloudflare_mode;
                        result.ns_servers = audit.ns_servers;
                    }

                    result
                }
                _ => DomainResult {
                    domain: clean,
                    status: "unknown".into(),
                    detail: "Could not be determined with certainty".into(),
                    ip: None,
                    registrar: None,
                    creation_date: None,
                    method: "WHOIS Socket 43 Query".into(),
                    ssl_active: false,
                    ssl_issuer: None,
                    cloudflare: "none".into(),
                    ns_servers: vec![],
                    brand_score: None,
                    brand_feedback: None,
                },
            }
        }
    }
}

fn handle_referral(domain: &str, raw: &str) -> String {
    let lower = raw.to_lowercase();
    for line in lower.lines() {
        if line.trim().starts_with("refer:") {
            let refer = line.split(':').nth(1).map(|s| s.trim());
            if let Some(ref refer_server) = refer {
                if !refer_server.is_empty() && *refer_server != "whois.iana.org" {
                    let redirect = query_whois(domain, refer_server);
                    if !redirect.starts_with("ERROR:") {
                        return redirect;
                    }
                }
            }
            break;
        }
    }
    raw.to_string()
}

fn get_whois_server(tld: &str) -> &str {
    WHOIS_SERVERS.get(tld).copied().unwrap_or("whois.iana.org")
}

const WHOIS_SERVERS: phf::Map<&'static str, &'static str> = phf::phf_map! {
    "com" => "whois.verisign-grs.com",
    "net" => "whois.verisign-grs.com",
    "org" => "whois.pir.org",
    "info" => "whois.afilias.net",
    "biz" => "whois.nic.biz",
    "io" => "whois.nic.io",
    "co" => "whois.nic.co",
    "me" => "whois.nic.me",
    "es" => "whois.nic.es",
    "mx" => "whois.nic.mx",
    "cl" => "whois.nic.cl",
    "ar" => "whois.nic.ar",
    "pe" => "kero.yachay.pe",
    "us" => "whois.nic.us",
    "la" => "whois.nic.la",
    "tv" => "whois.nic.tv",
    "cc" => "whois.nic.cc",
    "br" => "whois.registro.br",
    "ru" => "whois.tcinet.ru",
    "uk" => "whois.nic.uk",
    "fr" => "whois.nic.fr",
    "de" => "whois.denic.de",
    "it" => "whois.nic.it",
    "nl" => "whois.domain-registry.nl",
    "cn" => "whois.cnnic.cn",
    "in" => "whois.registry.in",
    "to" => "whois.tonic.to",
    "eu" => "whois.eu",
    "ai" => "whois.nic.ai",
    "app" => "whois.nic.google",
    "dev" => "whois.nic.google",
    "xyz" => "whois.nic.xyz",
    "shop" => "whois.nic.shop",
    "site" => "whois.nic.site",
    "online" => "whois.nic.online",
};
