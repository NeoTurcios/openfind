# 🛡️ Política de Privacidad - OpenFind AI

**Última actualización:** 1 de junio de 2026

La presente Política de Privacidad describe de manera clara y transparente cómo **OpenFind AI** (en adelante, "la Aplicación") trata la información de los usuarios que la descargan y utilizan a través de dispositivos móviles Android (incluida su distribución en Google Play Store).

Nuestra prioridad absoluta es el respeto a tu privacidad. Por ello, hemos diseñado **OpenFind AI** bajo la filosofía de **Cero Recopilación de Datos** (Data-Minimization).

---

## 1. Recopilación y Uso de Datos Personales
**OpenFind AI** **NO recopila, almacena, comparte ni vende ningún tipo de información de identificación personal (PII)**.
*   **Sin Cuentas ni Registros:** No necesitas crear un perfil, iniciar sesión o proporcionar correos electrónicos, nombres o números telefónicos para utilizar todas las funciones de la aplicación.
*   **Sin Seguimiento en Segundo Plano:** La aplicación no realiza un seguimiento de tu ubicación, identidad del dispositivo (como IMEI o ID de publicidad) ni de tu historial de navegación general.

---

## 2. Lógica de Consulta y Seguridad de Datos
Cuando buscas la disponibilidad de un dominio de internet en la aplicación:
*   **Conexiones Directas:** Las consultas se realizan directamente desde tu dispositivo móvil a los servidores DNS públicos y a los servidores oficiales de WHOIS (puerto 43) a nivel mundial (WHOIS recursivo).
*   **Sin Servidores Intermedios:** No utilizamos servidores intermediarios ni APIs propietarias para procesar tus consultas de dominios. Toda la transmisión de datos técnicos ocurre en tiempo real y no es registrada en ningún servidor externo bajo nuestro control.

---

## 3. Almacenamiento Local (SharedPreferences)
La aplicación cuenta con una sección de "Biblioteca" (Favoritos e Historial de búsquedas).
*   **Operación 100% Local:** Todo el historial de búsquedas y dominios guardados como favoritos se almacena exclusivamente en la memoria interna de tu dispositivo móvil mediante la tecnología nativa de `SharedPreferences`.
*   **Límite de Historial:** Para proteger tu espacio de almacenamiento y privacidad, la lista está limitada a un máximo de los **10 elementos más recientes**.
*   **Control Total:** Puedes borrar todo el historial y favoritos en cualquier momento presionando el botón "Limpiar" en la aplicación. Asimismo, al desinstalar la aplicación, todos estos datos locales se borrarán permanentemente del dispositivo de forma automática.

---

## 4. Anuncios y Proveedores de Servicios de Terceros
De acuerdo con los términos de nuestra licencia no comercial:
*   **Sin Publicidad (100% Libre de Ads):** No incluimos redes publicitarias de terceros (como Google AdMob, Unity, AppLovin, etc.). No verás banners, anuncios intersticiales o videos promocionales en la aplicación.
*   **Sin Analíticas Invasivas:** No empleamos SDKs de analítica predictiva de comportamiento de usuario que recolecten información en segundo plano.

---

## 5. Permisos Requeridos en el Dispositivo
Para funcionar correctamente, la aplicación solicita exclusivamente los siguientes accesos a nivel de sistema operativo:
1.  **INTERNET (`android.permission.INTERNET`):** Requerido para realizar las consultas técnicas DNS y abrir conexiones por Sockets TCP a las bases de datos mundiales de WHOIS.
2.  **ACCESS_NETWORK_STATE (`android.permission.ACCESS_NETWORK_STATE`):** Utilizado únicamente para comprobar si tu celular cuenta con una conexión activa a internet antes de procesar una búsqueda, evitando errores de red.

---

## 6. Privacidad Infantil (Cumplimiento de la COPPA)
Dado que **OpenFind AI** no recopila ningún tipo de información personal, es completamente segura para menores de edad. No solicitamos edad ni recolectamos datos que puedan comprometer a niños menores de 13 años.

---

## 7. Cambios en esta Política de Privacidad
Nos reservamos el derecho de actualizar esta Política de Privacidad si agregamos nuevas características no invasivas en el futuro. Cualquier cambio relevante se publicará dentro de este documento y será visible en el repositorio oficial de código abierto.

---

## 8. Contacto y Soporte
Si tienes cualquier duda técnica o comentario sobre esta Política de Privacidad o la seguridad de la aplicación, puedes ponerte en contacto con el equipo a través de:
*   **Repositorio Oficial de GitHub:** [https://github.com/NeoTurcios/liberdom](https://github.com/NeoTurcios/liberdom)
*   **Correo de Soporte:** *[Agrega aquí tu correo de contacto de Google Play Console]*
