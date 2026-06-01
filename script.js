/* ==========================================================================
   INTERACTIVIDAD Y INTELIGENCIA LOCAL - OPENFIND AI
   ========================================================================== */

// ==========================================================================
// 1. Diccionario Global de Traducciones (I18n Engine)
// ==========================================================================
const translations = {
    es: {
        "nav.generator": '<i class="fa-solid fa-wand-magic-sparkles"></i> Generador IA',
        "nav.fastcheck": '<i class="fa-solid fa-circle-check"></i> Escáner DNS',
        "nav.androidapp": '<i class="fa-solid fa-mobile-screen-button"></i> App Android',
        "nav.termuxcli": '<i class="fa-solid fa-terminal"></i> Termux CLI',
        "nav.about": '<i class="fa-solid fa-user-gear"></i> Nosotros',
        "nav.github": '<i class="fa-brands fa-github"></i> Código',

        "gen.title": "Generador de Dominios Inteligente y Autónomo",
        "gen.subtitle": "Crea ideas corporativas y creativas que se analizan en milisegundos con nuestro Agente IA local 100% libre de APIs externas.",
        "gen.config_title": '<i class="fa-solid fa-sliders"></i> Ajustes de Generación',
        "gen.label_keyword": "Palabra Clave o Idea Inicial:",
        "gen.label_style": "Estilo de Marca:",
        "gen.style_ai": "💡 Creativo & Inteligencia Artificial",
        "gen.style_corp": "🏢 Corporativo & Elegante (Galaxy Style)",
        "gen.style_short": "⚡ Ultra-Moderno & Corto (Yi Style)",
        "gen.style_geek": "🤖 Tecnológico & Geek",
        "gen.label_tld": "Extensión (TLD):",
        "gen.tld_all": "Todas las Extensiones Modernas",
        "gen.memory": "Memoria Local",
        "gen.ideas_title": '<i class="fa-solid fa-robot"></i> Recomendaciones de la IA',
        "gen.empty_text": "Ingresa una palabra clave a la izquierda y presiona Generar para despertar al Agente Autónomo.",
        "gen.saved_title": "Biblioteca de Favoritos Guardados",
        "gen.clear_btn": "Limpiar Todo",
        "gen.empty_saved": "No tienes dominios guardados en la memoria de tu navegador. Guarda tus preferidos desde la lista de recomendaciones.",
        
        "fast.title": "Escáner Masivo DNS en Paralelo",
        "fast.subtitle": "Pega una lista de palabras o dominios. Consultamos en paralelo a través de DNS-over-HTTPS (DoH) sin límites de velocidad.",
        "fast.label": "Pega tus dominios o palabras clave:",
        "fast.provider": "Servidor DNS Seguro:",
        "fast.start_btn": "Iniciar escaneo en paralelo",
        "fast.progress_idle": "Preparado para escanear...",
        "fast.stat_avail": "DNS Disponible",
        "fast.stat_taken": "DNS Ocupado",
        "fast.results_title": '<i class="fa-solid fa-list-check"></i> Resultados en tiempo real:',
        "fast.download_txt": "Reporte TXT",
        "fast.download_pdf": "Reporte PDF",
        "fast.empty_text": "Ingresa tu lista arriba y ejecuta el escaneo para ver los resultados.",

        "app.title": "OpenFind App - Versión Android Nativa",
        "app.subtitle": "Lleva todo el poder de los agentes autónomos de dominios directamente en tu teléfono inteligente.",
        "app.tech_title": '<i class="fa-solid fa-code"></i> Arquitectura Android 16 Premium',
        "app.tech_desc": "Desarrollada utilizando Kotlin Moderno en su totalidad, estructurada bajo un namespace limpio en solo dos niveles de carpetas (<code>openfind.ai</code>). Libre de código Java obsoleto.",
        "app.icons_title": '<i class="fa-solid fa-icons"></i> Sistema de Iconos Vectoriales Puros',
        "app.icons_desc": "Cumpliendo estrictamente las directrices estéticas de las tiendas modernas, se reemplazan todos los emojis vulgares en la interfaz por iconos vectoriales XML estilizados (Outlines y Filled) para lograr una estética profesional.",
        "app.limit_title": '<i class="fa-solid fa-database"></i> Gestión de Almacenamiento Inteligente',
        "app.limit_desc": "Para mantener la base de datos local ligera y libre de registros eternos o basura, el sistema limita el historial y los favoritos a un máximo de 10 elementos. Al llegar al límite, un diálogo proactivo solicita decidir entre el vaciado manual de la memoria o la autolimpieza inteligente periódica.",
        "app.download_btn": "Descargar APK Compilada",

        "cli.title": "OpenFind en tu terminal con Termux",
        "cli.subtitle": "Cómo instalar y ejecutar la versión CLI rápida optimizada para celulares y servidores Linux.",
        "cli.step1_title": "Instalación en un solo comando",
        "cli.step1_desc": "Abre Termux en tu Android, copia la línea de abajo y pégala para clonar, configurar e instalar el binario automáticamente:",
        "cli.step2_title": "Cómo ejecutar la aplicación CLI",
        "cli.step2_desc": "Una vez completado el instalador, puedes arrancar la herramienta en cualquier momento desde cualquier carpeta escribiendo:",
        "cli.step2_helper": '<i class="fa-solid fa-circle-info"></i> Se creará un alias directo en los binarios de tu terminal.',
        "cli.step3_title": '<i class="fa-solid fa-bolt"></i> Beneficios de usar la versión de Consola',
        "cli.step3_item1": '<i class="fa-solid fa-bolt"></i> <strong>Rendimiento instantáneo:</strong> Consultas a nivel de red directa a través de sockets TCP recursivos.',
        "cli.step3_item2": '<i class="fa-solid fa-file-import"></i> <strong>Importación local:</strong> Carga y analiza archivos físicos `.txt` en bloque desde tu almacenamiento interno.',
        "cli.step3_item3": '<i class="fa-solid fa-shield-halved"></i> <strong>Cero telemetría:</strong> Todo opera en tu dispositivo local, sin llamadas de red a terceros ni cuotas de APIs de pago.',

        "about.title": "Detalles del Proyecto y Nosotros",
        "about.subtitle": "Conoce los principios, políticas y enlaces clave que rigen a OpenFind AI.",
        "about.creator_title": "Desarrollador Principal",
        "about.bio": "Creador de herramientas autónomas, optimizadas para el rendimiento móvil y de red local. Desarrollando soluciones libres de APIs comerciales invasivas.",
        "about.license_title": '<i class="fa-solid fa-file-signature"></i> Licencia de Uso No Comercial',
        "about.license_p1": "Este software está distribuido bajo los términos de una licencia personalizada de <strong>Uso Personal No Comercial con Atribución Obligatoria</strong>.",
        "about.license_item1": '<i class="fa-solid fa-circle-xmark" style="color: var(--neon-red)"></i> Prohibido monetizar: Queda estrictamente prohibido vender, alquilar, sublicenciar o colocar publicidad comercial en este software o sus derivados.',
        "about.license_item2": '<i class="fa-solid fa-circle-check" style="color: var(--neon-green)"></i> Atribución obligatoria: Al redistribuir, se debe mantener de manera visible en la interfaz el enlace al repositorio original del motor.',
        "about.license_btn": "Leer Licencia Completa",
        "about.projects_title": '<i class="fa-solid fa-folder-open"></i> Más Proyectos de NeoTurcios',
        "about.proj1_desc": "Explora la lista completa de utilidades de consola y scripts en GitHub.",
        "about.proj2_desc": "Plataforma oficial y núcleo del ecosistema digital de desarrollo.",
        "about.privacy_btn": "Política de Privacidad de la Play Console",

        "footer.text": "Diseñado con amor y código abierto por <strong>NeoTurcios</strong> | Licencia No Comercial © 2026",

        // Modales
        "modal.title": "Límite de memoria alcanzado",
        "modal.desc": "Veo que la lista de favoritos y guardados está llena (Límite: 10 elementos). ¿Qué deseas hacer para continuar?",
        "modal.opt_a_title": "Opción A: Vaciar toda la lista",
        "modal.opt_a_desc": "Borra por completo todos los favoritos guardados para empezar de cero con la memoria limpia.",
        "modal.opt_b_title": "Opción B: Autolimpieza Automática",
        "modal.opt_b_desc": "Elimina automáticamente las recomendaciones más antiguas al guardar nuevas para mantener el límite en 10.",
        "modal.confirm_btn": "Confirmar Acción",
        "modal.cancel_btn": "Cancelar",

        // Alertas y estados dinámicos
        "alert.enter_keyword": "Por favor, introduce una palabra clave.",
        "alert.no_domains": "Introduce al menos un dominio para escanear.",
        "alert.scanning": "Escaneando...",
        "alert.progress": "Escaneando: {processed} de {total} dominios...",
        "alert.finished": '<i class="fa-solid fa-circle-check" style="color: var(--neon-green);"></i> ¡Escaneo masivo finalizado! ({processed}/{total})',
        
        "status.available": "Disponible",
        "status.taken": "Ocupado (DNS)",
        "status.checking": "Comprobando...",
        
        "msg.recommend": "🤖 Yo te recomiendo esta",
        "msg.metric_pron": "Pronunciación",
        "msg.metric_mem": "Memorabilidad",
        "msg.metric_len": "Longitud",
        "msg.metric_tld": "TLD Fit",
        "msg.technical_score": "Calificación Técnica del Agente:"
    },
    en: {
        "nav.generator": '<i class="fa-solid fa-wand-magic-sparkles"></i> AI Generator',
        "nav.fastcheck": '<i class="fa-solid fa-circle-check"></i> DNS Scanner',
        "nav.androidapp": '<i class="fa-solid fa-mobile-screen-button"></i> Android App',
        "nav.termuxcli": '<i class="fa-solid fa-terminal"></i> Termux CLI',
        "nav.about": '<i class="fa-solid fa-user-gear"></i> About Us',
        "nav.github": '<i class="fa-brands fa-github"></i> Code',

        "gen.title": "Smart & Autonomous Domain Generator",
        "gen.subtitle": "Create brand and creative domain ideas analyzed in milliseconds by our local AI Agent, 100% free of external APIs.",
        "gen.config_title": '<i class="fa-solid fa-sliders"></i> Generation Settings',
        "gen.label_keyword": "Keyword or Starting Concept:",
        "gen.label_style": "Brand Style:",
        "gen.style_ai": "💡 Creative & Artificial Intelligence",
        "gen.style_corp": "🏢 Corporate & Elegant (Galaxy Style)",
        "gen.style_short": "⚡ Ultra-Modern & Short (Yi Style)",
        "gen.style_geek": "🤖 Tech & Geek Style",
        "gen.label_tld": "Extension (TLD):",
        "gen.tld_all": "All Modern Extensions",
        "gen.memory": "Local Memory",
        "gen.ideas_title": '<i class="fa-solid fa-robot"></i> AI Recommendations',
        "gen.empty_text": "Enter a keyword on the left and click Generate to wake up the Autonomous Agent.",
        "gen.saved_title": "Saved Favorites Library",
        "gen.clear_btn": "Clear All",
        "gen.empty_saved": "You don't have domains saved in your browser's memory. Save your preferred ones from the recommendation list.",

        "fast.title": "Parallel DNS Mass Scanner",
        "fast.subtitle": "Paste a list of words or domains. We query them in parallel via DNS-over-HTTPS (DoH) with zero speed limits.",
        "fast.label": "Paste your domains or keywords:",
        "fast.provider": "Secure DNS Server:",
        "fast.start_btn": "Start Parallel Scan",
        "fast.progress_idle": "Ready to scan...",
        "fast.stat_avail": "DNS Available",
        "fast.stat_taken": "DNS Occupied",
        "fast.results_title": '<i class="fa-solid fa-list-check"></i> Real-time Results:',
        "fast.download_txt": "TXT Report",
        "fast.download_pdf": "PDF Report",
        "fast.empty_text": "Enter your list above and execute the scan to view results.",

        "app.title": "OpenFind App - Native Android Version",
        "app.subtitle": "Take all the power of autonomous domain agents directly onto your smartphone.",
        "app.tech_title": '<i class="fa-solid fa-code"></i> Premium Android 16 Architecture',
        "app.tech_desc": "Fully developed using modern Kotlin, structured under a clean namespace of only two package levels (<code>openfind.ai</code>). Completely free of legacy Java code.",
        "app.icons_title": '<i class="fa-solid fa-icons"></i> Pure Vector Icon System',
        "app.icons_desc": "Strictly complying with modern app store design systems, all emojis in the UI have been replaced by outlined/filled XML vector icons for a professional premium look.",
        "app.limit_title": '<i class="fa-solid fa-database"></i> Smart Local Storage Capping',
        "app.limit_desc": "To keep the local database light and free of infinite garbage logs, history and bookmarks are capped at 10 items. When reaching the limit, a custom alert requests to clear the list or trigger auto-cleanup.",
        "app.download_btn": "Download Compiled APK",

        "cli.title": "OpenFind on your terminal with Termux",
        "cli.subtitle": "How to install and run the fast CLI version optimized for Android phones and Linux servers.",
        "cli.step1_title": "One-command Installation",
        "cli.step1_desc": "Open Termux on your Android, copy the line below, and paste it to clone, configure, and install the binary automatically:",
        "cli.step2_title": "How to Run the CLI App",
        "cli.step2_desc": "Once the installer finishes, you can start the tool at any time from any folder by typing:",
        "cli.step2_helper": '<i class="fa-solid fa-circle-info"></i> A direct binary alias will be created in your terminal binaries.',
        "cli.step3_title": '<i class="fa-solid fa-bolt"></i> Benefits of Using the Console Version',
        "cli.step3_item1": '<i class="fa-solid fa-bolt"></i> <strong>Instant Performance:</strong> Direct network queries using low-level recursive WHOIS socket connections.',
        "cli.step3_item2": '<i class="fa-solid fa-file-import"></i> <strong>Local Importation:</strong> Load and analyze physical `.txt` files directly from your internal storage.',
        "cli.step3_item3": '<i class="fa-solid fa-shield-halved"></i> <strong>Zero Telemetry:</strong> Everything runs locally on your device with no calls to third-party paid APIs.',

        "about.title": "Project Details and About Us",
        "about.subtitle": "Get to know the core principles, licenses, and credentials that power OpenFind AI.",
        "about.creator_title": "Lead Developer",
        "about.bio": "Creator of autonomous tools, optimized for mobile performance and local network efficiency. Developing systems free of commercial APIs.",
        "about.license_title": '<i class="fa-solid fa-file-signature"></i> Non-Commercial Use License',
        "about.license_p1": "This software is distributed under a customized license of <strong>Personal Non-Commercial Use with Mandatory Attribution</strong>.",
        "about.license_item1": '<i class="fa-solid fa-circle-xmark" style="color: var(--neon-red)"></i> Monetization Banned: Selling, renting, sublicensing, or putting commercial ads in this software is strictly prohibited.',
        "about.license_item2": '<i class="fa-solid fa-circle-check" style="color: var(--neon-green)"></i> Mandatory Attribution: When redistributing, you must preserve the link to the original motor GitHub repository.',
        "about.license_btn": "Read Full License Terms",
        "about.projects_title": '<i class="fa-solid fa-folder-open"></i> More NeoTurcios Projects',
        "about.proj1_desc": "Explore the complete portfolio of CLI scripts and tools on GitHub.",
        "about.proj2_desc": "Official core and portal of the digital development ecosystem.",
        "about.privacy_btn": "Play Console Privacy Policy",

        "footer.text": "Designed with love and open source by <strong>NeoTurcios</strong> | Non-Commercial License © 2026",

        // Modals
        "modal.title": "Memory limit reached",
        "modal.desc": "I see that the saved favorites list is full (Limit: 10 items). What would you like to do to continue?",
        "modal.opt_a_title": "Option A: Empty the entire list",
        "modal.opt_a_desc": "Wipe out all saved domains to start fresh with fully clean storage.",
        "modal.opt_b_title": "Option B: Dynamic Auto-Cleanup",
        "modal.opt_b_desc": "Automatically delete the oldest saved recommendations when new ones are added to keep the limit at 10.",
        "modal.confirm_btn": "Confirm Action",
        "modal.cancel_btn": "Cancel",

        // Alerts and dynamic states
        "alert.enter_keyword": "Please enter a keyword.",
        "alert.no_domains": "Enter at least one domain to scan.",
        "alert.scanning": "Scanning...",
        "alert.progress": "Scanning: {processed} of {total} domains...",
        "alert.finished": '<i class="fa-solid fa-circle-check" style="color: var(--neon-green);"></i> Bulk scan completed! ({processed}/{total})',
        
        "status.available": "Available",
        "status.taken": "Taken (DNS)",
        "status.checking": "Checking...",
        
        "msg.recommend": "🤖 Recommended by AI",
        "msg.metric_pron": "Pronunciation",
        "msg.metric_mem": "Memorability",
        "msg.metric_len": "Length",
        "msg.metric_tld": "TLD Fit",
        "msg.technical_score": "Agent Technical Score:"
    }
};

