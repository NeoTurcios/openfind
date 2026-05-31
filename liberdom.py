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

# Limpiar pantalla según el sistema operativo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Banner estilizado
def mostrar_banner():
    banner = f"""
{CIAN}╔═══════════════════════════════════════════════════════════════╗
║  {VERDE}██╗     ██╗██████╗ ███████╗██████╗ ██████╗  ██████╗ ███╗   ███╗{CIAN}  ║
║  {VERDE}██║     ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗████╗ ████║{CIAN}  ║
║  {VERDE}██║     ██║██████╔╝█████╗  ██████╔╝██║  ██║██║   ██║██╔████╔██║{CIAN}  ║
║  {VERDE}██║     ██║██╔══██╗██╔══╝  ██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║{CIAN}  ║
║  {VERDE}███████╗██║██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║ ╚═╝ ██║{CIAN}  ║
║  {VERDE}╚══════╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝{CIAN}  ║
╠═══════════════════════════════════════════════════════════════╣
║         {BLANCO}🔍    LiberDom - Detector de Dominios Libre    🔍         {CIAN}║
║                     {AMARILLO}¡Optimizado para Termux!                  {CIAN}║
╚═══════════════════════════════════════════════════════════════╝{FIN}"""
    print(banner)

# ==========================================
# MOTOR DE BÚSQUEDA Y DETECCION WHOIS/DNS
# ==========================================

def registrar_whois_servidor(domain, server=None):
    """Realiza una consulta WHOIS pura usando sockets TCP en el puerto 43"""
    if not server:
        tld = domain.split('.')[-1].lower()
        # Servidores WHOIS comunes para agilizar
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
        s.settimeout(6.0)
        s.connect((server, 43))
        
        # Ajustes de formato de consulta para servidores especiales
        if server == 'whois.verisign-grs.com':
            query = f"domain {domain}\r\n"
        elif server == 'whois.denic.de':
            query = f"-T dn {domain}\r\n"
        elif server == 'whois.nic.es':
            # .es suele requerir configuración adicional o no da WHOIS público fácil por socket.
            query = f"{domain}\r\n"
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

def chequear_dominio(domain, dns_only=False):
    """
    Determina si un dominio está libre (disponible) o comprado (registrado).
    Retorna: (estado, detalle_espanol, info_adicional)
    """
    domain = domain.strip().lower()
    
    # Validar formato básico de dominio
    if not '.' in domain or len(domain) < 4:
        return "invalido", "Formato inválido (Ej: misitio.com)", {}

    # Quitar protocolos si el usuario los ingresó por error
    domain = re.sub(r'^(https?://)?(www\.)?', '', domain)
    # Quitar rutas extras
    domain = domain.split('/')[0]

    info = {
        "dominio": domain,
        "metodo": "Ninguno",
        "ip": None,
        "whois_server": None,
        "fecha_creacion": None,
        "registrador": None
    }

    # ----------------------------------------------------
    # MÈTODO 1: DNS Lookup (Súper Rápido)
    # ----------------------------------------------------
    try:
        ip = socket.gethostbyname(domain)
        info["ip"] = ip
        info["metodo"] = "Resolución DNS"
        return "comprado", "COMPRADO / REGISTRADO (Activo por DNS)", info
    except socket.gaierror:
        # Si falla DNS, puede que esté libre o comprado pero inactivo (sin hosting)
        if dns_only:
            # En modo DNS-only asumimos disponible (sin registros activos de DNS)
            info["metodo"] = "Verificación DNS Rápida"
            return "disponible", "DISPONIBLE (Por DNS - Sin registros activos)", info
        pass

    # ----------------------------------------------------
    # MÈTODO 2: Consulta WHOIS (100% Preciso)
    # ----------------------------------------------------
    res = registrar_whois_servidor(domain)
    
    if res.startswith("ERROR:"):
        # Si falla WHOIS básico, intentamos verificar si al menos responde a ping DNS general (Name Servers)
        # Algunos servidores cortan la conexión por spam o bloqueos de red
        return "desconocido", f"Error de red/servidor WHOIS ({res[6:]})", info

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
            return "desconocido", f"Error al redirigir WHOIS a {refer_server}", info

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

    info["metodo"] = "Consulta WHOIS Socket 43"

    if esta_disponible:
        return "disponible", "¡DISPONIBLE! (No está registrado)", info
    
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
        return "comprado", "COMPRADO / REGISTRADO (Confirmado por WHOIS)", info
    else:
        return "desconocido", "No se pudo determinar con certeza (Límite WHOIS / TLD no soportado)", info

