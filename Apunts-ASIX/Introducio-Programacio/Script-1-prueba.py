#!/bin/bash

# Guardem l'hora d'inici
inici=$(date +%s.%N)

# Fem la descàrrega (silenciosa i descartem el fitxer)
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