let currentLang = localStorage.getItem("openfind_lang") || "es";
let savedDomains = JSON.parse(localStorage.getItem("openfind_saved")) || [];
let autoCleanupEnabled = localStorage.getItem("openfind_autocleanup") === "true";
let pendingSaveDomain = null; // Guarda el dominio temporalmente mientras se abre el modal A/B

// ==========================================================================
// 2. Inicialización de la Aplicación
// ==========================================================================
document.addEventListener("DOMContentLoaded", () => {
    inicializarPestanas();
    inicializarCopiarCodigo();
    inicializarSelectorIdioma();
    inicializarGeneradorIA();
    inicializarEscanerMasivo();
    inicializarModalAlmacenamiento();
    
    // Cargar biblioteca de memoria guardada
    renderizarGuardados();
    
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
            // Preservar iconos internos si existen
            const icon = elem.querySelector("i");
            if (icon) {
                const iconHtml = icon.outerHTML;
                const cleanText = translations[lang][key].replace(/<i[^>]*><\/i>/i, "").trim();
                elem.innerHTML = `${iconHtml} ${cleanText}`;
            } else {
                elem.innerHTML = translations[lang][key];
            }
        }
    });

    // Inputs Placeholders
    const inputKeyword = document.getElementById("gen-keyword");
    if (inputKeyword) {
        inputKeyword.placeholder = lang === "es" ? "Ej: neo, galaxy, cloud..." : "E.g. neo, galaxy, cloud...";
    }
    const bulkTextarea = document.getElementById("bulk-textarea");
    if (bulkTextarea) {
        bulkTextarea.placeholder = lang === "es" ?
            "google.com\ngithub.com, neopunto.com\nmisitiolibrequeinvente.net\n# Puedes separar por comas o saltos de línea..." :
            "google.com\ngithub.com, neopunto.com\nmybrandnewsiteidea.net\n# You can separate by commas or line breaks...";
    }

    // Actualizar etiquetas de selector de idioma
    document.getElementById("current-lang-label").innerText = lang === "es" ? "Español" : "English";
    
    document.querySelectorAll(".lang-option").forEach(opt => {
        if (opt.getAttribute("data-lang") === lang) {
            opt.classList.add("active");
        } else {
            opt.classList.remove("active");
        }
    });

    // Volver a renderizar los contenedores que dependen de traducciones reactivas
    actualizarContadoresMemoria();
}