# ==========================================
# INTERFAZ DE USUARIO E INTERACCIÓN
# ==========================================

def mostrar_animacion_carga():
    """Muestra un spinner elegante mientras se realiza la consulta"""
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for i in range(8):
        for char in spinner:
            sys.stdout.write(f"\r{CIAN}[{char}] {AMARILLO}Consultando base de datos mundial de dominios...{FIN}")
            sys.stdout.flush()
            time.sleep(0.02)
    sys.stdout.write("\r" + " " * 65 + "\r")
    sys.stdout.flush()

def consulta_individual():
    limpiar_pantalla()
    mostrar_banner()
    print(f"\n{NEGRITA}{CIAN}╔══[ OPCIÓN 1: BÚSQUEDA INDIVIDUAL ]═════════════════════════╗{FIN}")
    print(f"║ Escribe el dominio completo que deseas buscar.            ║")
    print(f"║ Ejemplos: {VERDE}midominio.com{FIN}, {VERDE}proyecto.net{FIN}, {VERDE}app.co{FIN}, {VERDE}web.es{FIN}       ║")
    print(f"{CIAN}╚════════════════════════════════════════════════════════════╝{FIN}\n")
    
    dominio = input(f"{BLANCO}👉 Ingresa el dominio: {FIN}").strip()
    if not dominio:
        print(f"\n{ROJO}❌ No ingresaste ningún dominio.{FIN}")
        input(f"\n{GRIS}Presiona ENTER para volver al menú anterior...{FIN}")
        return

    print()
    mostrar_animacion_carga()
    
    estado, detalle, info = chequear_dominio(dominio)
    
    print(f"{CIAN}📊 RESULTADOS PARA:{FIN} {NEGRITA}{BLANCO}{dominio.upper()}{FIN}\n")
    
    if estado == "disponible":
        print(f"  {VERDE}███████████████████████████████████████████████")
        print(f"  ██ [✔] {detalle.upper()} ██")
        print(f"  ███████████████████████████████████████████████{FIN}\n")
        print(f"  {NEGRITA}{VERDE}¡Felicidades! Este dominio está libre. Puedes registrarlo.{FIN}")
    elif estado == "comprado":
        print(f"  {ROJO}███████████████████████████████████████████████")
        print(f"  ██ [❌] {detalle.upper()} ██")
        print(f"  ███████████████████████████████████████████████{FIN}\n")
        print(f"  {AMARILLO}Información del registro:{FIN}")
        if info["ip"]:
            print(f"  {BLANCO}• IP de Servidor:{FIN} {CIAN}{info['ip']}{FIN}")
        if info["registrador"]:
            print(f"  {BLANCO}• Registrado con:{FIN} {CIAN}{info['registrador']}{FIN}")
        if info["fecha_creacion"]:
            print(f"  {BLANCO}• Fecha Creación:{FIN} {CIAN}{info['fecha_creacion']}{FIN}")
        print(f"  {BLANCO}• Método de detección:{FIN} {GRIS}{info['metodo']}{FIN}")
    elif estado == "invalido":
        print(f"  {ROJO}❌ {detalle}{FIN}")
    else:
        print(f"  {AMARILLO}⚠ {detalle}{FIN}")
        print(f"  {GRIS}Intenta buscarlo directamente en tu navegador web o proveedor DNS.{FIN}")
        
    print()
    input(f"{GRIS}Presiona ENTER para regresar al menú principal...{FIN}")

