use std::net::ToSocketAddrs;

pub fn resolve_dns(domain: &str) -> Option<String> {
    let addr = format!("{}:0", domain);
    match addr.to_socket_addrs() {
        Ok(mut addrs) => addrs
            .find(|a| a.is_ipv4())
            .map(|a| a.ip().to_string()),
        Err(_) => None,
    }
}