// ==========================================================================
// 4. Manejador de Navegación por Pestañas
// ==========================================================================
function inicializarPestanas() {
    const tabButtons = document.querySelectorAll(".tab-btn");
    const tabPanels = document.querySelectorAll(".tab-panel");

    tabButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const targetTab = btn.getAttribute("data-tab");

            tabButtons.forEach(b => b.classList.remove("active"));
            tabPanels.forEach(p => p.classList.remove("active"));

            btn.classList.add("active");
            document.getElementById(`tab-${targetTab}`).classList.add("active");
        });
    });

    // Enlace de logo a pestaña de inicio (Generator)
    document.getElementById("header-logo").addEventListener("click", () => {
        tabButtons[0].click();
    });
}

// ==========================================================================
// 5. Copiar Código en Portapapeles (Clipboard Copy)
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
                console.error("Error copying text: ", err);
            });
        });
    });
}

// ==========================================================================
// 6. Generador Inteligente y Autónomo (Local AI Agent Engine)
// ==========================================================================
function inicializarGeneradorIA() {
    const btnGenerate = document.getElementById("btn-generate");
    const inputKeyword = document.getElementById("gen-keyword");
    const selectStyle = document.getElementById("gen-style");
    const selectTld = document.getElementById("gen-tld");
    const gridIdeas = document.getElementById("generator-ideas-grid");

    btnGenerate.addEventListener("click", () => {
        const keyword = inputKeyword.value.trim().toLowerCase();
        if (!keyword) {
            alert(translations[currentLang]["alert.enter_keyword"]);
            return;
        }

        // Limpiar estado
        gridIdeas.innerHTML = `
            <div class="spinner-container" style="text-align: center; padding: 40px 0; width: 100%;">
                <div class="spinner" style="width: 50px; height: 50px; border: 4px solid rgba(255, 255, 255, 0.05); border-top: 4px solid var(--primary); border-radius: 50%; margin: 0 auto 16px auto; animation: spin 1s linear infinite; box-shadow: 0 0 15px var(--primary-glow);"></div>
                <div class="loading-text" style="color: var(--text-muted); font-size: 15px; font-weight: 500;">${currentLang === "es" ? "🤖 Agente local evaluando ideas..." : "🤖 Local agent evaluating domain ideas..."}</div>
            </div>
        `;

        setTimeout(() => {
            const suggestions = generarIdeasLocales(keyword, selectStyle.value, selectTld.value);
            renderizarIdeasSugeridas(suggestions);
        }, 800);
    });

    // Enter en input ejecuta la búsqueda
    inputKeyword.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            btnGenerate.click();
        }
    });
}

