#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import re
import time
from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

# ==========================================
# MOTOR DE DETECCIÓN HÍBRIDO (Consistencia con LiberDom CLI)
# ==========================================

def registrar_whois_servidor(domain, server=None):
    """Realiza una consulta WHOIS pura usando sockets TCP en el puerto 43"""
    if not server:
        tld = domain.split('.')[-1].lower()
        tld_servers = {
            'com': 'whois.verisign-grs.com',
            'net': 'whois.verisign-grs.com',
            'org': 'whois.pir.org',
            'info': 'whois.afilias.net',
            'biz': 'whois.nic.biz',
            'io': 'whois.nic.io',
            'co': 'whois.nic.co',
            'me': 'whois.nic.me',
            'es': 'whois.nic.es',
            'mx': 'whois.mx',
            'cl': 'whois.nic.cl',
            'ar': 'whois.nic.ar',
            'pe': 'kero.yachay.pe',
            'us': 'whois.nic.us',
            'la': 'whois.nic.la',
            'tv': 'whois.nic.tv',
            'cc': 'whois.nic.cc',
            'br': 'whois.registro.br',
            'ru': 'whois.tcinet.ru',
            'uk': 'whois.nic.uk',
            'fr': 'whois.nic.fr',
            'de': 'whois.denic.de',
            'it': 'whois.nic.it',
            'nl': 'whois.domain-registry.nl',
            'cn': 'whois.cnnic.cn',
            'in': 'whois.registry.in',
            'to': 'whois.tonic.to',
        }
        server = tld_servers.get(tld, 'whois.iana.org')
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5.0)
        s.connect((server, 43))
        
        if server == 'whois.verisign-grs.com':
            query = f"domain {domain}\r\n"
        elif server == 'whois.denic.de':
            query = f"-T dn {domain}\r\n"
        else:
            query = f"{domain}\r\n"
            
        s.send(query.encode('utf-8', errors='ignore'))
        
        response = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data
        s.close()
        
        try:
            return response.decode('utf-8', errors='ignore')
        except Exception:
            return response.decode('latin-1', errors='ignore')
            
    except Exception as e:
        return f"ERROR: {str(e)}"

def auditar_servidor(domain, ip, res_whois, lang='es'):
    """
    Realiza auditorías de red avanzadas:
    - Extrae o consulta servidores de nombres (NS).
    - Comprueba si cuenta con SSL activo (Puerto 443) y extrae la entidad emisora.
    - Analiza el uso de Cloudflare (Orange Cloud proxied / Gray Cloud DNS-only).
    """
    ns_list = []
    
    # 1. Extraer registros NS desde el WHOIS
    if res_whois:
        for line in res_whois.split('\n'):
            line_clean = line.strip().lower()
            if line_clean.startswith("nserver:") or line_clean.startswith("name server:") or line_clean.startswith("nameserver:"):
                parts = line_clean.split(':', 1)
                if len(parts) > 1:
                    ns_val = parts[1].strip()
                    if ns_val.endswith('.'):
                        ns_val = ns_val[:-1]
                    if ns_val and ns_val not in ns_list:
                        ns_list.append(ns_val)

    # 2. Si no se hallaron NS, intentar mediante comando del sistema nslookup
    if not ns_list:
        try:
            import subprocess
            out = subprocess.check_output(["nslookup", "-type=ns", domain], stderr=subprocess.DEVNULL, timeout=1.5).decode('utf-8', errors='ignore')
            for line in out.split('\n'):
                line_clean = line.strip().lower()
                if "nameserver =" in line_clean:
                    ns_val = line_clean.split("nameserver =", 1)[1].strip()
                    if ns_val.endswith('.'):
                        ns_val = ns_val[:-1]
                    if ns_val and ns_val not in ns_list:
                        ns_list.append(ns_val)
        except Exception:
            pass

    ssl_active = False
    ssl_issuer = None
    is_orange = False
    is_gray = False

    # 3. Comprobar headers HTTP y SSL activo
    if ip:
        # Petición HTTP rápida para detectar cabeceras de proxy de Cloudflare
        try:
            import urllib.request
            req = urllib.request.Request(f"http://{domain}", headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=1.5) as response:
                server = response.headers.get('Server', '').lower()
                if "cloudflare" in server:
                    is_orange = True
        except Exception:
            pass

        # Socket SSL para comprobar el puerto 443
        import ssl
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443), timeout=1.5) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    ssl_active = True
                    if cert and 'issuer' in cert:
                        issuer = dict(x[0] for x in cert['issuer'])
                        ssl_issuer = issuer.get('commonName', 'Unknown Issuer')
                        if "cloudflare" in ssl_issuer.lower():
                            is_orange = True
        except Exception:
            pass

    # 4. Detección de Nube Gris (Usa DNS de Cloudflare pero no está proxificado)
    has_cf_ns = any("cloudflare" in ns for ns in ns_list)
    if has_cf_ns:
        if not is_orange:
            is_gray = True

    cloudflare_status = "none"
    if is_orange:
        cloudflare_status = "orange"
    elif is_gray:
        cloudflare_status = "gray"

    return {
        "ns": ns_list,
        "ssl_active": ssl_active,
        "ssl_issuer": ssl_issuer,
        "cloudflare": cloudflare_status
    }

