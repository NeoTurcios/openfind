#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
import time
import os
import re
import json

# ==========================================
# PALETA DE COLORES ANSI (Para Termux)
# ==========================================
VERDE = "\033[1;92m"
ROJO = "\033[1;91m"
AMARILLO = "\033[1;93m"
AZUL = "\033[1;94m"
MAGENTA = "\033[1;95m"
CIAN = "\033[1;96m"
BLANCO = "\033[1;97m"
GRIS = "\033[90m"
FIN = "\033[0m"
NEGRITA = "\033[1m"
CURSIVA = "\033[3m"

# ==========================================
# CONFIGURACIÓN PERSISTENTE DE IDIOMA (I18N)
# ==========================================
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".openfind_config.json")
CONFIG = {"lang": "es"}

def cargar_configuracion():
    global CONFIG
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                CONFIG = json.load(f)
        except Exception:
            pass
    if "lang" not in CONFIG:
        CONFIG["lang"] = "es"

def guardar_configuracion():
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(CONFIG, f, indent=4)
    except Exception:
        pass

# Diccionario de Textos de la Interfaz CLI
TEXTS = {
    "es": {
        "banner_sub": "¡Optimizado para Termux!",
        "menu_titulo": "💻  MENÚ PRINCIPAL EN ESPAÑOL  💻",
        "menu_opcion_1": "🔍 Buscar un dominio individual",
        "menu_opcion_2": "📂 Buscar por lote (archivo txt)",
        "menu_opcion_3": "💡 Generador de nombres + Verificar disponibilidad",
        "menu_opcion_4": "📘 Guía de ayuda / Consejos",
        "menu_opcion_5": "🌐 Cambiar Idioma (Change Language)",
        "menu_opcion_6": "👋 Salir del script",
        "ingresar_opcion": "👉 Selecciona una opción (1-6): ",
        "opcion_incorrecta": "❌ Opción incorrecta. Inténtalo de nuevo.",
        "salir_mensaje": "👋 ¡Gracias por usar OpenFind! Diseñado para optimizar tus proyectos.\n¡Haz tu repositorio público y compártelo con el mundo! 🚀",
        "interrumpido": "\n\n⚠ Script interrumpido por el usuario. ¡Adiós!\n",
        
        # Consulta Individual
        "ind_title": "╔══[ OPCIÓN 1: BÚSQUEDA INDIVIDUAL ]═════════════════════════╗",
        "ind_instr_1": "║ Escribe el dominio completo que deseas buscar.            ║",
        "ind_instr_2": "║ Ejemplos: midominio.com, proyecto.net, app.co, web.es       ║",
        "ind_prompt": "👉 Ingresa el dominio: ",
        "ind_empty": "❌ No ingresaste ningún dominio.",
        "enter_prev_menu": "Presiona ENTER para volver al menú anterior...",
        "enter_main_menu": "Presiona ENTER para regresar al menú principal...",
        "querying_db": "Consultando base de datos mundial de dominios...",
        "results_for": "📊 RESULTADOS PARA:",
        "status_avail_desc": "¡Felicidades! Este dominio está libre. Puedes registrarlo.",
        "info_header": "Información del registro:",
        "info_ip": "• IP de Servidor:",
        "info_registrar": "• Registrado con:",
        "info_date": "• Fecha Creación:",
        "info_method": "• Método de detección:",
        "unknown_help": "Intenta buscarlo directamente en tu navegador web o proveedor DNS.",
        "ind_prompt_audit": "👉 ¿Desea realizar una Auditoría de Servidor Avanzada (SSL/Cloudflare/NS)? (s/n) [Enter para Sí]: ",
        "lote_prompt_audit": "👉 ¿Desea realizar una Auditoría de Servidor Avanzada (SSL/Cloudflare/NS) para los dominios del lote? (s/n) [Enter para Sí]: ",
        "info_ssl_active": "• SSL Activo:",
        "info_ssl_issuer": "• Emisor SSL:",
        "info_ns": "• Servidores de Nombres (NS):",
        "info_cloudflare": "• Estado Cloudflare:",
        "cf_orange": "Nube Naranja (Proxificado)",
        "cf_gray": "Nube Gris (Solo DNS)",
        "cf_none": "No utiliza Cloudflare",
        
        # Consulta Lote
        "lote_title": "╔══[ OPCIÓN 2: BÚSQUEDA EN LOTE / MASIVA ]═══════════════════╗",
        "lote_instr_1": "║ Comprueba listas grandes de dominios con alta velocidad.   ║",
        "lote_instr_2": "║ Puedes usar un archivo .txt o pegar texto directamente.    ║",
        "lote_prompt_type": "¿Cómo deseas ingresar los dominios?",
        "lote_type_file": "Cargar desde un archivo de texto (.txt)",
        "lote_type_paste": "Pegar lista de dominios directamente en la consola",
        "select_1_2": "👉 Selecciona una opción (1-2): ",
        "file_prompt": "👉 Escribe el nombre o ruta del archivo (Ej: dominios.txt): ",
        "file_not_exist": "⚠ El archivo '{ruta}' no existe. ¿Quieres crear un archivo demo con ejemplos? (s/n): ",
        "file_demo_created": "✔ Archivo '{ruta}' creado con 8 dominios de ejemplo.",
        "file_read_error": "❌ Error al leer el archivo: ",
        "paste_instr_1": "👉 Pega tus dominios a continuación.",
        "paste_instr_2": "Puedes separarlos por comas, espacios o saltos de línea.",
        "paste_instr_3": "Cuando termines, escribe FIN en una línea sola y presiona ENTER:",
        "paste_warn": "Escribe tus dominios o 'FIN' para salir.",
        "lote_no_valid": "❌ No se encontraron dominios válidos para analizar.",
        "lote_processing": "✔ Se procesarán {total} dominios únicos.",
        "lote_duplicates": "💡 Se omitieron {duplicados} dominios duplicados/inválidos.",
        "scan_mode_title": "Selecciona el MODO DE ESCANEO para la lista:",
        "scan_mode_dns_title": "Modo Ultra-Rápido (Solo DNS):",
        "scan_mode_dns_desc": "     Comprueba si el dominio resuelve IP. Inmediato, sin límites de velocidad.\n     Recomendado para listas gigantes (más de 100 dominios).",
        "scan_mode_hybrid_title": "Modo Híbrido Completo (DNS + WHOIS):",
        "scan_mode_hybrid_desc": "     Comprobación oficial de registro en bases de datos mundiales.\n     Recomendado para listas cortas/medianas para evitar bloqueos WHOIS.",
        "select_mode": "👉 Selecciona modo (1 o 2): ",
        "rate_limit_warn": "Para evitar que los servidores WHOIS bloqueen tu IP (Rate Limit), se aconseja un retraso:",
        "suggest_delay_50": "  • Sugerido para tu lista (>50 dominios): 1.5 a 2.0 segundos",
        "suggest_delay_20": "  • Sugerido para tu lista (>20 dominios): 1.0 segundo",
        "suggest_delay_short": "  • Sugerido para tu lista: 0.4 segundos",
        "delay_prompt": "👉 Retraso en segundos entre búsquedas [Enter para el sugerido]: ",
        "save_prompt": "¿Quieres guardar los resultados en un archivo de texto? (s/n): ",
        "report_header": "=== RESULTADOS DE BÚSQUEDA DE DOMINIOS ===",
        "report_date": "Fecha: ",
        "report_mode": "Modo: ",
        "report_total": "Total de dominios únicos analizados: ",
        "report_dns_only": "Solo DNS (Rápido)",
        "report_hybrid": "Híbrido DNS+WHOIS",
        "scanning_item": "Escaneando {dom}...",
        "libre_dns": "Libre por DNS",
        "libre_whois": "Libre (WHOIS)",
        "scan_finished_saved": "✔ ¡Escaneo finalizado en {duracion:.1f}s! Resultados guardados en: {archivo}",
        "scan_finished": "✔ ¡Escaneo finalizado en {duracion:.1f}s!",
        "summary_label": "Resumen: {disponibles} Disponibles | {comprados} Comprados | {desconocidos} Desconocidos",
        
        # Generador de nombres
        "gen_title": "╔══[ OPCIÓN 3: GENERADOR E IDEAS DE DOMINIOS ]═══════════════╗",
        "gen_instr": "║ Mezcla palabras clave con TLDs para encontrar ideas libres ║",
        "gen_prompt": "👉 Escribe una palabra clave (Ej: tecno, app, net): ",
        "gen_empty": "❌ Entrada vacía.",
        "gen_tld_prompt": "Elige las extensiones (TLDs) a combinar (Separadas por comas):",
        "gen_tlds_default": "👉 Extensiones [por defecto: com, net, co]: ",
        "gen_style_title": "Elige el estilo de combinación:",
        "gen_style_1": "1. Palabra + sufijo (Ej: {palabra}hub, {palabra}app, {palabra}lab)",
        "gen_style_2": "2. Prefijo + palabra (Ej: super{palabra}, go{palabra}, check{palabra})",
        "gen_style_3": "3. Palabra exacta con múltiples TLDs (Ej: {palabra}.com, {palabra}.net)",
        "gen_style_4": "4. Estilo moderno de IA (Ej: {palabra}ai.com, my{palabra}ai.net)",
        "gen_select_style": "👉 Elige una opción (1-4): ",
        "gen_ready": "✔ Se generaron {total} ideas de dominios para comprobar.",
        "gen_start_check": "¿Quieres empezar a verificar cuáles están libres ahora mismo? (s/n): ",
        "gen_header_dom": "DOMINIO GENERADO",
        "gen_header_status": "ESTADO",
        "gen_avail": "✔ ¡DISPONIBLE!",
        "gen_taken": "❌ Comprado",
        "gen_unk": "? Desconocido",
        "gen_summary": "⭐ Fin del análisis. Encontraste {libres} dominios listos para comprar.",
        
        # Guía de ayuda
        "help_title": "╔══[ OPCIÓN 4: GUÍA DE AYUDA / CONSEJOS ]════════════════════╗",
        "help_body": """{NEGRITA}{CIAN}📘 CONSEJOS E INSTRUCCIONES DE USO (Termux) {FIN}

{NEGRITA}{AMARILLO}1. Límites de consulta (Rate Limiting){FIN}
Los servidores WHOIS mundiales tienen protección contra spam. Si buscas 
demasiados dominios en pocos minutos, el servidor podría bloquear temporalmente 
las peticiones y verás el estado como "DESCONOCIDO" o "LÍMITE". 
• {CURSIVA}Solución: Espera un par de minutos o usa una VPN/cambia de IP.{FIN}

{NEGRITA}{AMARILLO}2. Dominios Especiales (.es, .ar, .cl, etc.){FIN}
Algunos países tienen políticas WHOIS muy estrictas y no permiten consultas 
masivas directas por sockets libres. Si no se puede verificar un TLD local, 
el script te avisará para comprobarlo por vía DNS o manual.

{NEGRITA}{AMARILLO}3. Formato del archivo para búsquedas en Lote{FIN}
Crea tu lista en un archivo de texto plano como {CIAN}dominios.txt{FIN}.
Cada dominio debe ir en una línea separada. Ejemplo:
    {BLANCO}misitio.com
    tusitio.net
    otroweb.io{FIN}

{NEGRITA}{AMARILLO}4. Licencia No Comercial y Atribución Obligatoria{FIN}
Este proyecto es público y de código abierto. Se permiten colaboraciones,
modificaciones del diseño, logotipo, nombre, paquete y funciones para su
redistribución, siempre y cuando:
• {CURSIVA}Quede estrictamente prohibida la venta o uso comercial de este código.{FIN}
• {CURSIVA}Se mantenga de forma visible el enlace al repositorio original de GitHub:{FIN}
  https://github.com/NeoTurcios/liberdom.git (Basado en el motor LiberDom)
"""
    },
    "en": {
        "banner_sub": "Optimized for Termux!",
        "menu_titulo": "💻  MAIN MENU IN ENGLISH  💻",
        "menu_opcion_1": "🔍 Search an individual domain",
        "menu_opcion_2": "📂 Bulk search (txt file)",
        "menu_opcion_3": "💡 Name generator + Check availability",
        "menu_opcion_4": "📘 Help guide / Tips",
        "menu_opcion_5": "🌐 Change Language (Cambiar Idioma)",
        "menu_opcion_6": "👋 Exit the script",
        "ingresar_opcion": "👉 Select an option (1-6): ",
        "opcion_incorrecta": "❌ Incorrect option. Try again.",
        "salir_mensaje": "👋 Thank you for using OpenFind! Designed to optimize your projects.\nMake your repository public and share it with the world! 🚀",
        "interrumpido": "\n\n⚠ Script interrupted by the user. Goodbye!\n",
        
        # Individual Search
        "ind_title": "╔══[ OPTION 1: INDIVIDUAL SEARCH ]═══════════════════════════╗",
        "ind_instr_1": "║ Enter the complete domain you wish to search.             ║",
        "ind_instr_2": "║ Examples: mydomain.com, project.net, app.co, web.es       ║",
        "ind_prompt": "👉 Enter the domain: ",
        "ind_empty": "❌ You did not enter any domain.",
        "enter_prev_menu": "Press ENTER to return to the previous menu...",
        "enter_main_menu": "Press ENTER to return to the main menu...",
        "querying_db": "Querying global domain database...",
        "results_for": "📊 RESULTS FOR:",
        "status_avail_desc": "Congratulations! This domain is free. You can register it.",
        "info_header": "Registration information:",
        "info_ip": "• Server IP:",
        "info_registrar": "• Registered with:",
        "info_date": "• Creation Date:",
        "info_method": "• Detection method:",
        "unknown_help": "Try searching for it directly in your web browser or DNS provider.",
        "ind_prompt_audit": "👉 Do you want to perform an Advanced Server Audit (SSL/Cloudflare/NS)? (y/n) [Enter for Yes]: ",
        "lote_prompt_audit": "👉 Do you want to perform an Advanced Server Audit (SSL/Cloudflare/NS) for the batch domains? (y/n) [Enter for Yes]: ",
        "info_ssl_active": "• Active SSL:",
        "info_ssl_issuer": "• SSL Issuer:",
        "info_ns": "• Name Servers (NS):",
        "info_cloudflare": "• Cloudflare Status:",
        "cf_orange": "Orange Cloud (Proxied)",
        "cf_gray": "Gray Cloud (DNS-only)",
        "cf_none": "Does not use Cloudflare",
        
        # Bulk Search
        "lote_title": "╔══[ OPTION 2: BULK / MASSIVE SEARCH ]══════════════════════╗",
        "lote_instr_1": "║ Check large lists of domains at high speed.                ║",
        "lote_instr_2": "║ You can use a .txt file or paste text directly.            ║",
        "lote_prompt_type": "How do you want to enter the domains?",
        "lote_type_file": "Load from a text file (.txt)",
        "lote_type_paste": "Paste domain list directly in the console",
        "select_1_2": "👉 Select an option (1-2): ",
        "file_prompt": "👉 Enter the filename or path (e.g. domains.txt): ",
        "file_not_exist": "⚠ File '{ruta}' does not exist. Do you want to create a demo file with examples? (y/n): ",
        "file_demo_created": "✔ File '{ruta}' created with 8 example domains.",
        "file_read_error": "❌ Error reading file: ",
        "paste_instr_1": "👉 Paste your domains below.",
        "paste_instr_2": "You can separate them by commas, spaces, or line breaks.",
        "paste_instr_3": "When finished, type FIN on a line by itself and press ENTER:",
        "paste_warn": "Enter your domains or 'FIN' to exit.",
        "lote_no_valid": "❌ No valid domains found to analyze.",
        "lote_processing": "✔ {total} unique domains will be processed.",
        "lote_duplicates": "💡 {duplicados} duplicate/invalid domains were omitted.",
        "scan_mode_title": "Select the SCAN MODE for the list:",
        "scan_mode_dns_title": "Ultra-Fast Mode (DNS Only):",
        "scan_mode_dns_desc": "     Checks if the domain resolves IP. Immediate, without rate limits.\n     Recommended for giant lists (more than 100 domains).",
        "scan_mode_hybrid_title": "Full Hybrid Mode (DNS + WHOIS):",
        "scan_mode_hybrid_desc": "     Official registration check in global databases.\n     Recommended for short/medium lists to avoid WHOIS blocks.",
        "select_mode": "👉 Select mode (1 or 2): ",
        "rate_limit_warn": "To prevent WHOIS servers from blocking your IP (Rate Limit), a delay is advised:",
        "suggest_delay_50": "  • Suggested for your list (>50 domains): 1.5 to 2.0 seconds",
        "suggest_delay_20": "  • Suggested for your list (>20 domains): 1.0 second",
        "suggest_delay_short": "  • Suggested for your list: 0.4 seconds",
        "delay_prompt": "👉 Delay in seconds between searches [Enter for suggested]: ",
        "save_prompt": "Do you want to save results to a text file? (y/n): ",
        "report_header": "=== DOMAIN SEARCH RESULTS ===",
        "report_date": "Date: ",
        "report_mode": "Mode: ",
        "report_total": "Total unique domains analyzed: ",
        "report_dns_only": "DNS Only (Fast)",
        "report_hybrid": "Hybrid DNS+WHOIS",
        "scanning_item": "Scanning {dom}...",
        "libre_dns": "Free by DNS",
        "libre_whois": "Free (WHOIS)",
        "scan_finished_saved": "✔ Scan finished in {duracion:.1f}s! Results saved to: {archivo}",
        "scan_finished": "✔ Scan finished in {duracion:.1f}s!",
        "summary_label": "Summary: {disponibles} Available | {comprados} Registered | {desconocidos} Unknown",
        
        # Name generator
        "gen_title": "╔══[ OPTION 3: DOMAIN GENERATOR & IDEAS ]════════════════════╗",
        "gen_instr": "║ Mix keywords with TLDs to find available ideas             ║",
        "gen_prompt": "👉 Enter a keyword (e.g. tecno, app, net): ",
        "gen_empty": "❌ Empty input.",
        "gen_tld_prompt": "Choose the extensions (TLDs) to combine (Separated by commas):",
        "gen_tlds_default": "👉 Extensions [default: com, net, co]: ",
        "gen_style_title": "Choose the combination style:",
        "gen_style_1": "1. Keyword + suffix (e.g. {palabra}hub, {palabra}app, {palabra}lab)",
        "gen_style_2": "2. Prefix + keyword (e.g. super{palabra}, go{palabra}, check{palabra})",
        "gen_style_3": "3. Exact keyword with multiple TLDs (e.g. {palabra}.com, {palabra}.net)",
        "gen_style_4": "4. Modern AI style (e.g. {palabra}ai.com, my{palabra}ai.net)",
        "gen_select_style": "👉 Choose an option (1-4): ",
        "gen_ready": "✔ Generated {total} domain ideas to check.",
        "gen_start_check": "Do you want to start checking which ones are free right now? (y/n): ",
        "gen_header_dom": "GENERATED DOMAIN",
        "gen_header_status": "STATUS",
        "gen_avail": "✔ AVAILABLE!",
        "gen_taken": "❌ Registered",
        "gen_unk": "? Unknown",
        "gen_summary": "⭐ End of analysis. You found {libres} domains ready to register.",
        
        # Help guide
        "help_title": "╔══[ OPTION 4: HELP GUIDE / ADVICE ]═════════════════════════╗",
        "help_body": """{NEGRITA}{CIAN}📘 USER TIPS AND INSTRUCTIONS (Termux) {FIN}

{NEGRITA}{AMARILLO}1. Query Limits (Rate Limiting){FIN}
Global WHOIS servers have protection against spam. If you search too 
many domains in a few minutes, the server might temporarily block 
requests and you will see the status as "UNKNOWN" or "LIMIT". 
• {CURSIVA}Solution: Wait a couple of minutes or use a VPN/change your IP.{FIN}

{NEGRITA}{AMARILLO}2. Special Domains (.es, .ar, .cl, etc.){FIN}
Some countries have very strict WHOIS policies and do not allow raw 
bulk socket queries. If a local TLD cannot be verified, the script 
will notify you to check it via DNS or manually.

{NEGRITA}{AMARILLO}3. File format for bulk searches{FIN}
Create your list in a plain text file like {CIAN}domains.txt{FIN}.
Each domain must be on a separate line. Example:
    {BLANCO}mysite.com
    yoursite.net
    otherweb.io{FIN}

{NEGRITA}{AMARILLO}4. Non-Commercial & Attribution Required License{FIN}
This project is open-source. Collaborations, redesigns, and modifications of the 
logo, name, package, visual theme, and features are permitted for redistribution, 
as long as:
• {CURSIVA}Selling, reselling, or commercial use of this code is strictly prohibited.{FIN}
• {CURSIVA}You prominently display the link to the original GitHub repository:{FIN}
  https://github.com/NeoTurcios/liberdom.git (Based on the LiberDom engine)
"""
    }
}

