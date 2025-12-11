#!/bin/bash
#--- Configuració------
#Copia de desti:
DESTI="/home/sergi/Copies-Seguretat/"


#Definir la carpeta que vols copiar:

ORIGEN="$1"
if [ -d "$ORIGEN" ] && [[ ! "$ORIGEN" =~ /$ ]]; then
	ORIGEN="${ORIGEN}/"
fi

#-- Comprovacions directoris: 
if [ -z "$1" ]; then
	echo "Error: Has d'especificar la carpeta d'origen"
	echo "Uso: $0 /ruta/a/la/carpeta/repaldar"
	exit 1
fi 

# Obtenir la data i hora actual per el nombre de La carpeta Copia:
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S" )
NOVA_CARPETA_DESTI="${DESTI}/backup.${TIMESTAMP}"

#Si ja existeix la carpeta de desti:
ANTERIOR_CARPETA_DESTI=$(ls -1d ${DESTI}/backup.* 2>/dev/null | tail -n 1)
# La comanda 'ls -1d' Llista les carpetes pepr nombre , cada una per cada línea.
# tail -n 1 agafa l'ultima, que és la més recent per orden alfabétic i en cas de coincidir per data.

# ----- Comprovar l'existencia de la carpeta d'orgien i en cas contrari crearla:
if [ ! -d "$ORIGEN" ]; then
	echo "ERROR!!: La carpeta d'origen '$ORIGEN'  especificada no existeix o no es válida."
	exit 1
fi
 # Per crear la carpeta de desit si no existeix:
 mkdir -p "$DESTI"

#----- Creacio de copies de següretat incrementals:-----
echo "Inician copia de següretat incremental"
echo " Origen: $ORIGEN"
echo "Desti: $NOVA_CARPETA_DESTI"

if [ -d "$ANTERIOR_CARPETA_DESTI" ]; then
	echo "Copia anterior trobada: $ANTERIOR_CARPETA_DESTI"
	echo "Realitzan copia  incremental amb enllaços"
	rsync -avh --delete --link-dest="$ANTERIOR_CARPETA_DESTI" "$ORIGEN" "$NOVA_CARPETA_DESTI"
else
	echo "No s'ha trobat cap copia de següretat anterior. Realitzant la primera copiade següretat."
	rsync -avh --delete "$ORIGEN" "$NOVA_CARPETA_DESTI"
fi
echo "Copia de següretat completada amb exit."
exit 0


