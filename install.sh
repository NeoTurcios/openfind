#!/bin/bash

# Colores para la terminal
VERDE="\033[1;92m"
ROJO="\033[1;91m"
AMARILLO="\033[1;93m"
CIAN="\033[1;96m"
BLANCO="\033[1;97m"
FIN="\033[0m"

clear
echo -e "${CIAN}╔═══════════════════════════════════════════════════════════╗"
echo -e "║     🚀  INSTALADOR AUTOMÁTICO DE BUSCARDOM EN TERMUX  🚀   ║"
echo -e "╚═══════════════════════════════════════════════════════════╝${FIN}"
echo ""

echo -e "${AMARILLO}[+] 1. Actualizando paquetes del sistema en Termux...${FIN}"
apt update && apt upgrade -y

echo -e "\n${AMARILLO}[+] 2. Instalando dependencias básicas (Python)...${FIN}"
# Instala python, dnsutils para soporte DNS si es necesario, y git
pkg install python dnsutils git -y

echo -e "\n${AMARILLO}[+] 3. Configurando permisos del script...${FIN}"
chmod +x buscardom.py

# Crear un acceso directo/alias fácil de ejecutar en Termux
echo -e "\n${AMARILLO}[+] 4. Creando acceso rápido (comando 'buscardom')...${FIN}"
if [ -d "$PREFIX/bin" ]; then
    cp buscardom.py $PREFIX/bin/buscardom
    chmod +x $PREFIX/bin/buscardom
    echo -e "${VERDE}✔ ¡Acceso rápido instalado! Ahora puedes escribir 'buscardom' desde cualquier carpeta para iniciar.${FIN}"
else
    echo -e "${AMARILLO}⚠ Entorno diferente a Termux estándar. Permisos del script actualizados en su carpeta local.${FIN}"
fi

echo -e "\n${VERDE}================═══════════════════════════════════════════${FIN}"
echo -e "   ${BLANCO}¡INSTALACIÓN COMPLETADA CON ÉXITO! 🎉${FIN}"
echo -e "${VERDE}================═══════════════════════════════════════════${FIN}"
echo -e "${BLANCO}Para ejecutar el buscador ahora, usa:${FIN}"
echo -e "  ${CIAN}./buscardom.py${FIN}"
echo ""
echo -e "${BLANCO}O simplemente escribe el comando rápido desde cualquier ruta:${FIN}"
echo -e "  ${CIAN}buscardom${FIN}"
echo -e "${VERDE}================═══════════════════════════════════════════${FIN}\n"