// Generador Heurístico Local
function generarIdeasLocales(keyword, style, tld) {
    const extensions = tld === "all" ? ["ai", "io", "com", "co", "net"] : [tld];
    const suggestions = [];

    // Patrones de generación según estilo de marca
    const patrones = {
        ai: [
            { pre: "", suf: "-ai" },
            { pre: "", suf: "bot" },
            { pre: "open", suf: "" },
            { pre: "", suf: "intel" },
            { pre: "mind", suf: "" },
            { pre: "", suf: "brain" }
        ],
        corp: [
            { pre: "galaxy", suf: "" },
            { pre: "", suf: "corp" },
            { pre: "neo", suf: "" },
            { pre: "", suf: "hub" },
            { pre: "nexus", suf: "" },
            { pre: "", suf: "global" }
        ],
        short: [
            { pre: "yi", suf: "" },
            { pre: "", suf: "yi" },
            { pre: "", suf: "n3o" },
            { pre: "", suf: "x" },
            { pre: "", suf: "go" },
            { pre: "", suf: "v" }
        ],
        geek: [
            { pre: "tech", suf: "" },
            { pre: "", suf: "labs" },
            { pre: "", suf: "dev" },
            { pre: "cyber", suf: "" },
            { pre: "", suf: "geek" },
            { pre: "hyper", suf: "" }
        ]
    };

    const esquemas = patrones[style] || patrones.ai;

    esquemas.forEach((esq, idx) => {
        const ext = extensions[idx % extensions.length];
        const name = `${esq.pre}${keyword}${esq.suf}.${ext}`;
        const cleanName = name.replace(/-+/g, "-"); // Evitar guiones dobles
        
        // Evaluar con heurísticas del Agente IA local
        const rating = evaluarDominioHeuristicamente(cleanName);
        suggestions.push({
            domain: cleanName,
            score: rating.score,
            metrics: rating.metrics
        });
    });

    // Ordenar de mayor score a menor
    return suggestions.sort((a, b) => b.score - a.score);
}

// Algoritmo Evaluador Heurístico del Agente Autónomo (Local Client AI)
function evaluarDominioHeuristicamente(domain) {
    const parts = domain.split('.');
    const name = parts[0];
    const ext = parts[1] || "";
    
    // 1. Métrica de Longitud (Ideal: corto, castigo por más de 12 letras)
    let lenScore = 10.0;
    if (name.length <= 4) lenScore = 10.0;
    else if (name.length <= 8) lenScore = 9.0;
    else if (name.length <= 12) lenScore = 7.5;
    else lenScore = Math.max(3.0, 10.0 - (name.length - 8) * 0.8);

    // 2. Métrica de Pronunciabilidad (Ratio vocal-consonante ideal 40-60%)
    let pronScore = 8.0;
    const vowels = (name.match(/[aeiou]/g) || []).length;
    const consonants = name.length - vowels;
    
    if (name.length > 0) {
        const ratio = vowels / name.length;
        if (ratio >= 0.35 && ratio <= 0.55) {
            pronScore = 9.8; // Excelente
        } else if (ratio >= 0.20 && ratio <= 0.70) {
            pronScore = 8.5; // Aceptable
        } else {
            pronScore = 5.0; // Difícil pronunciar
        }
    }
    // Castigo por consonantes consecutivas repetidas (ej: ccc, trr)
    if (/[bcdfghjklmnpqrstvwxyz]{3,}/i.test(name)) {
        pronScore = Math.max(2.0, pronScore - 3.5);
    }

    // 3. Métrica de Memorabilidad (Depende de prefijos/sufijos potentes)
    let memScore = 7.0;
    const words = ["open", "bot", "neo", "intel", "mind", "galaxy", "yi", "tech", "dev", "n3o"];
    let matchWord = false;
    words.forEach(w => {
        if (name.includes(w)) matchWord = true;
    });
    
    if (matchWord) memScore = 9.5;
    if (name.length <= 5) memScore = Math.max(memScore, 9.0); // Nombres muy cortos son memorables
    if (name.includes("-")) memScore = Math.max(3.0, memScore - 1.5); // Guiones reducen memorabilidad

    // 4. Métrica de Extensión TLD Fit
    let tldScore = 6.0;
    if (ext === "ai") {
        tldScore = name.includes("bot") || name.includes("intel") || name.includes("mind") ? 10.0 : 9.5;
    } else if (ext === "com") {
        tldScore = 9.8; // Rey comercial
    } else if (ext === "io") {
        tldScore = name.includes("tech") || name.includes("dev") || name.includes("labs") ? 9.8 : 8.8;
    } else if (ext === "co") {
        tldScore = 8.0;
    } else if (ext === "net") {
        tldScore = 7.5;
    }

    // Promedio Ponderado
    const score = parseFloat(((pronScore * 0.3) + (memScore * 0.35) + (lenScore * 0.15) + (tldScore * 0.2)).toFixed(1));

    return {
        score: score,
        metrics: {
            pron: parseFloat(pronScore.toFixed(1)),
            mem: parseFloat(memScore.toFixed(1)),
            len: parseFloat(lenScore.toFixed(1)),
            tld: parseFloat(tldScore.toFixed(1))
        }
    };
}

