/* ==========================================================================
   INTERACTIVIDAD Y TRADUCCIONES - OPENFIND AI LANDING SHOWCASE
   ========================================================================= */

// ==========================================================================
// 1. Diccionario Global de Traducciones (I18n Engine - PURE TEXTS)
// ==========================================================================
const translations = {
    es: {
        "nav.start": "Inicio",
        "nav.tools": "Ecosistema",
        "nav.arch": "Flujo",
        "nav.about": "Nosotros",
        "nav.github": "Código",
        "hero.github": "Ver Repositorio",

        "nav.tab_android": "Android Client",
        "nav.tab_cli": "Termux CLI",
        "nav.tab_bot": "Telegram Bot",

        "hero.badge": "Ecosistema 100% Autónomo & Local",
        "hero.title": "Búsqueda Inteligente de Dominios a Nivel de Red",
        "hero.subtitle": "El motor híbrido definitivo que combina resolución DNS ultrarrápida, sockets TCP recursivos WHOIS y agentes locales de marca. Diseñado para Android, terminales Termux y Telegram.",
        "hero.btn_android": "Explorar Herramientas",

        "tools.section_title": "El Ecosistema OpenFind AI",
        "tools.subtitle": "Explora las potentes utilidades integradas en nuestro ecosistema de código abierto.",

        "app.tech_label": "Arquitectura Móvil",
        "app.title": "OpenFind App - Cliente Android",
        "app.feat1_title": "Kotlin Puro (openfind.ai)",
        "app.feat1_desc": "Compilado bajo Android 16 (SDK 36) con soporte retrospectivo estable hasta SDK 26. Código 100% Kotlin limpio, libre de Java.",
        "app.feat2_title": "Agente IA de Marca Lingüístico",
        "app.feat2_desc": "Evalúa dominios localmente según fluidez silábica, memorabilidad, idoneidad del TLD, y se personaliza aprendiendo de los intereses almacenados en tu dispositivo.",
        "app.feat3_title": "Almacenamiento Inteligente (Límite: 10)",
        "app.feat3_desc": "Evita bases de datos lentas limitando el almacenamiento a 10 elementos. Avisa al usuario con un elegante diálogo interactivo Choice A/B/Cancelar.",
        "app.feat4_title": "Sistema de Iconos XML Sin Emojis",
        "app.feat4_desc": "Cumple con las normas visuales de las tiendas de apps modernas, utilizando exclusivamente drawables vectoriales XML nítidos para todas las acciones de la interfaz.",
        "app.download_btn": "Descargar APK Compilada",

        "cli.tech_label": "Consola y Red",
        "cli.title": "OpenFind Termux - CLI Engine",
        "cli.desc_p": "Especialmente diseñado para ejecutarse en terminales de celulares Android (a través de la app Termux) y servidores Linux. Escrito en Python nativo puro, sin dependencias pesadas ni necesidad de compiladores.",
        "cli.step1_title": "Instalación en un solo comando:",
        "cli.step2_title": "Ejecución rápida (Alias directo):",
        "cli.step2_helper": "El instalador crea de forma segura un alias de sistema en tu terminal.",
        "cli.features_title": "Funciones de la CLI",
        "cli.feat1_title": "Auditoría Individual de Dominios",
        "cli.feat1_desc": "Combina resolución DNS instantánea y sockets TCP directos en el puerto 43 para verificar disponibilidad real sin límites de APIs externas.",
        "cli.feat2_title": "Escaneo Masivo por Lotes",
        "cli.feat2_desc": "Procesa listas grandes de dominios cargando archivos .txt o pegando texto. Incluye filtro de duplicados y control de retraso anti-bloqueo.",
        "cli.feat3_title": "Generador de Nombres Inteligente",
        "cli.feat3_desc": "Crea ideas mezclando palabras clave con prefijos, sufijos y estilos modernos de IA, verificando disponibilidad en tiempo real.",
        "cli.feat4_title": "Guía de Red y Consola Local",
        "cli.feat4_desc": "Ayuda interactiva integrada sobre reglas de TLDs y WHOIS. Soporta localización completa en Español e Inglés sin conexión.",

        "bot.tech_label": "Agente de Red Conversacional",
        "bot.title": "Telegram Bot Autónomo",
        "bot.desc_p": "Integra un script de bot en Python que opera de manera asíncrona sobre los servidores de Telegram. Te permite interactuar y auditar dominios enviando mensajes de chat simples desde cualquier lugar.",
        "bot.feat1_title": "Respuestas en Milisegundos",
        "bot.feat1_desc": "Combina los mismos motores de sockets TCP para procesar de forma inmediata la disponibilidad de dominios y devolver tarjetas con formato HTML.",
        "bot.feat2_title": "Configuración en Consola Segura",
        "bot.feat2_desc": "Al ejecutar python telegram_bot.py por primera vez, el CLI te pedirá de forma segura tu token de BotFather y creará un archivo de configuración local cifrado.",
        "bot.feat3_title": "Reporte Detallado de Red",
        "bot.feat3_desc": "Devuelve la IP activa del dominio, el registrador actual y la fecha de creación en un formato interactivo y fácil de leer.",
        "bot.feat4_title": "Operación 24/7 Autónoma",
        "bot.feat4_desc": "Script ligero en Python diseñado para ejecutarse asíncronamente como servicio en Termux o servidores VPS remotos con mínimo consumo.",

        "arch.title": "¿Cómo funciona bajo el capó?",
        "arch.subtitle": "El motor de OpenFind no depende de intermediarios costosos. Funciona directamente en las capas de red de internet.",
        "arch.step1_title": "Paso 1: Resolución DNS",
        "arch.step1_desc": "Realiza una consulta ultra-veloz a los servidores DNS. Si el dominio responde con una dirección IP activa, se marca como Ocupado inmediatamente sin consumir recursos adicionales.",
        "arch.step2_title": "Paso 2: Consulta Socket WHOIS",
        "arch.step2_desc": "Si no hay registros DNS, abre un socket TCP directo en el puerto 43 hacia el servidor de IANA y redirige recursivamente la consulta al servidor TLD oficial para confirmar si está libre.",
        "arch.step3_title": "Paso 3: Evaluación de Marca",
        "arch.step3_desc": "El agente de inteligencia local del dispositivo procesa el nombre y genera calificaciones dinámicas de memorabilidad y fluidez del nombre de marca.",

        "about.title": "Nosotros y Licencia del Proyecto",
        "about.creator_title": "Desarrollador Principal",
        "about.bio": "Creador de herramientas autónomas, optimizadas para el rendimiento móvil y de red local. Desarrollando soluciones libres de APIs comerciales invasivas.",
        "about.license_title": "Licencia de Uso No Comercial",
        "about.license_p1": "Este software está distribuido bajo los términos de una licencia personalizada de Uso Personal No Comercial con Atribución Obligatoria.",
        "about.license_item1": "Prohibido monetizar: Queda estrictamente prohibido vender, alquilar, sublicenciar o colocar publicidad comercial en este software o sus derivados.",
        "about.license_item2": "Atribución obligatoria: Al redistribuir, se debe mantener de manera visible en la interfaz el enlace al repositorio original del motor.",
        "about.license_btn": "Leer Licencia Completa",
        "about.projects_title": "Más Proyectos de NeoTurcios",
        "about.proj1_desc": "Explora la lista completa de utilidades de consola y scripts en GitHub.",
        "about.proj2_desc": "Plataforma oficial y núcleo del ecosistema digital de desarrollo.",
        "about.privacy_btn": "Política de Privacidad de la Play Console",

        "footer.text": "Diseñado con amor y código abierto por NeoTurcios | Licencia No Comercial © 2026"
    },
    en: {
        "nav.start": "Home",
        "nav.tools": "Ecosystem",
        "nav.arch": "Flow",
        "nav.about": "About Us",
        "nav.github": "Code",
        "hero.github": "View Repository",

        "nav.tab_android": "Android Client",
        "nav.tab_cli": "Termux CLI",
        "nav.tab_bot": "Telegram Bot",

        "hero.badge": "100% Autonomous & Local Ecosystem",
        "hero.title": "Smart Domain Audit at Network Level",
        "hero.subtitle": "The ultimate hybrid engine combining ultra-fast DNS resolution, recursive WHOIS TCP sockets, and local brand agents. Built for Android, Termux terminals, and Telegram.",
        "hero.btn_android": "Explore Tools",

        "tools.section_title": "The OpenFind AI Ecosystem",
        "tools.subtitle": "Explore the powerful utilities integrated into our open-source ecosystem.",

        "app.tech_label": "Mobile Architecture",
        "app.title": "OpenFind App - Android Client",
        "app.feat1_title": "Pure Kotlin Code (openfind.ai)",
        "app.feat1_desc": "Compiled under Android 16 (SDK 36) with stable backward compatibility down to SDK 26. Clean 100% Kotlin codebase structured in two package levels, free of Java.",
        "app.feat2_title": "Linguistic Brand AI Agent",
        "app.feat2_desc": "Evaluates domains locally based on syllable rhythm, memorability, TLD fitness, and customizes itself by learning from saved items on your device.",
        "app.feat3_title": "Smart Storage Capping (Limit: 10)",
        "app.feat3_desc": "Prevents database bloating or lag by restricting local database items to 10. Prompts the user with an elegant dialog to clear or auto-clean storage.",
        "app.feat4_title": "XML Vector Icons System (No Emojis)",
        "app.feat4_desc": "Strictly complies with modern app store guidelines, using exclusively vector XML drawables for all visual actions.",
        "app.download_btn": "Download Compiled APK",

        "cli.tech_label": "Console & Network",
        "cli.title": "OpenFind Termux - CLI Engine",
        "cli.desc_p": "Specially designed to run on Android phone terminal emulators (Termux) and Linux servers. Written in pure native Python, with zero external dependencies.",
        "cli.step1_title": "One-command Installation:",
        "cli.step2_title": "Fast Execution (Direct Alias):",
        "cli.step2_helper": "The installer securely registers a binary system alias in your terminal path.",
        "cli.features_title": "CLI Features",
        "cli.feat1_title": "Individual Domain Audit",
        "cli.feat1_desc": "Combines instant DNS resolution and direct TCP sockets on port 43 to verify real-time availability without external API limits.",
        "cli.feat2_title": "Bulk Domain Batch Scan",
        "cli.feat2_desc": "Processes large domain lists by loading .txt files or pasting text. Includes duplicate filtering and anti-blocking rate limit control.",
        "cli.feat3_title": "Smart Name Generator",
        "cli.feat3_desc": "Generates ideas by combining keywords with prefixes, suffixes, and modern AI styles, checking availability in real-time.",
        "cli.feat4_title": "Network Guide & Local Console",
        "cli.feat4_desc": "Embedded interactive help on TLD rules and WHOIS. Supports full Spanish and English localization 100% offline.",

        "bot.tech_label": "Conversational Network Agent",
        "bot.title": "Autonomous Telegram Bot",
        "bot.desc_p": "Integrates an asynchronous Python bot script operating over Telegram APIs. It enables auditing and inspecting domains directly on the go via chat messages.",
        "bot.feat1_title": "Millisecond Response Cards",
        "bot.feat1_desc": "Utilizes the same low-level TCP socket engines to process domains instantly and return cards formatted with clean HTML tags.",
        "bot.feat2_title": "Secure Console Setup",
        "bot.feat2_desc": "Running python telegram_bot.py for the first time will securely prompt for your BotFather token and generate a local encrypted config file.",
        "bot.feat3_title": "Detailed Network Report",
        "bot.feat3_desc": "Returns active domain IP, registrar details, and creation date in a beautifully formatted message.",
        "bot.feat4_title": "Autonomous 24/7 Operation",
        "bot.feat4_desc": "Lightweight Python script optimized for running as an asynchronous daemon in Termux or VPS with minimal footprint.",

        "arch.title": "How does it work under the hood?",
        "arch.subtitle": "The OpenFind engine does not rely on third-party brokers. It runs directly on internet network layers.",
        "arch.step1_title": "Step 1: DNS Resolution",
        "arch.step1_desc": "Executes an ultra-fast DNS lookup. If the domain resolves to an active IP address, it is immediately marked as Taken, saving network resources.",
        "arch.step2_title": "Step 2: WHOIS Socket Query",
        "arch.step2_desc": "If no DNS records exist, it opens a direct TCP socket on port 43 to IANA and recursively queries official TLD servers to confirm availability.",
        "arch.step3_title": "Step 3: Brand Assessment",
        "arch.step3_desc": "The local device AI agent processes the brand name and calculates dynamic scores for memorability and syllable pronunciation.",

        "about.title": "Repository Details & License",
        "about.creator_title": "Lead Developer",
        "about.bio": "Creator of autonomous utilities, optimized for mobile and local network performance. Developing lightweight software free of commercial APIs.",
        "about.license_title": "Non-Commercial Use License",
        "about.license_p1": "This software is distributed under a customized license of Personal Non-Commercial Use with Mandatory Attribution.",
        "about.license_item1": "Monetization Banned: Selling, renting, sublicensing, or putting commercial ads in this software is strictly prohibited.",
        "about.license_item2": "Mandatory Attribution: When redistributing, you must preserve a visible link to the original repository.",
        "about.license_btn": "Read Full License Terms",
        "about.projects_title": "More Projects by NeoTurcios",
        "about.proj1_desc": "Explore the complete portfolio of CLI scripts and tools on GitHub.",
        "about.proj2_desc": "Official core and portal of the digital development ecosystem.",
        "about.privacy_btn": "Play Console Privacy Policy",

        "footer.text": "Designed with love and open source by NeoTurcios | Non-Commercial License © 2026"
    }
};