def chequear_dominio(domain, dns_only=False, lang='es', realizar_auditoria=True):
    """Determina si un dominio está libre (disponible) o comprado (registrado)"""
    domain = domain.strip().lower()
    
    # Validar formato
    if not '.' in domain or len(domain) < 4:
        msg = "Formato inválido (Ej: misitio.com)" if lang == 'es' else "Invalid format (e.g. mysite.com)"
        return "invalido", msg, {}

    domain = re.sub(r'^(https?://)?(www\.)?', '', domain)
    domain = domain.split('/')[0]

    info = {
        "dominio": domain,
        "metodo": "Ninguno" if lang == 'es' else "None",
        "ip": None,
        "whois_server": None,
        "fecha_creacion": None,
        "registrador": None,
        "ns": [],
        "ssl_active": False,
        "ssl_issuer": None,
        "cloudflare": "none"
    }

    # 1. DNS Lookup Rápido
    try:
        ip = socket.gethostbyname(domain)
        info["ip"] = ip
        info["metodo"] = "Resolución DNS" if lang == 'es' else "DNS Resolution"
        msg = "Registrado (Activo por DNS)" if lang == 'es' else "Registered (Active via DNS)"
        
        if realizar_auditoria:
            audit = auditar_servidor(domain, ip, None, lang)
            info.update(audit)
            
        return "comprado", msg, info
    except socket.gaierror:
        if dns_only:
            info["metodo"] = "Verificación DNS Rápida" if lang == 'es' else "Fast DNS Verification"
            msg = "Disponible (Por DNS - Sin registros activos)" if lang == 'es' else "Available (via DNS - No active records)"
            return "disponible", msg, info
        pass

    # 2. WHOIS
    res = registrar_whois_servidor(domain)
    if res.startswith("ERROR:"):
        err_msg = res[6:]
        msg = f"Error de servidor WHOIS ({err_msg})" if lang == 'es' else f"WHOIS server error ({err_msg})"
        return "desconocido", msg, info

    res_lower = res.lower()
    refer_server = None
    if "refer:" in res_lower:
        lines = res.split('\n')
        for line in lines:
            if line.lower().startswith("refer:"):
                refer_server = line.split(":", 1)[1].strip()
                break
                
    if refer_server:
        info["whois_server"] = refer_server
        res = registrar_whois_servidor(domain, refer_server)
        if not res.startswith("ERROR:"):
            res_lower = res.lower()
        else:
            msg = f"Error al redirigir WHOIS a {refer_server}" if lang == 'es' else f"Error redirecting WHOIS to {refer_server}"
            return "desconocido", msg, info

    # Analizar si está disponible
    patrones_disponible = [
        "no match", "not found", "available", "no entries found",
        "no data found", "free", "status: free", "incorrect domain name",
        "is free", "no registered", "not registered", "no object found",
        "domain not found", "is available", "no match for", "no se encuentra",
        "el dominio no existe", "no matching record", "no domain found",
        "object_not_found"
    ]
    
    esta_disponible = False
    for patron in patrones_disponible:
        if patron in res_lower:
            esta_disponible = True
            break

    info["metodo"] = "Consulta WHOIS Socket 43" if lang == 'es' else "WHOIS Socket 43 Query"

    if esta_disponible:
        msg = "¡Disponible para registro!" if lang == 'es' else "Available for registration!"
        return "disponible", msg, info
    
    # Analizar si está comprado
    patrones_comprado = [
        "registrar:", "creation date:", "domain name:", "registry domain id:",
        "status: registered", "registered:", "expir", "changed:", "owner:"
    ]
    
    esta_comprado = False
    for patron in patrones_comprado:
        if patron in res_lower:
            esta_comprado = True
            break
            
    # Extraer campos
    for line in res.split('\n'):
        line_clean = line.strip()
        line_lower = line_clean.lower()
        if "creation date" in line_lower or "created:" in line_lower or "fecha de creacion" in line_lower:
            parts = line_clean.split(':', 1)
            if len(parts) > 1:
                info["fecha_creacion"] = parts[1].strip()
        if "registrar:" in line_lower or "registrador:" in line_lower:
            parts = line_clean.split(':', 1)
            if len(parts) > 1:
                info["registrador"] = parts[1].strip()

    if esta_comprado or len(res) > 250:
        msg = "Registrado (Confirmado por WHOIS)" if lang == 'es' else "Registered (Confirmed by WHOIS)"
        
        if realizar_auditoria:
            audit = auditar_servidor(domain, info["ip"], res, lang)
            info.update(audit)
            
        return "comprado", msg, info
    else:
        msg = "No se pudo determinar (Límite WHOIS / TLD no soportado)" if lang == 'es' else "Could not determine (WHOIS Limit / TLD not supported)"
        return "desconocido", msg, info

# ==========================================
# RUTAS DE LA APLICACIÓN FLASK
# ==========================================

@app.route('/')
def home():
    """Sirve la página web visual principal"""
    return render_template("index.html")

@app.route('/api/check')
def api_check():
    """Endpoint API para buscar un dominio individual"""
    domain = request.args.get('domain', '').strip()
    dns_only = request.args.get('dns_only', 'false').lower() == 'true'
    realizar_auditoria = request.args.get('audit', 'true').lower() == 'true'
    lang = request.args.get('lang', 'es').strip().lower()
    
    if lang not in ['es', 'en']:
        lang = 'es'
        
    if not domain:
        err_msg = "Falta el parámetro 'domain'" if lang == 'es' else "Missing parameter 'domain'"
        return jsonify({"status": "error", "message": err_msg}), 400
        
    estado, detalle, info = chequear_dominio(domain, dns_only=dns_only, lang=lang, realizar_auditoria=realizar_auditoria)
    
    return jsonify({
        "status": "success",
        "domain": domain,
        "estado": estado,
        "detalle": detalle,
        "info": info
    })

if __name__ == '__main__':
    # Ejecutar servidor Flask en el puerto 5000
    print("🚀 Iniciando Servidor Web de OpenFind...")
    print("👉 Abre en tu navegador: http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