// Renderizar Tarjetas de Ideas
function renderizarIdeasSugeridas(ideas) {
    const grid = document.getElementById("generator-ideas-grid");
    grid.innerHTML = "";

    ideas.forEach(idea => {
        const isHighlyRec = idea.score >= 8.5;
        const card = document.createElement("div");
        card.className = `idea-card ${isHighlyRec ? 'highly-recommended' : ''}`;
        
        // Estructura de métricas
        const ratingTitle = translations[currentLang]["msg.technical_score"];
        const btnSaveLabel = currentLang === "es" ? "Guardar Idea" : "Save Idea";
        const btnCheckLabel = currentLang === "es" ? "Comprobar DNS" : "Check DNS";
        
        // Comprobar si ya está guardado
        const isSaved = savedDomains.some(d => d.domain === idea.domain);
        const savedClass = isSaved ? 'action-save' : '';
        const savedIcon = isSaved ? 'fa-bookmark' : 'fa-bookmark-slash';
        const savedText = isSaved ? (currentLang === "es" ? "Guardado" : "Saved") : btnSaveLabel;

        let badgeHtml = "";
        if (isHighlyRec) {
            badgeHtml = `<span class="agent-badge"><i class="fa-solid fa-shield-halved"></i> ${translations[currentLang]["msg.recommend"]}</span>`;
        }

        card.innerHTML = `
            <div class="idea-top">
                <span class="idea-domain-title">${idea.domain}</span>
                <div class="idea-badges">
                    ${badgeHtml}
                    <span class="dns-status-badge" id="dns-badge-${idea.domain.replace('.', '_')}">${translations[currentLang]["status.checking"]}</span>
                </div>
            </div>
            
            <div class="agent-analysis-panel">
                <div class="analysis-header">
                    <span>${ratingTitle}</span>
                    <strong>${idea.score} / 10</strong>
                </div>
                <div class="analysis-metrics">
                    <div class="metric-item">
                        <div class="metric-meta">
                            <span>${translations[currentLang]["msg.metric_pron"]}</span>
                            <strong>${idea.metrics.pron}</strong>
                        </div>
                        <div class="metric-bar"><div class="metric-bar-fill" style="width: ${idea.metrics.pron * 10}%"></div></div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-meta">
                            <span>${translations[currentLang]["msg.metric_mem"]}</span>
                            <strong>${idea.metrics.mem}</strong>
                        </div>
                        <div class="metric-bar"><div class="metric-bar-fill" style="width: ${idea.metrics.mem * 10}%"></div></div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-meta">
                            <span>${translations[currentLang]["msg.metric_len"]}</span>
                            <strong>${idea.metrics.len}</strong>
                        </div>
                        <div class="metric-bar"><div class="metric-bar-fill" style="width: ${idea.metrics.len * 10}%"></div></div>
                    </div>
                    <div class="metric-item">
                        <div class="metric-meta">
                            <span>${translations[currentLang]["msg.metric_tld"]}</span>
                            <strong>${idea.metrics.tld}</strong>
                        </div>
                        <div class="metric-bar"><div class="metric-bar-fill" style="width: ${idea.metrics.tld * 10}%"></div></div>
                    </div>
                </div>
            </div>

            <div class="idea-actions">
                <button class="card-btn action-check" data-domain="${idea.domain}">
                    <i class="fa-solid fa-magnifying-glass"></i> <span>${btnCheckLabel}</span>
                </button>
                <button class="card-btn action-save ${savedClass}" data-domain="${idea.domain}" data-score="${idea.score}">
                    <i class="fa-solid ${savedIcon}"></i> <span>${savedText}</span>
                </button>
            </div>
        `;

        grid.appendChild(card);

        // Disparar comprobación DNS rápida client-side vía DoH inmediata en segundo plano para cada recomendación
        verificarDNSClientSide(idea.domain, `dns-badge-${idea.domain.replace('.', '_')}`);
    });

    // Enlazar eventos de botones
    grid.querySelectorAll(".action-check").forEach(btn => {
        btn.addEventListener("click", () => {
            const dom = btn.getAttribute("data-domain");
            const badgeId = `dns-badge-${dom.replace('.', '_')}`;
            verificarDNSClientSide(dom, badgeId, true);
        });
    });

    grid.querySelectorAll(".action-save").forEach(btn => {
        btn.addEventListener("click", () => {
            const dom = btn.getAttribute("data-domain");
            const score = btn.getAttribute("data-score");
            guardarDominioEnMemoria(dom, score, btn);
        });
    });
}

// ==========================================================================
// 7. Motor DNS over HTTPS (DoH) Client-Side sin dependencias externas
// ==========================================================================
async function verificarDNSClientSide(domain, badgeId, manualTrigger = false) {
    const badge = document.getElementById(badgeId);
    if (!badge) return;

    if (manualTrigger) {
        badge.className = "dns-status-badge checking";
        badge.innerText = translations[currentLang]["status.checking"];
    }

    try {
        // Consultar API DoH de Cloudflare (Formato JSON de DNS seguro)
        const response = await fetch(`https://cloudflare-dns.com/dns-query?name=${encodeURIComponent(domain)}&type=A`, {
            headers: { 'accept': 'application/dns-json' }
        });
        
        if (!response.ok) throw new Error("DoH Failed");
        const json = await response.json();
        
        // Status 3 es NXDOMAIN (No existe registro en DNS, posible disponibilidad)
        // Status 0 es NOERROR. Si tiene Answer, está comprado. Si no, podría estar libre o apuntado a NS raros.
        const hasRecords = json.Answer && json.Answer.length > 0;
        
        if (hasRecords) {
            badge.className = "dns-status-badge taken";
            badge.innerText = translations[currentLang]["status.taken"];
        } else {
            badge.className = "dns-status-badge available";
            badge.innerText = translations[currentLang]["status.available"];
        }
    } catch (err) {
        // En caso de que falle Cloudflare, reintentamos con Google DoH
        try {
            const resGoogle = await fetch(`https://dns.google/resolve?name=${encodeURIComponent(domain)}&type=A`);
            if (!resGoogle.ok) throw new Error();
            const jsonG = await resGoogle.json();
            const recordsG = jsonG.Answer && jsonG.Answer.length > 0;
            
            if (recordsG) {
                badge.className = "dns-status-badge taken";
                badge.innerText = translations[currentLang]["status.taken"];
            } else {
                badge.className = "dns-status-badge available";
                badge.innerText = translations[currentLang]["status.available"];
            }
        } catch (e) {
            badge.className = "dns-status-badge";
            badge.innerText = currentLang === "es" ? "Desconocido" : "Unknown";
        }
    }
}