# Limpiar pantalla según el sistema operativo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Banner estilizado
def mostrar_banner():
    lang = CONFIG["lang"]
    sub = TEXTS[lang]["banner_sub"]
    padding = " " * ((38 - len(sub)) // 2)
    right_padding = " " * (38 - len(sub) - len(padding))
    banner = f"""
{CIAN}╔═══════════════════════════════════════════════════════════════╗
║  {VERDE} ██████╗ ██████╗ ███████╗███╗   ██╗███████╗██╗███╗   ██╗██████╗ {CIAN} ║
║  {VERDE}██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██║████╗  ██║██╔══██╗{CIAN} ║
║  {VERDE}██║   ██║██████╔╝█████╗  ██╔██╗ ██║█████╗  ██║██╔██╗ ██║██║  ██║{CIAN} ║
║  {VERDE}██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══╝  ██║██║╚██╗██║██║  ██║{CIAN} ║
║  {VERDE}╚██████╔╝██║     ███████╗██║ ╚████║██║     ██║██║ ╚████║██████╔╝{CIAN} ║
║  {VERDE} ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ {CIAN} ║
╠═══════════════════════════════════════════════════════════════╣
║         {BLANCO}🔍    OpenFind AI - Detector de Dominios Libre    🔍      {CIAN}║
║               {AMARILLO}{padding}{sub}{right_padding}{CIAN}            ║
╚═══════════════════════════════════════════════════════════════╝{FIN}"""
    print(banner)
    print(f" {GRIS}Original Repository: https://github.com/NeoTurcios/liberdom{FIN}")

# ==========================================
# MOTOR DE BÚSQUEDA Y DETECCION WHOIS/DNS
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
        s.settimeout(3.0)
        s.connect((server, 43))
        
        # Ajustes de formato de consulta para servidores especiales
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
    """
    Determina si un dominio está libre (disponible) o comprado (registrado).
    Retorna: (estado, detalle_localizado, info_adicional)
    """
    domain = domain.strip().lower()
    
    # Validar formato básico de dominio
    if not '.' in domain or len(domain) < 4:
        msg = "Formato inválido (Ej: misitio.com)" if lang == 'es' else "Invalid format (e.g. mysite.com)"
        return "invalido", msg, {}

    # Quitar protocolos si el usuario los ingresó por error
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

    # ----------------------------------------------------
    # MÈTODO 1: DNS Lookup (Súper Rápido)
    # ----------------------------------------------------
    try:
        ip = socket.gethostbyname(domain)
        info["ip"] = ip
        info["metodo"] = "Resolución DNS" if lang == 'es' else "DNS Resolution"
        msg = "COMPRADO / REGISTRADO (Activo por DNS)" if lang == 'es' else "REGISTERED (Active via DNS)"
        
        # Realizar auditorías avanzadas de red si está activo
        if realizar_auditoria:
            audit = auditar_servidor(domain, ip, None, lang)
            info.update(audit)
            
        return "comprado", msg, info
    except socket.gaierror:
        if dns_only:
            info["metodo"] = "Verificación DNS Rápida" if lang == 'es' else "Fast DNS Verification"
            msg = "DISPONIBLE (Por DNS - Sin registros activos)" if lang == 'es' else "AVAILABLE (via DNS - No active records)"
            return "disponible", msg, info
        pass

    # ----------------------------------------------------
    # MÈTODO 2: Consulta WHOIS (100% Preciso)
    # ----------------------------------------------------
    res = registrar_whois_servidor(domain)
    
    if res.startswith("ERROR:"):
        err_msg = res[6:]
        msg = f"Error de red/servidor WHOIS ({err_msg})" if lang == 'es' else f"Network/WHOIS server error ({err_msg})"
        return "desconocido", msg, info

    # Analizar respuesta de IANA (si redirige a otro servidor)
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

    # ----------------------------------------------------
    # PARSEO DE RESULTADOS EN BÚSQUEDA DE SEÑALES DE LIBRE
    # ----------------------------------------------------
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
        msg = "¡DISPONIBLE! (No está registrado)" if lang == 'es' else "AVAILABLE! (Not registered)"
        return "disponible", msg, info
    
    # Si no tiene patrones de libre, buscar campos típicos de comprado
    patrones_comprado = [
        "registrar:", "creation date:", "domain name:", "registry domain id:",
        "status: registered", "registered:", "expir", "changed:", "owner:"
    ]
    
    esta_comprado = False
    for patron in patrones_comprado:
        if patron in res_lower:
            esta_comprado = True
            break
            
    # Intentar extraer info útil de WHOIS
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
        msg = "COMPRADO / REGISTRADO (Confirmado por WHOIS)" if lang == 'es' else "REGISTERED (Confirmed by WHOIS)"
        
        # Realizar auditorías avanzadas de red si está activo
        if realizar_auditoria:
            audit = auditar_servidor(domain, info["ip"], res, lang)
            info.update(audit)
            
        return "comprado", msg, info
    else:
        msg = "No se pudo determinar con certeza (Límite WHOIS / TLD no soportado)" if lang == 'es' else "Could not determine with certainty (WHOIS Limit / TLD not supported)"
        return "desconocido", msg, info

# ==========================================
# INTERFAZ DE USUARIO E INTERACCIÓN
# ==========================================

def mostrar_animacion_carga():
    """Muestra un spinner elegante mientras se realiza la consulta"""
    lang = CONFIG["lang"]
    msg = TEXTS[lang]["querying_db"]
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for i in range(8):
        for char in spinner:
            sys.stdout.write(f"\r{CIAN}[{char}] {AMARILLO}{msg}{FIN}")
            sys.stdout.flush()
            time.sleep(0.02)
    sys.stdout.write("\r" + " " * 75 + "\r")
    sys.stdout.flush()

def consulta_individual():
    lang = CONFIG["lang"]
    t = TEXTS[lang]
    
    limpiar_pantalla()
    mostrar_banner()
    print(f"\n{NEGRITA}{CIAN}{t['ind_title']}{FIN}")
    print(f"{t['ind_instr_1']}")
    print(f"{t['ind_instr_2']}")
    print(f"{CIAN}╚════════════════════════════════════════════════════════════╝{FIN}\n")
    
    dominio = input(f"{BLANCO}{t['ind_prompt']}{FIN}").strip()
    if not dominio:
        print(f"\n{ROJO}{t['ind_empty']}{FIN}")
        input(f"\n{GRIS}{t['enter_prev_menu']}{FIN}")
        return

    # Preguntar por la Auditoría de Servidor Avanzada (SSL/Cloudflare/NS)
    auditar_input = input(f"{BLANCO}{t['ind_prompt_audit']}{FIN}").strip().lower()
    realizar_auditoria = auditar_input not in ['n', 'no']

    print()
    mostrar_animacion_carga()
    
    estado, detalle, info = chequear_dominio(dominio, lang=lang, realizar_auditoria=realizar_auditoria)
    
    print(f"{CIAN}{t['results_for']}{FIN} {NEGRITA}{BLANCO}{dominio.upper()}{FIN}\n")
    
    if estado == "disponible":
        print(f"  {VERDE}███████████████████████████████████████████████")
        print(f"  ██ [✔] {detalle.upper()} ██")
        print(f"  ███████████████████████████████████████████████{FIN}\n")
        print(f"  {NEGRITA}{VERDE}{t['status_avail_desc']}{FIN}")
    elif estado == "comprado":
        print(f"  {ROJO}███████████████████████████████████████████████")
        print(f"  ██ [❌] {detalle.upper()} ██")
        print(f"  ███████████████████████████████████████████████{FIN}\n")
        print(f"  {AMARILLO}{t['info_header']}{FIN}")
        if info["ip"]:
            print(f"  {BLANCO}{t['info_ip']}{FIN} {CIAN}{info['ip']}{FIN}")
        if info["registrador"]:
            print(f"  {BLANCO}{t['info_registrar']}{FIN} {CIAN}{info['registrador']}{FIN}")
        if info["fecha_creacion"]:
            print(f"  {BLANCO}{t['info_date']}{FIN} {CIAN}{info['fecha_creacion']}{FIN}")
        print(f"  {BLANCO}{t['info_method']}{FIN} {GRIS}{info['metodo']}{FIN}")
        
        if realizar_auditoria:
            # Estado SSL
            ssl_status = f"{VERDE}ACTIVO / ACTIVE{FIN}" if info.get("ssl_active") else f"{ROJO}NO ACTIVO / INACTIVE{FIN}"
            print(f"  {BLANCO}{t['info_ssl_active']}{FIN} {ssl_status}")
            if info.get("ssl_issuer"):
                print(f"  {BLANCO}{t['info_ssl_issuer']}{FIN} {CIAN}{info['ssl_issuer']}{FIN}")
            
            # Estado Cloudflare
            cf_val = info.get("cloudflare", "none")
            if cf_val == "orange":
                cf_display = f"{AMARILLO}☁ {t['cf_orange']}{FIN}"
            elif cf_val == "gray":
                cf_display = f"{GRIS}☁ {t['cf_gray']}{FIN}"
            else:
                cf_display = f"{GRIS}{t['cf_none']}{FIN}"
            print(f"  {BLANCO}{t['info_cloudflare']}{FIN} {cf_display}")
            
            # Servidores de Nombres
            if info.get("ns"):
                ns_str = ", ".join(info.get("ns", []))
                print(f"  {BLANCO}{t['info_ns']}{FIN} {CIAN}{ns_str}{FIN}")
    elif estado == "invalido":
        print(f"  {ROJO}❌ {detalle}{FIN}")
    else:
        print(f"  {AMARILLO}⚠ {detalle}{FIN}")
        print(f"  {GRIS}{t['unknown_help']}{FIN}")
        
    print()
    input(f"{GRIS}{t['enter_main_menu']}{FIN}")

def consulta_lote():
    lang = CONFIG["lang"]
    t = TEXTS[lang]
    
    limpiar_pantalla()
    mostrar_banner()
    print(f"\n{NEGRITA}{CIAN}{t['lote_title']}{FIN}")
    print(f"{t['lote_instr_1']}")
    print(f"{t['lote_instr_2']}")
    print(f"{CIAN}╚════════════════════════════════════════════════════════════╝{FIN}\n")
    
    print(f"{NEGRITA}{BLANCO}{t['lote_prompt_type']}{FIN}")
    print(f" {CIAN}[1]{FIN} {t['lote_type_file']}")
    print(f" {CIAN}[2]{FIN} {t['lote_type_paste']}")
    print()
    
    opcion_ingreso = input(f"{BLANCO}{t['select_1_2']}{FIN}").strip()
    
    lineas = []
    
    if opcion_ingreso == "1":
        # Cargar desde archivo
        ruta_archivo = input(f"\n{BLANCO}{t['file_prompt']}{FIN}").strip()
        
        if not os.path.exists(ruta_archivo):
            crear_demo = input(f"\n{AMARILLO}{t['file_not_exist'].format(ruta=ruta_archivo)}{FIN}").lower()
            if crear_demo in ['s', 'y']:
                ejemplos = [
                    "google.com\n", "midominioquenoexiste12345.com\n", "github.com\n", 
                    "termux-espanol-libre.net\n", "facebook.com\n", "www.youtube.com\n",
                    "http://ejemplolibre999.org\n", "mi-empresa-ideal.co\n"
                ]
                with open(ruta_archivo, "w") as f:
                    f.writelines(ejemplos)
                print(f"{VERDE}{t['file_demo_created'].format(ruta=ruta_archivo)}{FIN}")
            else:
                return

        try:
            with open(ruta_archivo, "r") as f:
                lineas = f.readlines()
        except Exception as e:
            print(f"{ROJO}{t['file_read_error']}{e}{FIN}")
            input(f"\n{GRIS}{t['enter_prev_menu']}{FIN}")
            return
            
    elif opcion_ingreso == "2":
        # Pegar texto directamente
        print(f"\n{AMARILLO}{t['paste_instr_1']}{FIN}")
        print(f"{BLANCO}{t['paste_instr_2']}{FIN}")
        print(f"{GRIS}{t['paste_instr_3']}{FIN}\n")
        
        lineas_pegadas = []
        while True:
            try:
                linea = input().strip()
                if linea.upper() == 'FIN':
                     break
                if linea == '' and len(lineas_pegadas) > 0:
                     break
                if linea == '' and len(lineas_pegadas) == 0:
                     print(f"{ROJO}{t['paste_warn']}{FIN}")
                     continue
                lineas_pegadas.append(linea)
            except (KeyboardInterrupt, EOFError):
                break
        
        lineas = lineas_pegadas
        
    else:
        print(f"\n{ROJO}{t['opcion_incorrecta']}{FIN}")
        time.sleep(1)
        return

    # Limpiar y normalizar dominios
    dominios_crudos = []
    for line in lineas:
        line_clean = line.strip()
        if not line_clean or line_clean.startswith('#'):
            continue
            
        partes = re.split(r'[,\s]+', line_clean)
        for part in partes:
            dom = part.strip().lower()
            dom = re.sub(r'^(https?://)?(www\.)?', '', dom)
            dom = dom.split('/')[0]
            if '.' in dom and len(dom) >= 4:
                dominios_crudos.append(dom)

    total_cargados = len(dominios_crudos)
    dominios = list(dict.fromkeys(dominios_crudos))
    total = len(dominios)
    duplicados = total_cargados - total

    if total == 0:
        print(f"{ROJO}{t['lote_no_valid']}{FIN}")
        input(f"\n{GRIS}{t['enter_prev_menu']}{FIN}")
        return

    print(f"\n{VERDE}{t['lote_processing'].format(total=total)}{FIN}")
    if duplicados > 0:
        print(f"{AMARILLO}{t['lote_duplicates'].format(duplicados=duplicados)}{FIN}")

    # Menú de selección de modo de escaneo
    print(f"\n{NEGRITA}{BLANCO}{t['scan_mode_title']}{FIN}")
    print(f" {CIAN}[1]{FIN} {NEGRITA}{t['scan_mode_dns_title']}{FIN}")
    print(f"{t['scan_mode_dns_desc']}")
    print(f" {CIAN}[2]{FIN} {NEGRITA}{t['scan_mode_hybrid_title']}{FIN}")
    print(f"{t['scan_mode_hybrid_desc']}")
    
    modo = input(f"\n{BLANCO}{t['select_mode']}{FIN}").strip()
    dns_only = True if modo == "1" else False

    # Configuración de retraso (delay)
    retraso = 0.0
    if not dns_only:
        print(f"\n{AMARILLO}{t['rate_limit_warn']}{FIN}")
        if total > 50:
            print(t["suggest_delay_50"])
        elif total > 20:
            print(t["suggest_delay_20"])
        else:
            print(t["suggest_delay_short"])
            
        retraso_input = input(f"{BLANCO}{t['delay_prompt']}{FIN}").strip()
        if retraso_input == "":
            retraso = 1.5 if total > 50 else (1.0 if total > 20 else 0.4)
        else:
            try:
                retraso = float(retraso_input)
            except ValueError:
                retraso = 0.5

    guardar = input(f"\n{BLANCO}{t['save_prompt']}{FIN}").strip().lower()
    guardar_archivo = "resultados_dominios.txt" if guardar in ['s', 'y'] else None
    
    realizar_auditoria = False
    if not dns_only:
        auditar_lote = input(f"{BLANCO}{t['lote_prompt_audit']}{FIN}").strip().lower()
        realizar_auditoria = auditar_lote not in ['n', 'no']

    disponibles = []
    comprados = []
    desconocidos = []
    
    if guardar_archivo:
        f_out = open(guardar_archivo, "w", encoding="utf-8")
        f_out.write(f"{t['report_header']}\n")
        f_out.write(f"{t['report_date']}{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f_out.write(f"{t['report_mode']}{t['report_dns_only'] if dns_only else t['report_hybrid']}\n")
        f_out.write(f"{t['report_total']}{total}\n")
        f_out.write("==========================================\n\n")
    
    hdr_dom = "DOMINIO" if lang == "es" else "DOMAIN"
    hdr_est = "ESTADO" if lang == "es" else "STATUS"
    hdr_det = "MÉTODO/DETALLE" if lang == "es" else "METHOD/DETAIL"
    print(f"\n{NEGRITA}{BLANCO}{hdr_dom:<35} {hdr_est:<15} {hdr_det:<30}{FIN}")
    print("-" * 80)
    
    inicio_tiempo = time.time()
    
    for idx, dom in enumerate(dominios, 1):
        # Efecto de carga
        loader_txt = t["scanning_item"].format(dom=dom)
        sys.stdout.write(f"\r[{idx}/{total}] {loader_txt}")
        sys.stdout.flush()
        
        reintentos = 2 if not dns_only else 1
        estado, detalle, info = "desconocido", "Error", {}
        
        for r in range(reintentos):
            estado, detalle, info = chequear_dominio(dom, dns_only=dns_only, lang=lang, realizar_auditoria=realizar_auditoria)
            if estado != "desconocido" or dns_only:
                break
            if r < reintentos - 1:
                time.sleep(2.0)
        
        sys.stdout.write("\r" + " " * 80 + "\r")
        
        # Formato de visualización
        if estado == "disponible":
            status_text = f"{VERDE}{t['gen_avail'].replace('✔ ', '')}{FIN}"
            disponibles.append(dom)
            metodo_text = t["libre_dns"] if dns_only else t["libre_whois"]
            if guardar_archivo:
                f_out.write(f"[✔] FREE: {dom:<35} | {metodo_text}\n")
        elif estado == "comprado":
            status_text = f"{ROJO}{t['gen_taken'].replace('❌ ', '').upper()}{FIN}"
            comprados.append(dom)
            
            # Formatear el detalle / método con indicación de Cloudflare si aplica
            metodo_text = info.get("metodo", "DNS")
            cf_val = info.get("cloudflare", "none")
            if realizar_auditoria and cf_val != "none":
                if cf_val == "orange":
                    metodo_text += f" {AMARILLO}(☁ Orange){FIN}"
                elif cf_val == "gray":
                    metodo_text += f" {GRIS}(☁ Gray){FIN}"
            
            if guardar_archivo:
                cf_str = f" | Cloudflare: {cf_val.upper()}" if (realizar_auditoria and cf_val != "none") else ""
                ssl_str = " | SSL: YES" if (realizar_auditoria and info.get("ssl_active")) else " | SSL: NO"
                f_out.write(f"[❌] TAKEN: {dom:<32} | {detalle} | IP: {info.get('ip')}{cf_str}{ssl_str}\n")
        else:
            status_text = f"{AMARILLO}{t['gen_unk'].replace('? ', '').upper()}{FIN}"
            desconocidos.append(dom)
            metodo_text = detalle
            if guardar_archivo:
                f_out.write(f"[?] UNKNOWN: {dom:<32} | {detalle}\n")
                
        print(f"{dom:<35} {status_text:<25} {metodo_text:<30}")
        
        if idx < total:
            time.sleep(retraso if not dns_only else 0.05)
            
    fin_tiempo = time.time()
    duracion = fin_tiempo - inicio_tiempo
    
    if guardar_archivo:
        f_out.write("\n==========================================\n")
        f_out.write(f"Resumen / Summary:\n")
        f_out.write(f" • Free: {len(disponibles)}\n")
        f_out.write(f" • Taken: {len(comprados)}\n")
        f_out.write(f" • Unknown: {len(desconocidos)}\n")
        f_out.write(f" Total time: {duracion:.2f}s\n")
        f_out.close()
        print(f"\n{VERDE}{t['scan_finished_saved'].format(duracion=duracion, archivo=guardar_archivo)}{FIN}")
    else:
        print(f"\n{VERDE}{t['scan_finished'].format(duracion=duracion)}{FIN}")
        
    print(t["summary_label"].format(disponibles=len(disponibles), comprados=len(comprados), desconocidos=len(desconocidos)))
    input(f"\n{GRIS}{t['enter_main_menu']}{FIN}")

def generador_dominios():
    lang = CONFIG["lang"]
    t = TEXTS[lang]
    
    limpiar_pantalla()
    mostrar_banner()
    print(f"\n{NEGRITA}{CIAN}{t['gen_title']}{FIN}")
    print(f"{t['gen_instr']}")
    print(f"{CIAN}╚════════════════════════════════════════════════════════════╝{FIN}\n")
    
    palabra = input(f"{BLANCO}{t['gen_prompt']}{FIN}").strip().lower()
    if not palabra:
        print(f"{ROJO}{t['gen_empty']}{FIN}")
        input(f"\n{GRIS}{t['enter_prev_menu']}{FIN}")
        return
        
    print(f"\n{AMARILLO}{t['gen_tld_prompt']}{FIN}")
    print(f"Ej: com, net, org, co, io, es, mx")
    tlds_input = input(f"{BLANCO}{t['gen_tlds_default']}{FIN}").strip().lower()
    
    if not tlds_input:
        tlds = ["com", "net", "co"]
    else:
        tlds = [t.strip().replace('.', '') for t in tlds_input.split(',')]
        
    print(f"\n{AMARILLO}{t['gen_style_title']}{FIN}")
    print(t["gen_style_1"].format(palabra=palabra))
    print(t["gen_style_2"].format(palabra=palabra))
    print(t["gen_style_3"].format(palabra=palabra))
    print(t["gen_style_4"].format(palabra=palabra))
    
    estilo = input(f"{BLANCO}{t['gen_select_style']}{FIN}").strip()
    
    sufijos = ["hub", "app", "lab", "net", "tech", "web", "site", "online", "box", "soft", "dev", "ly", "fy"]
    prefijos = ["go", "get", "my", "the", "super", "neo", "mega", "pro", "easy", "cyber", "smart", "quick"]
    
    ideas = []
    if estilo == "1":
        for suf in sufijos[:6]:
            for tld in tlds:
                ideas.append(f"{palabra}{suf}.{tld}")
    elif estilo == "2":
        for pref in prefijos[:6]:
            for tld in tlds:
                ideas.append(f"{pref}{palabra}.{tld}")
    elif estilo == "3":
        for tld in tlds:
            ideas.append(f"{palabra}.{tld}")
    elif estilo == "4":
        for tld in tlds:
            ideas.append(f"{palabra}ai.{tld}")
            ideas.append(f"my{palabra}ai.{tld}")
    else:
        for tld in tlds:
            ideas.append(f"{palabra}.{tld}")
            
    print(f"\n{VERDE}{t['gen_ready'].format(total=len(ideas))}{FIN}")
    confirmar = input(f"{t['gen_start_check']}{FIN}").lower()
    
    if confirmar not in ['s', 'y']:
        return
        
    print(f"\n{NEGRITA}{BLANCO}{t['gen_header_dom']:<35} {t['gen_header_status']:<15}{FIN}")
    print("-" * 60)
    
    libres = 0
    for dom in ideas:
        sys.stdout.write(f"\rComprobando / Checking {dom}...")
        sys.stdout.flush()
        
        estado, detalle, _ = chequear_dominio(dom, lang=lang)
        sys.stdout.write("\r" + " " * 50 + "\r")
        
        if estado == "disponible":
            print(f"{dom:<35} {VERDE}{t['gen_avail']}{FIN}")
            libres += 1
        elif estado == "comprado":
            print(f"{dom:<35} {ROJO}{t['gen_taken']}{FIN}")
        else:
            print(f"{dom:<35} {AMARILLO}{t['gen_unk']}{FIN}")
            
        time.sleep(0.5)
        
    print(f"\n{VERDE}{t['gen_summary'].format(libres=libres)}{FIN}")
    input(f"\n{GRIS}{t['enter_main_menu']}{FIN}")

def mostrar_manual():
    lang = CONFIG["lang"]
    t = TEXTS[lang]
    limpiar_pantalla()
    mostrar_banner()
    
    body = t["help_body"].format(
        NEGRITA=NEGRITA, CIAN=CIAN, FIN=FIN, 
        AMARILLO=AMARILLO, CURSIVA=CURSIVA, BLANCO=BLANCO
    )
    print(f"\n{NEGRITA}{CIAN}{t['help_title']}{FIN}")
    print(body)
    input(f"{GRIS}{t['enter_main_menu']}{FIN}")

def cambiar_idioma():
    limpiar_pantalla()
    mostrar_banner()
    print(f"\n{NEGRITA}{CIAN}╔══[ SELECCIÓN DE IDIOMA / LANGUAGE SELECTION ]═════════════╗{FIN}")
    print(f"║ Idioma actual / Current Language: {VERDE}{'Español' if CONFIG['lang'] == 'es' else 'English'}{FIN}       ║")
    print(f"║                                                           ║")
    print(f"║ {CIAN}[1]{FIN} Español (Spanish)                                      ║")
    print(f"║ {CIAN}[2]{FIN} English (Official English)                              ║")
    print(f"{CIAN}╚═══════════════════════════════════════════════════════════╝{FIN}\n")
    
    op = input("👉 Selecciona tu idioma / Select your language (1-2): ").strip()
    if op == "1":
        CONFIG["lang"] = "es"
        guardar_configuracion()
        print(f"\n{VERDE}✔ Idioma cambiado a Español.{FIN}")
    elif op == "2":
        CONFIG["lang"] = "en"
        guardar_configuracion()
        print(f"\n{VERDE}✔ Language changed to English.{FIN}")
    else:
        print(f"\n{ROJO}❌ Opción inválida / Invalid option.{FIN}")
    time.sleep(1)

def menu_principal():
    while True:
        lang = CONFIG["lang"]
        t = TEXTS[lang]
        
        limpiar_pantalla()
        mostrar_banner()
        print(f"\n{NEGRITA}{BLANCO}{t['menu_titulo']}{FIN}\n")
        print(f" {CIAN}[1]{FIN} {t['menu_opcion_1']}")
        print(f" {CIAN}[2]{FIN} {t['menu_opcion_2']}")
        print(f" {CIAN}[3]{FIN} {t['menu_opcion_3']}")
        print(f" {CIAN}[4]{FIN} {t['menu_opcion_4']}")
        print(f" {CIAN}[5]{FIN} {t['menu_opcion_5']}")
        print(f" {CIAN}[6]{FIN} {t['menu_opcion_6']}")
        print()
        
        opcion = input(f"{BLANCO}{t['ingresar_opcion']}{FIN}").strip()
        
        if opcion == "1":
            consulta_individual()
        elif opcion == "2":
            consulta_lote()
        elif opcion == "3":
            generador_dominios()
        elif opcion == "4":
            mostrar_manual()
        elif opcion == "5":
            cambiar_idioma()
        elif opcion == "6":
            limpiar_pantalla()
            print(f"\n{VERDE}{t['salir_mensaje']}{FIN}\n")
            sys.exit(0)
        else:
            print(f"\n{ROJO}{t['opcion_incorrecta']}{FIN}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        cargar_configuracion()
        # Si no existía el archivo config, preguntamos el idioma la primera vez de manera rápida
        if not os.path.exists(CONFIG_FILE):
            limpiar_pantalla()
            mostrar_banner()
            print(f"\n{NEGRITA}{CIAN}╔══[ IDIOMA / LANGUAGE ]═════════════════════════════════════╗{FIN}")
            print(f"║ Elige tu idioma para continuar:                           ║")
            print(f"║ Choose your language to continue:                         ║")
            print(f"║                                                           ║")
            print(f"║ {CIAN}[1]{FIN} Español (Spanish)                                      ║")
            print(f"║ {CIAN}[2]{FIN} English (Official English)                              ║")
            print(f"{CIAN}╚════════════════════════════════════════════════════════════╝{FIN}\n")
            op = input("👉 Selecciona / Select (1-2): ").strip()
            if op == "2":
                CONFIG["lang"] = "en"
            else:
                CONFIG["lang"] = "es"
            guardar_configuracion()
            print(f"\n{VERDE}✔ Guardado / Saved!{FIN}")
            time.sleep(1.0)
        menu_principal()
    except KeyboardInterrupt:
        print(f"\n\n{ROJO}⚠ Script interrumpido por el usuario. ¡Adiós!{FIN}\n" if CONFIG["lang"] == "es" else f"\n\n{ROJO}⚠ Script interrupted by the user. Goodbye!{FIN}\n")
        sys.exit(0)
