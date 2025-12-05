#!/bin/bash

# Nombre de descàrregues (pots canviar-ho)
NUM_DESCARREGUES=3

for i in $(seq 1 $NUM_DESCARREGUES); do
    # Guardem l'hora d'inici en segons
    inici=$(date +%s.%N)

    # Fem la descàrrega amb wget i descartem la sortida
    wget -q https://ash-speed.hetzner.com/100MB.bin -O /dev/null

    # Guardem l'hora de finalització
    fi=$(date +%s.%N)

    # Calculem el temps de descàrrega
    temps=$(echo "$fi - $inici" | bc)

    # Data i hora actual
    data=$(date +%Y-%m-%d)
    hora=$(date +%H:%M:%S)

    # Mostrem en el format demanat
    echo "$data,$hora,$temps"

    # Pausa de 10 segons
    sleep 10
done