// ==========================================================================
// 8. Gestión de Memoria Local (LocalStorage & 10 Limit System)
// ==========================================================================
function guardarDominioEnMemoria(domain, score, buttonElem) {
    // Comprobar si ya está guardado
    if (savedDomains.some(d => d.domain === domain)) {
        // Remover de guardados si se da de baja
        savedDomains = savedDomains.filter(d => d.domain !== domain);
        localStorage.setItem("openfind_saved", JSON.stringify(savedDomains));
        
        buttonElem.classList.remove("action-save");
        buttonElem.querySelector("i").className = "fa-solid fa-bookmark-slash";
        buttonElem.querySelector("span").innerText = currentLang === "es" ? "Guardar Idea" : "Save Idea";
        
        renderizarGuardados();
        actualizarContadoresMemoria();
        return;
    }

    // Comprobar límite estricto de 10 elementos
    if (savedDomains.length >= 10) {
        if (autoCleanupEnabled) {
            // Autolimpieza (Opción B activa): elimina el más viejo (índice 0)
            savedDomains.shift();
            
            // Insertar el nuevo
            savedDomains.push({ domain, score: parseFloat(score) });
            localStorage.setItem("openfind_saved", JSON.stringify(savedDomains));
            
            buttonElem.classList.add("action-save");
            buttonElem.querySelector("i").className = "fa-solid fa-bookmark";
            buttonElem.querySelector("span").innerText = currentLang === "es" ? "Guardado" : "Saved";
            
            renderizarGuardados();
            actualizarContadoresMemoria();
        } else {
            // Guardar en cola pendiente y disparar el diálogo A/B modal animado
            pendingSaveDomain = { domain, score: parseFloat(score), btn: buttonElem };
            abrirModalAlmacenamiento();
        }
    } else {
        // Guardar normalmente
        savedDomains.push({ domain, score: parseFloat(score) });
        localStorage.setItem("openfind_saved", JSON.stringify(savedDomains));
        
        buttonElem.classList.add("action-save");
        buttonElem.querySelector("i").className = "fa-solid fa-bookmark";
        buttonElem.querySelector("span").innerText = currentLang === "es" ? "Guardado" : "Saved";
        
        renderizarGuardados();
        actualizarContadoresMemoria();
    }
}

function renderizarGuardados() {
    const listElem = document.getElementById("saved-domains-list");
    const clearBtn = document.getElementById("btn-clear-saved");
    
    if (savedDomains.length === 0) {
        listElem.innerHTML = `
            <div class="empty-saved-state">
                <p data-i18n="gen.empty_saved">${translations[currentLang]["gen.empty_saved"]}</p>
            </div>
        `;
        clearBtn.classList.add("disabled");
        clearBtn.disabled = true;
        return;
    }

    listElem.innerHTML = "";
    clearBtn.classList.remove("disabled");
    clearBtn.disabled = false;

    savedDomains.forEach(item => {
        const tag = document.createElement("div");
        tag.className = "saved-tag";
        tag.innerHTML = `
            <span>${item.domain}</span>
            <small style="color: var(--primary); font-size: 11px; font-weight:700;">Score: ${item.score}</small>
            <button class="delete-saved-btn" data-domain="${item.domain}">
                <i class="fa-solid fa-xmark"></i>
            </button>
        `;
        listElem.appendChild(tag);
    });

    // Eventos de borrado individual
    listElem.querySelectorAll(".delete-saved-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            const dom = btn.getAttribute("data-domain");
            eliminarDominioFavorito(dom);
        });
    });
}

function eliminarDominioFavorito(domain) {
    savedDomains = savedDomains.filter(d => d.domain !== domain);
    localStorage.setItem("openfind_saved", JSON.stringify(savedDomains));
    
    // Desmarcar botón en la rejilla si es visible
    document.querySelectorAll(`.action-save[data-domain="${domain}"]`).forEach(btn => {
        btn.classList.remove("action-save");
        btn.querySelector("i").className = "fa-solid fa-bookmark-slash";
        btn.querySelector("span").innerText = currentLang === "es" ? "Guardar Idea" : "Save Idea";
    });

    renderizarGuardados();
    actualizarContadoresMemoria();
}

function actualizarContadoresMemoria() {
    const count = savedDomains.length;
    document.getElementById("saved-count").innerText = count;
    document.getElementById("saved-count-2").innerText = count;
}

// Limpiar favoritos completo
document.getElementById("btn-clear-saved").addEventListener("click", () => {
    savedDomains = [];
    localStorage.removeItem("openfind_saved");
    
    // Desmarcar todos los botones visuales
    document.querySelectorAll(".action-save").forEach(btn => {
        btn.classList.remove("action-save");
        btn.querySelector("i").className = "fa-solid fa-bookmark-slash";
        btn.querySelector("span").innerText = currentLang === "es" ? "Guardar Idea" : "Save Idea";
    });

    renderizarGuardados();
    actualizarContadoresMemoria();
});

// ==========================================================================
// 9. Diálogo Animado Almacenamiento Límite (Custom A/B Modal Dialog)
// ==========================================================================
function inicializarModalAlmacenamiento() {
    const modal = document.getElementById("storage-modal-overlay");
    const optionA = document.getElementById("modal-option-a");
    const optionB = document.getElementById("modal-option-b");
    const btnConfirm = document.getElementById("modal-btn-confirm");
    const btnCancel = document.getElementById("modal-btn-cancel");
    
    let selectedOption = null;

    optionA.addEventListener("click", () => {
        optionA.classList.add("selected");
        optionB.classList.remove("selected");
        selectedOption = "A";
        btnConfirm.classList.remove("disabled");
        btnConfirm.disabled = false;
    });

    optionB.addEventListener("click", () => {
        optionB.classList.add("selected");
        optionA.classList.remove("selected");
        selectedOption = "B";
        btnConfirm.classList.remove("disabled");
        btnConfirm.disabled = false;
    });

    btnCancel.addEventListener("click", () => {
        cerrarModalAlmacenamiento();
    });

    btnConfirm.addEventListener("click", () => {
        if (!selectedOption) return;

        if (selectedOption === "A") {
            // Opción A: Limpiar todo
            savedDomains = [];
            localStorage.removeItem("openfind_saved");
            
            // Desmarcar botones antiguos
            document.querySelectorAll(".action-save").forEach(btn => {
                btn.classList.remove("action-save");
                btn.querySelector("i").className = "fa-solid fa-bookmark-slash";
                btn.querySelector("span").innerText = currentLang === "es" ? "Guardar Idea" : "Save Idea";
            });

            // Guardar el nuevo dominio pendiente
            if (pendingSaveDomain) {
                savedDomains.push({ domain: pendingSaveDomain.domain, score: pendingSaveDomain.score });
                localStorage.setItem("openfind_saved", JSON.stringify(savedDomains));
                
                if (pendingSaveDomain.btn) {
                    pendingSaveDomain.btn.classList.add("action-save");
                    pendingSaveDomain.btn.querySelector("i").className = "fa-solid fa-bookmark";
                    pendingSaveDomain.btn.querySelector("span").innerText = currentLang === "es" ? "Guardado" : "Saved";
                }
            }
        } else if (selectedOption === "B") {
            // Opción B: Activar Autolimpieza Automática
            autoCleanupEnabled = true;
            localStorage.setItem("openfind_autocleanup", "true");
            
            // Eliminar el más antiguo
            savedDomains.shift();
            
            // Guardar el nuevo dominio
            if (pendingSaveDomain) {
                savedDomains.push({ domain: pendingSaveDomain.domain, score: pendingSaveDomain.score });
                localStorage.setItem("openfind_saved", JSON.stringify(savedDomains));
                
                if (pendingSaveDomain.btn) {
                    pendingSaveDomain.btn.classList.add("action-save");
                    pendingSaveDomain.btn.querySelector("i").className = "fa-solid fa-bookmark";
                    pendingSaveDomain.btn.querySelector("span").innerText = currentLang === "es" ? "Guardado" : "Saved";
                }
            }
        }

        renderizarGuardados();
        actualizarContadoresMemoria();
        cerrarModalAlmacenamiento();
    });
}

