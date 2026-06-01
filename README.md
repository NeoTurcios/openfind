<p align="center">
  <img src="web/static/logo.webp" alt="Logo OpenFind AI" width="130" height="130" style="border-radius: 26px; box-shadow: 0 10px 30px rgba(0, 230, 118, 0.25);">
</p>

<h1 align="center">🔎 OpenFind AI</h1>
<p align="center">
  <strong>El detector y buscador de dominios híbrido inteligente y ultrarrápido diseñado para Termux, la Web y Android.</strong>
</p>

<p align="center">
  <a href="https://termux.com/"><img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Android-00e676?style=flat-square&logo=android&logoColor=white" alt="Platform"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.7+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/Licencia-No_Comercial-8b5cf6?style=flat-square" alt="License"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/Idioma-Espa%C3%B1ol%20%F0%9F%87%AA%F0%9F%87%B8-ff1744?style=flat-square" alt="Language"></a>
</p>

---

> [!TIP]
> **OpenFind AI** es una herramienta de código abierto para comprobar la disponibilidad de dominios en milisegundos. Combina consultas DNS ultrarrápidas, sockets TCP recursivos a nivel de red WHOIS (puerto 43), y un generador inteligente asistido por IA para ideas de marcas. **¡100% libre de APIs de pago o cuotas de terceros!**

---

## 🌟 Características Clave

*   ⚡ **Búsqueda Híbrida Inteligente:** Primero realiza una resolución DNS instantánea (sin límites ni costos). Si no detecta una IP activa, conmuta a un cliente WHOIS puro de bajo nivel (Sockets TCP) para comprobar si está libre.
*   📦 **Cero Dependencias en CLI:** Escrito en Python nativo puro. Ideal para Termux y servidores ligeros sin necesidad de instalar compiladores C o librerías pesadas.
*   🌍 **Conexión WHOIS Recursiva Mundial:** Consulta dinámicamente `whois.iana.org` y redirige de forma automática al servidor correspondiente para cualquier TLD global (`.com`, `.net`, `.io`) o regional (`.es`, `.mx`, `.cl`, etc.).
*   🎨 **Estética de Terminal Matrix:** Banner dinámico de inicio, colores ANSI vivos y spinner de carga diseñado para brillar en la terminal de Termux.
*   📂 **Búsqueda Masiva en Lote:** Carga listas de dominios desde un archivo `.txt` o pega texto libre directamente. El sistema limpia protocolos, subdominios y descarta duplicados de forma inteligente.
*   💡 **Generador Inteligente con IA:** Genera ideas creativas de dominios combinando palabras clave con prefijos, sufijos y opciones de inteligencia artificial (`ai`, `my...ai`) comprobando su disponibilidad en tiempo real.

---

## 📥 Instalación en Termux

Abre tu aplicación **Termux** y ejecuta esta única línea para clonar e instalar el alias rápido de forma totalmente automatizada:

```bash
pkg install git -y && git clone https://github.com/NeoTurcios/openfind.git && cd openfind && chmod +x install.sh && ./install.sh
```

Una vez completada la instalación, puedes abrir la herramienta desde cualquier directorio escribiendo:

```bash
openfind
```

*(O ejecutando directamente en la carpeta: `./openfind.py`)*

---

## 📱 Cliente Android Nativo (OpenFind AI - Premium)

¡OpenFind AI incluye una **aplicación nativa para teléfonos inteligentes** en la carpeta `/android/`!

*   🎯 **Compilada para Android 16 (SDK 36):** Soporta los últimos estándares de Google (con soporte retrospectivo desde SDK 26).
*   🚀 **Estructura Modernizada de Kotlin:** Desarrollada bajo arquitectura Kotlin moderna bajo el paquete limpio `openfind.ai`.
*   🌐 **Idioma Dinámico en la Barra Flotante:** Soporte multi-idioma (Español/Inglés) que traduce de manera dinámica toda la interfaz, incluyendo la barra de navegación flotante tipo isla.
*   📂 **Biblioteca Inteligente Limitada a 10 Elementos:** Mantiene la app rápida y limpia guardando solo los 10 dominios favoritos e historial más recientes de forma automatizada.
*   📊 **Exportación PDF Nativa:** Genera reportes técnicos y corporativos de disponibilidad y compártelos al instante.
*   🎨 **Diseño Oscuro Glassmorphism:** Interfaz interactiva de alta fidelidad con bordes neón que responden dinámicamente al estado del dominio analizado.

### Cómo compilar localmente:
1. Dirígete a la carpeta: `cd android`
2. Genera la compilación: `./gradlew assembleDebug`
3. APK resultante en: `app/build/outputs/apk/debug/app-debug.apk`

---

## 🌐 Versión Web Responsiva (Flask + Glassmorphism)

El panel web visual está ubicado en la carpeta `/web/`.

> [!NOTE]
> La versión web incluye **escaneo masivo en paralelo** con concurrencia controlada en JavaScript, tarjetas responsivas glassmorphism y descargas de reportes en PDF y TXT.

### Cómo encender la Web localmente:
1. Entra a la carpeta: `cd web`
2. Instala los requerimientos: `pip install -r requirements.txt`
3. Enciende el servidor Flask: `python app.py`
4. Navega a: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🤖 Bot de Telegram Autónomo

Activa el bot en segundos para buscar dominios de forma conversacional:
1. Inicia el bot: `python telegram_bot.py`
2. Pega tu Bot Token de [@BotFather](https://t.me/BotFather) en la consola cuando se solicite.
3. Envía cualquier dominio directamente en chat y obtén respuestas técnicas en milisegundos.

---

## ⚙️ ¿Cómo funciona bajo el capó?

```mermaid
%%{init: {"flowchart": {"htmlLabels": true}} }%%
flowchart LR
    A["Inicio: Dominio"] --> B["Paso 1: Resolución DNS"]
    B -->|Tiene IP| C["Ocupado (DNS)"]
    B -->|Sin IP| D["Paso 2: Consulta WHOIS Sockets"]
    D --> E{"¿Registrado?"}
    E -->|No| F["¡DISPONIBLE!"]
    E -->|Sí| G["Ocupado (WHOIS)"]
    E -->|Error| H["Desconocido"]

    style F fill:#00e676,stroke:#00e676,color:#070b13,font-weight:bold
    style C fill:#ff1744,stroke:#ff1744,color:#ffffff,font-weight:bold
    style G fill:#ff1744,stroke:#ff1744,color:#ffffff,font-weight:bold
    style H fill:#ffea00,stroke:#ffea00,color:#070b13,font-weight:bold
```

---

## 📄 Licencia y Atribución

Este proyecto se distribuye bajo una **Licencia Personalizada de Uso No Comercial y Atribución Obligatoria**.

*   **Uso No Comercial Estricto (Prohibido monetizar):** Queda estrictamente prohibido vender, alquilar, sublicenciar, comercializar o usar este software o cualquier parte de su código fuente para beneficio comercial directo o indirecto. **No está permitido colocar anuncios (Ads) en la Play Store o Web.**
*   **Requisito de Atribución Obligatoria:** Al publicar o redistribuir versiones (modificadas o compiladas) de este software, **debes mantener visible en la interfaz** el enlace al repositorio original de GitHub del motor LiberDom en el cual está basado:  
    `https://github.com/NeoTurcios/openfind`

---

Desarrollado con pasión y código abierto. ¡Disfruta de **OpenFind AI**! 🚀