let currentLang = localStorage.getItem("openfind_lang") || "es";

// ==========================================================================
// 2. Inicialización
// ==========================================================================
document.addEventListener("DOMContentLoaded", () => {
    inicializarSelectorIdioma();
    inicializarCopiarCodigo();
    inicializarNavegacionScroll();
    inicializarPestanasDashboard();
    
    // Aplicar traducción inicial
    aplicarTraducciones(currentLang);
});

// ==========================================================================
// 3. Sistema de Idioma e Interfaz (I18n Switcher)
// ==========================================================================
function inicializarSelectorIdioma() {
    const langBtn = document.getElementById("lang-btn");
    const langDropdown = document.getElementById("lang-dropdown");
    const langOptions = document.querySelectorAll(".lang-option");

    langBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        langDropdown.classList.toggle("show");
    });

    document.addEventListener("click", () => {
        langDropdown.classList.remove("show");
    });

    langOptions.forEach(opt => {
        opt.addEventListener("click", () => {
            const lang = opt.getAttribute("data-lang");
            currentLang = lang;
            localStorage.setItem("openfind_lang", lang);
            aplicarTraducciones(lang);
        });
    });
}

function aplicarTraducciones(lang) {
    document.querySelectorAll("[data-i18n]").forEach(elem => {
        const key = elem.getAttribute("data-i18n");
        if (translations[lang] && translations[lang][key]) {
            elem.textContent = translations[lang][key];
        }
    });

    // Actualizar etiquetas visuales de selector de idioma
    document.getElementById("current-lang-label").innerText = lang === "es" ? "Español" : "English";
    
    document.querySelectorAll(".lang-option").forEach(opt => {
        if (opt.getAttribute("data-lang") === lang) {
            opt.classList.add("active");
        } else {
            opt.classList.remove("active");
        }
    });
}