function abrirModalAlmacenamiento() {
    const modal = document.getElementById("storage-modal-overlay");
    modal.classList.add("show");
}

function cerrarModalAlmacenamiento() {
    const modal = document.getElementById("storage-modal-overlay");
    modal.classList.remove("show");
    
    // Resetear selección
    document.getElementById("modal-option-a").classList.remove("selected");
    document.getElementById("modal-option-b").classList.remove("selected");
    const btnConfirm = document.getElementById("modal-btn-confirm");
    btnConfirm.classList.add("disabled");
    btnConfirm.disabled = true;
    
    pendingSaveDomain = null;
}

// ==========================================================================
// 10. Escáner Masivo DNS en Paralelo (Parallel DoH Scanner System)
// ==========================================================================
let bulkScannerData = []; // Para reportes PDF/TXT

function inicializarEscanerMasivo() {
    const startBtn = document.getElementById("start-bulk-btn");
    const textarea = document.getElementById("bulk-textarea");
    const dnsProvider = document.getElementById("scan-dns-provider");
    const resultsGrid = document.getElementById("bulk-results-grid");
    const progressPanel = document.getElementById("bulk-progress-panel");
    const downloadBtn = document.getElementById("download-results-btn");
    const downloadPdfBtn = document.getElementById("download-pdf-btn");

    startBtn.addEventListener("click", async () => {
        const text = textarea.value.trim();
        if (!text) {
            alert(translations[currentLang]["alert.no_domains"]);
            return;
        }

        const lines = text.split(/[\n,]+/);
        const rawDomains = [];

        lines.forEach(line => {
            let clean = line.trim();
            if (!clean || clean.startsWith("#")) return;

            let dom = clean.toLowerCase();
            dom = dom.replace(/^(https?://)?(www\.)?/, "");
            dom = dom.split("/")[0];

            if (dom.includes(".") && dom.length >= 4) {
                rawDomains.push(dom);
            }
        });

        // Eliminar duplicados
        const domains = [...new Set(rawDomains)];

        if (domains.length === 0) {
            alert(currentLang === "es" ? "No se encontraron dominios con formato válido (ej: dominio.com)." : "No domains found with valid format (e.g. domain.com).");
            return;
        }

        // Reset
        resultsGrid.innerHTML = "";
        bulkScannerData = [];
        progressPanel.style.display = "block";
        downloadBtn.classList.add("disabled");
        downloadBtn.disabled = true;
        downloadPdfBtn.classList.add("disabled");
        downloadPdfBtn.disabled = true;
        startBtn.disabled = true;
        startBtn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> ${translations[currentLang]["alert.scanning"]}`;

        let counts = { disponible: 0, comprado: 0 };
        const total = domains.length;
        let processed = 0;

        actualizarProgresoMasivo(0, total, counts);

        // Procesar en paralelo con lote controlado de concurrencia de 5
        const limitConcurrencia = 5;
        const cola = [...domains];
        const promesasActivas = [];

        const procesarDominio = async (dom) => {
            try {
                const isCloudflare = dnsProvider.value === "cloudflare";
                const url = isCloudflare ?
                    `https://cloudflare-dns.com/dns-query?name=${encodeURIComponent(dom)}&type=A` :
                    `https://dns.google/resolve?name=${encodeURIComponent(dom)}&type=A`;
                
                const response = await fetch(url, {
                    headers: isCloudflare ? { 'accept': 'application/dns-json' } : {}
                });

                if (!response.ok) throw new Error();
                const json = await response.json();
                
                const isTaken = json.Answer && json.Answer.length > 0;
                const status = isTaken ? "comprado" : "disponible";
                
                counts[status]++;
                processed++;

                bulkScannerData.push({
                    domain: dom,
                    estado: isTaken ? "OCUPADO" : "DISPONIBLE",
                    metodo: isCloudflare ? "Cloudflare Secure DoH" : "Google Public DoH"
                });

                inyectarTarjetaMiniBulk(dom, status, isCloudflare ? "Cloudflare DoH" : "Google DoH");
                actualizarProgresoMasivo(processed, total, counts);
            } catch (err) {
                // Fallback a disponible ante fallos de red
                counts.disponible++;
                processed++;
                bulkScannerData.push({
                    domain: dom,
                    estado: "DNS LIBRE",
                    metodo: "Falla de consulta (DoH)"
                });
                inyectarTarjetaMiniBulk(dom, "disponible", "Falla de red (Libre)");
                actualizarProgresoMasivo(processed, total, counts);
            }
        };

        while (cola.length > 0 || promesasActivas.length > 0) {
            while (promesasActivas.length < limitConcurrencia && cola.length > 0) {
                const siguienteDom = cola.shift();
                const promesa = procesarDominio(siguienteDom).then(() => {
                    promesasActivas.splice(promesasActivas.indexOf(promesa), 1);
                });
                promesasActivas.push(promesa);
            }
            await Promise.race(promesasActivas);
        }

        // Finalizado
        startBtn.disabled = false;
        startBtn.innerHTML = `<i class="fa-solid fa-play"></i> ${translations[currentLang]["fast.start_btn"]}`;
        
        downloadBtn.classList.remove("disabled");
        downloadBtn.disabled = false;
        downloadPdfBtn.classList.remove("disabled");
        downloadPdfBtn.disabled = false;
    });

    downloadBtn.addEventListener("click", () => {
        if (bulkScannerData.length === 0) return;
        descargarReporteTxt();
    });

    downloadPdfBtn.addEventListener("click", () => {
        if (bulkScannerData.length === 0) return;
        descargarReportePdf();
    });
}

function inyectarTarjetaMiniBulk(domain, status, method) {
    const resultsGrid = document.getElementById("bulk-results-grid");
    
    const emptyState = resultsGrid.querySelector(".empty-state");
    if (emptyState) emptyState.remove();

    const isAvail = status === "disponible";
    const cardClass = isAvail ? "available" : "taken";
    const badgeClass = isAvail ? "available" : "taken";
    const label = isAvail ? (currentLang === "es" ? "DNS Libre" : "DNS Free") : (currentLang === "es" ? "Ocupado" : "Taken");

    const miniCard = document.createElement("div");
    miniCard.className = `bulk-mini-card ${cardClass}`;
    miniCard.innerHTML = `
        <div class="mini-left">
            <span class="mini-domain" title="${domain}">${domain}</span>
            <div style="font-size: 11px; color: var(--text-muted); margin-top: 4px; font-family: var(--font-mono)">
                ${method}
            </div>
        </div>
        <span class="mini-badge ${badgeClass}">${label}</span>
    `;

    resultsGrid.appendChild(miniCard);
}

