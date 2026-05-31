#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import re
import time
import os
import sys
import json
import urllib.request
import urllib.parse

# Importar motor central de LiberDom
try:
    from liberdom import chequear_dominio
except ImportError:
    # Si por alguna razón se ejecuta fuera de la ruta, agregar el path local
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from liberdom import chequear_dominio

# Colores ANSI para Consola
VERDE = "\033[1;92m"
CIAN = "\033[1;96m"
AMARILLO = "\033[1;93m"
ROJO = "\033[1;91m"
GRIS = "\033[0;37m"
FIN = "\033[0m"

# ==========================================
# ARCHIVOS DE CONFIGURACIÓN Y PERSISTENCIA
# ==========================================
BOT_CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".telegram_bot_config.json")
USERS_LANG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".telegram_bot_users.json")

BOT_CONFIG = {"token": ""}
USERS_LANG = {}

def cargar_config():
    global BOT_CONFIG
    if os.path.exists(BOT_CONFIG_FILE):
        try:
            with open(BOT_CONFIG_FILE, "r", encoding="utf-8") as f:
                BOT_CONFIG = json.load(f)
        except Exception:
            pass

def guardar_config():
    try:
        with open(BOT_CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(BOT_CONFIG, f, indent=4)
    except Exception:
        pass

def cargar_usuarios():
    global USERS_LANG
    if os.path.exists(USERS_LANG_FILE):
        try:
            with open(USERS_LANG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Convertir llaves a string (JSON las guarda como str de todos modos)
                USERS_LANG = {str(k): v for k, v in data.items()}
        except Exception:
            pass

def guardar_usuarios():
    try:
        with open(USERS_LANG_FILE, "w", encoding="utf-8") as f:
            json.dump(USERS_LANG, f, indent=4)
    except Exception:
        pass

# ==========================================
# TEXTOS DEL BOT DE TELEGRAM (ENGLISH ONLY)
# ==========================================
BOT_TEXTS = {
    "welcome": (
        "🔍 <b>Welcome to LiberDom Bot!</b>\n\n"
        "I am the autonomous, ultra-fast hybrid domain availability detector, optimized to help you find free domains without limits or premium third-party APIs.\n\n"
        "🌐 <b>How to use me?</b>\n"
        "• Send any domain directly (e.g. <code>myweb.com</code>).\n"
        "• Or use /check command followed by your domain (e.g. <code>/check myweb.com</code>).\n"
        "• For detailed help, type /help."
    ),
    "help": (
        "📚 <b>Help Guide - LiberDom Bot</b>\n\n"
        "Available commands:\n"
        "• /start - Start message.\n"
        "• /help - Shows this instruction manual.\n"
        "• /check &lt;domain&gt; - Technical availability check.\n\n"
        "💡 <b>Tip:</b> You can send me any domain in plain text directly in private chats! I will clean and parse it, then check it in milliseconds."
    ),
    "checking": "⏳ Querying global databases for <code>{domain}</code>...",
    "invalid": "❌ <b>Invalid format.</b> Enter a correct domain format (e.g. <code>myweb.com</code>).",
    "card_avail": "Congratulations! This domain is free to register.",
    "card_taken": "Domain already registered and taken on the internet.",
    "card_unk": "Could not determine with certainty (WHOIS rate limit / TLD not supported).",
    "card_tech": "Technical Details",
    "card_ip": "Server IP",
    "card_registrar": "Registrar",
    "card_created": "Created",
    "card_method": "Method",
    "card_footer": "Verified with LiberDom | GitHub: github.com/NeoTurcios/liberdom"
}

# ==========================================
# API DE TELEGRAM SIN DEPENDENCIAS (NATIVA)
# ==========================================
class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{self.token}/"
        self.id = None
        self.username = ""
        self.startup_time = None

    def get_me(self):
        return self._request("getMe")

    def _request(self, method, payload=None):
        url = self.base_url + method
        headers = {"Content-Type": "application/json"}
        
        data = None
        if payload:
            data = json.dumps(payload).encode("utf-8")
            
        try:
            req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
            with urllib.request.urlopen(req, timeout=10) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as e:
            return {"ok": False, "description": str(e)}

    def get_updates(self, offset=None):
        payload = {}
        if offset:
            payload["offset"] = offset
        payload["timeout"] = 5  # Polling corto
        return self._request("getUpdates", payload)

    def send_message(self, chat_id, text, reply_markup=None):
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True
        }
        if reply_markup:
            payload["reply_markup"] = reply_markup
        return self._request("sendMessage", payload)

    def edit_message_text(self, chat_id, message_id, text, reply_markup=None):
        payload = {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True
        }
        if reply_markup:
            payload["reply_markup"] = reply_markup
        return self._request("editMessageText", payload)

    def answer_callback_query(self, callback_query_id, text=None):
        payload = {"callback_query_id": callback_query_id}
        if text:
            payload["text"] = text
        return self._request("answerCallbackQuery", payload)

# ==========================================
# LÓGICA DE PROCESAMIENTO
# ==========================================
def formatear_tarjeta_html(domain, estado, detalle, info):
    t = BOT_TEXTS
    
    if estado == "disponible":
        icon = "🟢"
        status_label = "FREE"
        desc = t["card_avail"]
    elif estado == "comprado":
        icon = "🔴"
        status_label = "TAKEN"
        desc = t["card_taken"]
    else:
        icon = "🟡"
        status_label = "UNKNOWN"
        desc = t["card_unk"]

    msg = f"{icon} <b>{domain.upper()}</b> | <b>{status_label}</b>\n\n"
    msg += f"<i>{desc}</i>\n\n"
    msg += f"⚙ <b>{t['card_tech']}:</b>\n"
    msg += f"• {t['card_tech']}: <code>{detalle}</code>\n"
    if info.get("ip"):
        msg += f"• {t['card_ip']}: <code>{info['ip']}</code>\n"
    if info.get("registrador"):
        msg += f"• {t['card_registrar']}: <code>{info['registrador']}</code>\n"
    if info.get("fecha_creacion"):
        msg += f"• {t['card_created']}: <code>{info['fecha_creacion']}</code>\n"
    msg += f"• {t['card_method']}: <code>{info['metodo']}</code>\n\n"
    msg += f"🔎 <i>{t['card_footer']}</i>"
    return msg

def procesar_mensaje(bot, msg):
    chat_id = msg["chat"]["id"]
    chat_type = msg["chat"]["type"]
    user = msg.get("from", {}).get("username", "unknown")
    text = msg.get("text", "").strip()
    msg_date = msg.get("date", 0)
    
    print(f"{CIAN}[Recibido] Chat: {chat_type} ({chat_id}) | Usuario: @{user} | Mensaje: {text} | Fecha: {msg_date} | Startup: {bot.startup_time}{FIN}")
    
    # Ignorar mensajes antiguos (anteriores a la inicialización del bot)
    if bot.startup_time and msg_date < bot.startup_time:
        print(f"{ROJO}[Ignorado] Mensaje antiguo descartado.{FIN}")
        return

    # Detectar cuando el bot es añadido a un grupo/supergrupo
    new_members = msg.get("new_chat_members", [])
    if new_members:
        for member in new_members:
            if bot.id and member.get("id") == bot.id:
                welcome_group = (
                    f"👋 <b>Hello everyone! Thanks for adding me to the group.</b>\n\n"
                    f"I am <b>LiberDom Bot</b>, the ultra-fast hybrid domain availability detector. 🌐\n\n"
                    f"👥 <b>How to use me in this group?</b>\n"
                    f"• Use the <code>/check &lt;domain&gt;</code> command to check availability in milliseconds (e.g. <code>/check myweb.com</code>).\n"
                    f"• Use /help to see the user guide.\n\n"
                    f"⚡ <i>Optimized, autonomous, and without limits!</i>"
                )
                bot.send_message(chat_id, welcome_group)
                return

    text = msg.get("text", "").strip()
    if not text:
        return

    is_group = msg["chat"]["type"] in ["group", "supergroup"]

    # Limpiar y normalizar comando (ej: /check@LiberDomBot -> /check)
    if text.startswith("/"):
        partes = text.split(maxsplit=1)
        cmd_part = partes[0]
        args_part = partes[1] if len(partes) > 1 else ""
        
        if "@" in cmd_part:
            cmd_name, bot_user = cmd_part.split("@", 1)
            if bot.username and bot_user.lower() != bot.username.lower():
                return  # Para otro bot
            cmd_part = cmd_name
        
        text_normalized = cmd_part + (" " + args_part if args_part else "")
    else:
        text_normalized = text

    t = BOT_TEXTS

    # Comando /start
    if text_normalized.startswith("/start"):
        bot.send_message(chat_id, t["welcome"])
        return

    # Comando /help
    if text_normalized.startswith("/help"):
        bot.send_message(chat_id, t["help"])
        return

    # Comando /check o parsear dominios en texto plano
    dominio = ""
    if text_normalized.startswith("/check"):
        partes = text_normalized.split(maxsplit=1)
        if len(partes) > 1:
            dominio = partes[1].strip()
    elif not is_group:
        # En grupos NO permitimos detectar dominios en texto plano para evitar spam/falsos positivos "a lo loco"
        # Detectar si el texto parece un dominio
        clean_text = text_normalized.lower().replace("https://", "").replace("http://", "").replace("www.", "")
        clean_text = clean_text.split("/")[0]
        if "." in clean_text and len(clean_text) >= 4 and not " " in clean_text:
            dominio = clean_text

    if dominio:
        # Quitar subdominios y protocolos por seguridad de motor
        dom = dominio.lower()
        dom = re.sub(r'^(https?://)?(www\.)?', '', dom)
        dom = dom.split('/')[0]

        if not '.' in dom or len(dom) < 4:
            bot.send_message(chat_id, t["invalid"])
            return

        # Enviar cargando
        loading_msg = bot.send_message(chat_id, t["checking"].format(domain=dom))
        
        # Consultar motor híbrido local (usamos lang='en')
        estado, detalle, info = chequear_dominio(dom, dns_only=False, lang='en')
        
        # Formatear y actualizar mensaje
        card_html = formatear_tarjeta_html(dom, estado, detalle, info)
        bot.edit_message_text(chat_id, loading_msg["result"]["message_id"], card_html)
    else:
        # Si envían texto plano que no es comando ni dominio en chat privado, responder breve guía
        # En grupos ignoramos por completo
        if not is_group:
            if text_normalized.startswith("/"):
                bot.send_message(chat_id, t["invalid"])

def procesar_callback(bot, cb):
    # Función vacía para compatibilidad de callbacks antiguos
    pass

# ==========================================
# BUCLE DE POLLING PRINCIPAL
# ==========================================
def main():
    limpiar_pantalla = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    limpiar_pantalla()
    
    print(f"{CIAN}╔═══════════════════════════════════════════════════════════════╗")
    print(f"║      {VERDE}🤖  LiberDom Telegram Bot Engine (Zero-Dependency)  🤖{CIAN}   ║")
    print(f"╚═══════════════════════════════════════════════════════════════╝{FIN}\n")
    
    cargar_config()
    cargar_usuarios()
    
    if not BOT_CONFIG.get("token"):
        print(f"{AMARILLO}💡 ¡Primer inicio! Por favor, ingresa las credenciales de tu Bot de Telegram.{FIN}")
        print(f"Puedes crear un bot hablando con {VERDE}@BotFather{FIN} en Telegram y copiando el Token API.\n")
        
        token = input(f"{CIAN}👉 Ingresa el Bot Token: {FIN}").strip()
        if not token:
            print(f"\n{ROJO}❌ Token vacío. Saliendo...{FIN}\n")
            sys.exit(1)
            
        BOT_CONFIG["token"] = token
        guardar_config()
        print(f"\n{VERDE}✔ Token guardado de forma persistente.{FIN}\n")

    token = BOT_CONFIG["token"]
    bot = TelegramBot(token)
    
    print(f"{AMARILLO}⏳ Conectando con los servidores de Telegram Bot API...{FIN}")
    bot_info = bot.get_me()
    if not bot_info.get("ok"):
        print(f"\n{ROJO}❌ Error al conectar: {bot_info.get('description')}{FIN}")
        print(f"{AMARILLO}Asegúrate de que el Token sea válido y de tener conexión a Internet.{FIN}\n")
        
        reconfig = input("¿Deseas restablecer el token ahora? (s/n): ").strip().lower()
        if reconfig in ['s', 'y']:
            BOT_CONFIG["token"] = ""
            guardar_config()
            print(f"{VERDE}Token restablecido. Ejecuta de nuevo para ingresar uno nuevo.{FIN}")
        sys.exit(1)
        
    bot.id = bot_info["result"]["id"]
    bot.username = bot_info["result"]["username"]
    bot.startup_time = int(time.time())
    
    print(f"{VERDE}✔ Conexión establecida con éxito.{FIN}")
    print(f"{VERDE}✔ Conectado como @{bot.username} (ID: {bot.id}){FIN}")
    print(f"{CIAN}👉 El bot está encendido y escuchando mensajes en tiempo real...{FIN}")
    print(f"{GRIS}Presiona Ctrl+C en cualquier momento para apagar el motor.{FIN}\n")
    
    offset = None
    
    while True:
        try:
            updates = bot.get_updates(offset)
            if updates.get("ok") and updates.get("result"):
                for update in updates["result"]:
                    offset = update["update_id"] + 1
                    
                    if "message" in update:
                        procesar_mensaje(bot, update["message"])
                    elif "callback_query" in update:
                        procesar_callback(bot, update["callback_query"])
                        
            time.sleep(0.8)  # Pequeña pausa para no saturar CPU ni rate limits
        except KeyboardInterrupt:
            print(f"\n{ROJO}⚠ Motor del Bot apagado correctamente. ¡Hasta luego!{FIN}\n")
            sys.exit(0)
        except Exception as e:
            print(f"{ROJO}⚠ Error en bucle: {e}{FIN}")
            time.sleep(3)

if __name__ == "__main__":
    main()
