#!/bin/bash

opc=0
while [ "$opc" -ne 4 ]; do
    clear
    echo "-----------------------------"
    echo "    MENÚ D'ADMINISTRACIÓ"
    echo "-----------------------------"
    echo "1. Mostrar usuaris del sistema"
    echo "2. Mostrar adreça IP local"
    echo "3. Llistar processos actius"
    echo "4. Sortir"
    echo "-----------------------------"
    read -p "Escull una opció [1-4]: " opc

    case $opc in
        1) cat /etc/passwd; read -p "Prem ENTER per continuar..." ;;
        2) hostname -I; read -p "Prem ENTER per continuar..." ;;
        3) ps -e; read -p "Prem ENTER per continuar..." ;;
        4) echo "Sortint...";;
        *) echo "Opció no vàlida"; read -p "Prem ENTER per continuar..." ;;
    esac
done