// ==========================================================================
// 4. Copiar Código en Portapapeles (Clipboard Copy)
// ==========================================================================
function inicializarCopiarCodigo() {
    const copyButtons = document.querySelectorAll(".copy-code-btn");

    copyButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const targetId = btn.getAttribute("data-target");
            const codeText = document.getElementById(targetId).innerText;

            navigator.clipboard.writeText(codeText).then(() => {
                const originalIcon = btn.innerHTML;
                btn.innerHTML = `<i class="fa-solid fa-check" style="color: var(--neon-green);"></i>`;
                btn.style.pointerEvents = "none";

                setTimeout(() => {
                    btn.innerHTML = originalIcon;
                    btn.style.pointerEvents = "auto";
                }, 2000);
            }).catch(err => {
                console.error("Error al copiar al portapapeles: ", err);
            });
        });
    });
}

// ==========================================================================
// 5. Navegación por Scroll Activa (Active Section Scroll Highlighter)
// ==========================================================================
function inicializarNavegacionScroll() {
    const tabLinks = document.querySelectorAll(".tab-link");
    const sections = document.querySelectorAll("section[id]");

    window.addEventListener("scroll", resaltarEnlacesNavegacion);

    function resaltarEnlacesNavegacion() {
        let scrollY = window.pageYOffset;
        
        sections.forEach(current => {
            const sectionHeight = current.offsetHeight;
            const sectionTop = current.offsetTop - 120;
            const sectionId = current.getAttribute("id");
            
            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                tabLinks.forEach(link => {
                    link.classList.remove("active");
                    if (link.getAttribute("href") === `#${sectionId}`) {
                        link.classList.add("active");
                    }
                });
            }
        });
    }

    tabLinks.forEach(link => {
        link.addEventListener("click", () => {
            tabLinks.forEach(l => l.classList.remove("active"));
            link.classList.add("active");
        });
    });
}

// ==========================================================================
// 6. Pestanas del Dashboard Interactivo (Vercel-Style Tab Switcher)
// ==========================================================================
function inicializarPestanasDashboard() {
    const dashTabs = document.querySelectorAll(".dash-tab");
    const dashPanels = document.querySelectorAll(".dash-panel");

    dashTabs.forEach(btn => {
        btn.addEventListener("click", () => {
            const target = btn.getAttribute("data-dash");

            dashTabs.forEach(t => t.classList.remove("active"));
            dashPanels.forEach(p => p.classList.remove("active"));

            btn.classList.add("active");
            document.getElementById(`dash-panel-${target}`).classList.add("active");
        });
    });
}