function actualizarProgresoMasivo(processed, total, counts) {
    const progressFill = document.getElementById("progress-bar-fill");
    const progressText = document.getElementById("progress-text");
    const progressPerc = document.getElementById("progress-percentage");

    document.getElementById("stat-avail-count").innerText = counts.disponible;
    document.getElementById("stat-taken-count").innerText = counts.comprado;

    const percentage = total > 0 ? Math.round((processed / total) * 100) : 0;
    
    progressFill.style.width = `${percentage}%`;
    progressPerc.innerText = `${percentage}%`;
    
    if (processed === total && total > 0) {
        progressText.innerHTML = translations[currentLang]["alert.finished"].replace("{processed}", processed).replace("{total}", total);
    } else {
        progressText.innerText = translations[currentLang]["alert.progress"].replace("{processed}", processed).replace("{total}", total);
    }
}

// ==========================================================================
// 11. Reportes Exportables Client-side (TXT & PDF con jsPDF)
// ==========================================================================
function descargarReporteTxt() {
    let contenido = `====================================================\n`;
    contenido += `      REPORTE DE ESCANEO DNS - OPENFIND AI 🔎      \n`;
    contenido += `====================================================\n\n`;
    contenido += `Fecha del Escaneo: ${new Date().toLocaleString()}\n`;
    contenido += `Total Analizados: ${bulkScannerData.length}\n\n`;
    contenido += `RESULTADOS DETALLADOS:\n`;
    contenido += `----------------------------------------------------\n`;
    
    bulkScannerData.forEach((row, idx) => {
        contenido += `${(idx + 1).toString().padStart(3, '0')}. DOMINIO: ${row.domain.padEnd(28)} | ESTADO: ${row.estado.padEnd(12)} | MÉTODO: ${row.metodo}\n`;
    });
    
    contenido += `\n====================================================\n`;
    contenido += `Desarrollado con amor por NeoTurcios - hola@neopunto.com\n`;
    contenido += `====================================================\n`;

    const blob = new Blob([contenido], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `reporte_dns_openfind_${Date.now()}.txt`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
}

function descargarReportePdf() {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF('p', 'pt', 'a4');
    
    const margin = 40;
    let y = 50;
    const width = 595;
    
    // Colores corporativos
    const darkSlate = [13, 20, 38];
    const neonGreen = [16, 185, 129];
    const neonRed = [239, 68, 68];
    const neutralGray = [148, 163, 184];
    const lightGray = [248, 250, 252];
    
    // Header Bar
    doc.setFillColor(...darkSlate);
    doc.rect(margin, y, width - (margin * 2), 55, 'F');
    
    doc.setTextColor(255, 255, 255);
    doc.setFont("Helvetica", "bold");
    doc.setFontSize(18);
    doc.text("OPENFIND AI - REPORTE DNS", margin + 20, y + 34);
    
    y += 55;
    doc.setFillColor(...neonGreen);
    doc.rect(margin, y, width - (margin * 2), 3, 'F');
    
    y += 35;
    
    doc.setTextColor(15, 23, 42);
    doc.setFont("Helvetica", "bold");
    doc.setFontSize(14);
    doc.text(currentLang === "es" ? "Escaneo Masivo de Disponibilidad DNS" : "Bulk DNS Availability Scan", margin, y);
    
    y += 18;
    doc.setFont("Helvetica", "normal");
    doc.setFontSize(9);
    doc.setTextColor(100, 116, 139);
    doc.text(`${currentLang === "es" ? "Fecha del escaneo" : "Scan Date"}: ${new Date().toLocaleString()}`, margin, y);
    
    y += 25;
    
    // Tarjetas resumen
    const disponibles = bulkScannerData.filter(d => d.estado === 'DISPONIBLE').length;
    const ocupados = bulkScannerData.filter(d => d.estado === 'OCUPADO').length;
    
    // Disponibles
    doc.setFillColor(240, 253, 244); 
    doc.setDrawColor(...neonGreen);
    doc.roundedRect(margin, y, 235, 42, 4, 4, 'FD');
    doc.setTextColor(...neonGreen);
    doc.setFont("Helvetica", "bold");
    doc.setFontSize(14);
    doc.text(`${disponibles}`, margin + 15, y + 20);
    doc.setFont("Helvetica", "normal");
    doc.setFontSize(8.5);
    doc.setTextColor(22, 101, 52);
    doc.text(currentLang === "es" ? "Dominios sin registros (Disponibles)" : "Domains without records (Available)", margin + 15, y + 32);
    
    // Ocupados
    doc.setFillColor(254, 242, 242); 
    doc.setDrawColor(...neonRed);
    doc.roundedRect(margin + 260, y, 255, 42, 4, 4, 'FD');
    doc.setTextColor(...neonRed);
    doc.setFont("Helvetica", "bold");
    doc.setFontSize(14);
    doc.text(`${ocupados}`, margin + 275, y + 20);
    doc.setFont("Helvetica", "normal");
    doc.setFontSize(8.5);
    doc.setTextColor(153, 27, 27);
    doc.text(currentLang === "es" ? "Dominios con IP activa (Registrados)" : "Domains with active IP (Registered)", margin + 275, y + 32);
    
    y += 65;
    
    // Detalle de tabla
    doc.setFont("Helvetica", "bold");
    doc.setFontSize(10);
    doc.setTextColor(15, 23, 42);
    doc.text(currentLang === "es" ? "Listado Completo de Dominios" : "Complete Domain List", margin, y);
    
    y += 15;
    
    // Cabecera Tabla
    doc.setFillColor(241, 245, 249);
    doc.rect(margin, y, width - (margin * 2), 22, 'F');
    
    doc.setTextColor(71, 85, 105);
    doc.setFontSize(8.5);
    doc.text("#", margin + 10, y + 14);
    doc.text("Dominio", margin + 40, y + 14);
    doc.text("Estado DNS", margin + 240, y + 14);
    doc.text("Servidor de consulta", margin + 370, y + 14);
    
    y += 22;
    doc.setFont("Helvetica", "normal");
    
    bulkScannerData.forEach((row, idx) => {
        if (y > 750) {
            doc.addPage();
            y = 50;
            // Dibujar cabecera resumida
            doc.setFillColor(...darkSlate);
            doc.rect(margin, y, width - (margin * 2), 30, 'F');
            doc.setTextColor(255, 255, 255);
            doc.setFont("Helvetica", "bold");
            doc.text("OPENFIND AI", margin + 15, y + 18);
            y += 40;
        }
        
        // Fila alternada de color
        if (idx % 2 === 1) {
            doc.setFillColor(248, 250, 252);
            doc.rect(margin, y, width - (margin * 2), 20, 'F');
        }
        
        doc.setTextColor(15, 23, 42);
        doc.setFont("Helvetica", "normal");
        doc.text((idx + 1).toString(), margin + 10, y + 13);
        doc.text(row.domain, margin + 40, y + 13);
        
        const isAv = row.estado === "DISPONIBLE";
        doc.setTextColor(isAv ? 22 : 153, isAv ? 101 : 27, isAv ? 52 : 27);
        doc.setFont("Helvetica", "bold");
        doc.text(row.estado, margin + 240, y + 13);
        
        doc.setTextColor(100, 116, 139);
        doc.setFont("Helvetica", "normal");
        doc.text(row.metodo, margin + 370, y + 13);
        
        y += 20;
    });
    
    doc.save(`reporte_dns_openfind_${Date.now()}.pdf`);
}