def consulta_lote():
    limpiar_pantalla()
    mostrar_banner()
    print(f"\n{NEGRITA}{CIAN}╔══[ OPCIÓN 2: BÚSQUEDA EN LOTE / MASIVA ]═══════════════════╗{FIN}")
    print(f"║ Comprueba listas grandes de dominios con alta velocidad.   ║")
    print(f"║ Puedes usar un archivo .txt o pegar texto directamente.    ║")
    print(f"{CIAN}╚════════════════════════════════════════════════════════════╝{FIN}\n")
    
    print(f"{NEGRITA}{BLANCO}¿Cómo deseas ingresar los dominios?{FIN}")
    print(f" {CIAN}[1]{FIN} Cargar desde un archivo de texto (.txt)")
    print(f" {CIAN}[2]{FIN} Pegar lista de dominios directamente en la consola")
    print()
    
    opcion_ingreso = input(f"{BLANCO}👉 Selecciona una opción (1-2): {FIN}").strip()
    
    lineas = []
    
    if opcion_ingreso == "1":
        # Cargar desde archivo
        ruta_archivo = input(f"\n{BLANCO}👉 Escribe el nombre o ruta del archivo (Ej: dominios.txt): {FIN}").strip()
        
        if not os.path.exists(ruta_archivo):
            crear_demo = input(f"\n{AMARILLO}⚠ El archivo '{ruta_archivo}' no existe. ¿Quieres crear un archivo demo con ejemplos? (s/n): {FIN}").lower()
            if crear_demo == 's':
                ejemplos = [
                    "google.com\n", "midominioquenoexiste12345.com\n", "github.com\n", 
                    "termux-espanol-libre.net\n", "facebook.com\n", "www.youtube.com\n",
                    "http://ejemplolibre999.org\n", "mi-empresa-ideal.co\n"
                ]
                with open(ruta_archivo, "w") as f:
                    f.writelines(ejemplos)
                print(f"{VERDE}✔ Archivo '{ruta_archivo}' creado con 8 dominios de ejemplo.{FIN}")
            else:
                return

        try:
            with open(ruta_archivo, "r") as f:
                lineas = f.readlines()
        except Exception as e:
            print(f"{ROJO}❌ Error al leer el archivo: {e}{FIN}")
            input(f"\n{GRIS}Presiona ENTER para continuar...{FIN}")
            return
            
    elif opcion_ingreso == "2":
        # Pegar texto directamente
        print(f"\n{AMARILLO}👉 Pega tus dominios a continuación.{FIN}")
        print(f"{BLANCO}Puedes separarlos por comas, espacios o saltos de línea.{FIN}")
        print(f"{GRIS}Cuando termines, escribe {NEGRITA}{BLANCO}FIN{FIN}{GRIS} en una línea sola y presiona ENTER:{FIN}\n")
        
        lineas_pegadas = []
        while True:
            try:
                linea = input().strip()
                if linea.upper() == 'FIN':
                    break
                # También permitimos terminar con una línea vacía si ya pegaron algo y dan enter adicional
                if linea == '' and len(lineas_pegadas) > 0:
                    break
                if linea == '' and len(lineas_pegadas) == 0:
                    print(f"{ROJO}Escribe tus dominios o 'FIN' para salir.{FIN}")
                    continue
                lineas_pegadas.append(linea)
            except (KeyboardInterrupt, EOFError):
                break
        
        # Guardar en la estructura de lineas
        lineas = lineas_pegadas
        
    else:
        print(f"\n{ROJO}❌ Opción inválida.{FIN}")
        time.sleep(1)
        return

    # Limpiar y normalizar dominios (soporta múltiples separadores por línea en caso de copiado con comas/espacios)
    dominios_crudos = []
    for line in lineas:
        line_clean = line.strip()
        # Ignorar comentarios si es un archivo o texto
        if not line_clean or line_clean.startswith('#'):
            continue
            
        # Separar por comas, espacios o tabuladores para soportar formatos pegados continuos
        partes = re.split(r'[,\s]+', line_clean)
        for part in partes:
            dom = part.strip().lower()
            # Limpiar protocolos y www
            dom = re.sub(r'^(https?://)?(www\.)?', '', dom)
            dom = dom.split('/')[0]
            if '.' in dom and len(dom) >= 4:
                dominios_crudos.append(dom)

    total_cargados = len(dominios_crudos)
    # Eliminar duplicados manteniendo el orden
    dominios = list(dict.fromkeys(dominios_crudos))
    total = len(dominios)
    duplicados = total_cargados - total

    if total == 0:
        print(f"{ROJO}❌ No se encontraron dominios válidos para analizar.{FIN}")
        input(f"\n{GRIS}Presiona ENTER para volver al menú anterior...{FIN}")
        return

    print(f"\n{VERDE}✔ Se procesarán {total} dominios únicos.{FIN}")
    if duplicados > 0:
        print(f"{AMARILLO}💡 Se omitieron {duplicados} dominios duplicados/inválidos.{FIN}")

    # Menú de selección de modo de escaneo
    print(f"\n{NEGRITA}{BLANCO}Selecciona el MODO DE ESCANEO para la lista:{FIN}")
    print(f" {CIAN}[1]{FIN} {NEGRITA}Modo Ultra-Rápido (Solo DNS):{FIN}")
    print(f"     Comprueba si el dominio resuelve IP. Inmediato, sin límites de velocidad.")
    print(f"     Recomendado para listas gigantes (más de 100 dominios).")
    print(f" {CIAN}[2]{FIN} {NEGRITA}Modo Híbrido Completo (DNS + WHOIS):{FIN}")
    print(f"     Comprobación oficial de registro en bases de datos mundiales.")
    print(f"     Recomendado para listas cortas/medianas para evitar bloqueos WHOIS.")
    
    modo = input(f"\n{BLANCO}👉 Selecciona modo (1 o 2): {FIN}").strip()
    dns_only = True if modo == "1" else False

    # Configuración de retraso (delay) para WHOIS si es modo completo
    retraso = 0.0
    if not dns_only:
        print(f"\n{AMARILLO}Para evitar que los servidores WHOIS bloqueen tu IP (Rate Limit), se aconseja un retraso:{FIN}")
        if total > 50:
            print(f"  • Sugerido para tu lista (>50 dominios): {VERDE}1.5 a 2.0 segundos{FIN}")
        elif total > 20:
            print(f"  • Sugerido para tu lista (>20 dominios): {VERDE}1.0 segundo{FIN}")
        else:
            print(f"  • Sugerido para tu lista: {VERDE}0.4 segundos{FIN}")
            
        retraso_input = input(f"{BLANCO}👉 Retraso en segundos entre búsquedas [Enter para el sugerido]: {FIN}").strip()
        if retraso_input == "":
            retraso = 1.5 if total > 50 else (1.0 if total > 20 else 0.4)
        else:
            try:
                retraso = float(retraso_input)
            except ValueError:
                retraso = 0.5

    guardar = input(f"\n{BLANCO}¿Quieres guardar los resultados en un archivo de texto? (s/n): {FIN}").strip().lower()
    guardar_archivo = "resultados_dominios.txt" if guardar == 's' else None
    
    disponibles = []
    comprados = []
    desconocidos = []
    
    if guardar_archivo:
        f_out = open(guardar_archivo, "w", encoding="utf-8")
        f_out.write("=== RESULTADOS DE BÚSQUEDA DE DOMINIOS ===\n")
        f_out.write(f"Fecha: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f_out.write(f"Modo: {'Solo DNS (Rápido)' if dns_only else 'Híbrido DNS+WHOIS'}\n")
        f_out.write(f"Total de dominios únicos analizados: {total}\n")
        f_out.write("==========================================\n\n")
    
    print(f"\n{NEGRITA}{BLANCO}{'DOMINIO':<35} {'ESTADO':<15} {'MÉTODO/DETALLE':<30}{FIN}")
    print("-" * 80)
    
    inicio_tiempo = time.time()
    
    for idx, dom in enumerate(dominios, 1):
        # Efecto de carga por línea
        sys.stdout.write(f"\r[{idx}/{total}] Escaneando {dom}...")
        sys.stdout.flush()
        
        # Intentar con reintento si es WHOIS y falla
        reintentos = 2 if not dns_only else 1
        estado, detalle, info = "desconocido", "Error", {}
        
        for r in range(reintentos):
            estado, detalle, info = chequear_dominio(dom, dns_only=dns_only)
            if estado != "desconocido" or dns_only:
                break
            # Si da error desconocido (WHOIS rate limit o red), esperar un poco y reintentar
            if r < reintentos - 1:
                time.sleep(2.0)
        
        # Borrar línea de carga actual
        sys.stdout.write("\r" + " " * 80 + "\r")
        
        # Formato de visualización
        if estado == "disponible":
            status_text = f"{VERDE}DISPONIBLE{FIN}"
            disponibles.append(dom)
            metodo_text = "Libre por DNS" if dns_only else "Libre (WHOIS)"
            if guardar_archivo:
                f_out.write(f"[✔] LIBRE: {dom:<35} | {metodo_text}\n")
        elif estado == "comprado":
            status_text = f"{ROJO}COMPRADO{FIN}"
            comprados.append(dom)
            metodo_text = info.get("metodo", "DNS")
            if guardar_archivo:
                f_out.write(f"[❌] COMPRADO: {dom:<32} | Detalle: {detalle} | IP: {info.get('ip')}\n")
        else:
            status_text = f"{AMARILLO}DESCONOCIDO{FIN}"
            desconocidos.append(dom)
            metodo_text = detalle
            if guardar_archivo:
                f_out.write(f"[?] INSEGURO: {dom:<32} | Razón: {detalle}\n")
                
        print(f"{dom:<35} {status_text:<25} {metodo_text:<30}")
        
        # Aplicar el retraso configurado
        if idx < total:
            time.sleep(retraso if not dns_only else 0.05)
            
    fin_tiempo = time.time()
    duracion = fin_tiempo - inicio_tiempo
    
    if guardar_archivo:
        f_out.write("\n==========================================\n")
        f_out.write(f"Resumen del Escaneo:\n")
        f_out.write(f" • Disponibles: {len(disponibles)}\n")
        f_out.write(f" • Comprados: {len(comprados)}\n")
        f_out.write(f" • Desconocidos: {len(desconocidos)}\n")
        f_out.write(f" Tiempo total de ejecución: {duracion:.2f} segundos\n")
        f_out.close()
        print(f"\n{VERDE}✔ ¡Escaneo finalizado en {duracion:.1f}s! Resultados guardados en: {NEGRITA}{guardar_archivo}{FIN}")
    else:
        print(f"\n{VERDE}✔ ¡Escaneo finalizado en {duracion:.1f}s!{FIN}")
        
    print(f"\n{CIAN}Resumen: {VERDE}{len(disponibles)} Disponibles{FIN} | {ROJO}{len(comprados)} Comprados{FIN} | {AMARILLO}{len(desconocidos)} Desconocidos{FIN}")
    input(f"\n{GRIS}Presiona ENTER para regresar al menú principal...{FIN}")

def generador_dominios():
    limpiar_pantalla()
    mostrar_banner()
    print(f"\n{NEGRITA}{CIAN}╔══[ OPCIÓN 3: GENERADOR E IDEAS DE DOMINIOS ]═══════════════╗{FIN}")
    print(f"║ Mezcla palabras clave con TLDs para encontrar ideas libres ║")
    print(f"{CIAN}╚════════════════════════════════════════════════════════════╝{FIN}\n")
    
    palabra = input(f"{BLANCO}👉 Escribe una palabra clave (Ej: tecno, app, net): {FIN}").strip().lower()
    if not palabra:
        print(f"{ROJO}❌ Entrada vacía.{FIN}")
        input(f"\n{GRIS}Presiona ENTER para continuar...{FIN}")
        return
        
    print(f"\n{AMARILLO}Elige las extensiones (TLDs) a combinar (Separadas por comas):{FIN}")
    print(f"Ejemplo: {CIAN}com, net, org, co, io, es, mx{FIN}")
    tlds_input = input(f"{BLANCO}👉 Extensiones [por defecto: com, net, co]: {FIN}").strip().lower()
    
    if not tlds_input:
        tlds = ["com", "net", "co"]
    else:
        tlds = [t.strip().replace('.', '') for t in tlds_input.split(',')]
        
    print(f"\n{AMARILLO}Elige el estilo de combinación:{FIN}")
    print(f"1. Palabra + sufijo (Ej: {palabra}hub, {palabra}app, {palabra}lab)")
    print(f"2. Prefijo + palabra (Ej: super{palabra}, go{palabra}, check{palabra})")
    print(f"3. Palabra exacta con múltiples TLDs (Ej: {palabra}.com, {palabra}.net)")
    estilo = input(f"{BLANCO}👉 Elige una opción (1-3): {FIN}").strip()
    
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
    else:
        for tld in tlds:
            ideas.append(f"{palabra}.{tld}")
            
    print(f"\n{VERDE}✔ Se generaron {len(ideas)} ideas de dominios para comprobar.{FIN}")
    confirmar = input(f"¿Quieres empezar a verificar cuáles están libres ahora mismo? (s/n): {FIN}").lower()
    
    if confirmar != 's':
        return
        
    print(f"\n{NEGRITA}{BLANCO}{'DOMINIO GENERADO':<35} {'ESTADO':<15}{FIN}")
    print("-" * 60)
    
    libres = 0
    for dom in ideas:
        sys.stdout.write(f"\rComprobando {dom}...")
        sys.stdout.flush()
        
        estado, detalle, _ = chequear_dominio(dom)
        sys.stdout.write("\r" + " " * 50 + "\r")
        
        if estado == "disponible":
            print(f"{dom:<35} {VERDE}✔ ¡DISPONIBLE!{FIN}")
            libres += 1
        elif estado == "comprado":
            print(f"{dom:<35} {ROJO}❌ Comprado{FIN}")
        else:
            print(f"{dom:<35} {AMARILLO}? Desconocido{FIN}")
            
        time.sleep(0.5)
        
    print(f"\n{VERDE}⭐ Fin del análisis. Encontraste {libres} dominios listos para comprar.{FIN}")
    input(f"\n{GRIS}Presiona ENTER para regresar al menú principal...{FIN}")

def mostrar_manual():
    limpiar_pantalla()
    mostrar_banner()
    manual = f"""
{NEGRITA}{CIAN}📘 CONSEJOS E INSTRUCCIONES DE USO (Termux) {FIN}

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

{NEGRITA}{AMARILLO}4. Licencia y Uso{FIN}
Este script es público y 100% de código abierto. ¡Puedes usarlo y editarlo 
para integrarlo en tus herramientas de automatización de hacking ético, 
desarrollo web o marketing!
"""
    print(manual)
    input(f"{GRIS}Presiona ENTER para volver al menú...{FIN}")

def menu_principal():
    while True:
        limpiar_pantalla()
        mostrar_banner()
        print(f"\n{NEGRITA}{BLANCO}💻  MENÚ PRINCIPAL EN ESPAÑOL  💻{FIN}\n")
        print(f" {CIAN}[1]{FIN} 🔍 Buscar un dominio individual")
        print(f" {CIAN}[2]{FIN} 📂 Buscar por lote (archivo txt)")
        print(f" {CIAN}[3]{FIN} 💡 Generador de nombres + Verificar disponibilidad")
        print(f" {CIAN}[4]{FIN} 📘 Guía de ayuda / Consejos")
        print(f" {CIAN}[5]{FIN} 👋 Salir del script")
        print()
        
        opcion = input(f"{BLANCO}👉 Selecciona una opción (1-5): {FIN}").strip()
        
        if opcion == "1":
            consulta_individual()
        elif opcion == "2":
            consulta_lote()
        elif opcion == "3":
            generador_dominios()
        elif opcion == "4":
            mostrar_manual()
        elif opcion == "5":
            limpiar_pantalla()
            print(f"\n{VERDE}👋 ¡Gracias por usar LiberDom! Diseñado para optimizar tus proyectos.{FIN}")
            print(f"{CIAN}¡Haz tu repositorio público y compártelo con el mundo! 🚀{FIN}\n")
            sys.exit(0)
        else:
            print(f"\n{ROJO}❌ Opción incorrecta. Inténtalo de nuevo.{FIN}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print(f"\n\n{ROJO}⚠ Script interrumpido por el usuario. ¡Adiós!{FIN}\n")
        sys.exit(0)
