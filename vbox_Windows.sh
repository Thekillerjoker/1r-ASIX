#!/bin/bash

# Nombre y ubicación de la máquina virtual
VM_NAME="Windows 10"
VM_FOLDER="/home/thekillerjoker1433/VirtualBox VMs/${VM_NAME}.vdi"

# Tamaño de la memoria RAM y el disco duro de la máquina virtual
MEMORY_SIZE="4096"  # 4GB
HDD_SIZE="50000"   # 50GB

# Crear la máquina virtual en VirtualBox
echo "Creando la máquina virtual..."
VBoxManage createvm --name "$VM_NAME" --ostype Windows10_64 --register

# Configurar la memoria RAM de la máquina virtual
echo "Configurando la memoria RAM de la máquina virtual..."
VBoxManage modifyvm "$VM_NAME" --memory "$MEMORY_SIZE"

# Crear y adjuntar el disco duro a la máquina virtual
echo "Creando y adjuntando el disco duro a la máquina virtual..."
VBoxManage createhd --filename "$VM_FOLDER/$VM_NAME.vdi" --size "$HDD_SIZE"
VBoxManage storagectl "$VM_NAME" --name "SATA Controller" --add sata --controller IntelAHCI
VBoxManage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "$VM_FOLDER/$VM_NAME.vdi"
a
# Descargar la imagen ISO de Windows 10
echo "Descargando la imagen ISO de Windows 10..."
ISO_URL="https://software.download.prss.microsoft.com/dbazure/Win10_22H2_Spanish_x64v1.iso?t=31a41a13-7891-4063-ba11-88ea7c3ae076&e=1688923268&h=7e20cb9850db3888fcc28eb76e6dc3d68c21932c27c74b3499b2cc3afe916e45"
ISO_FILE="Win10_22H2_Spanish_x64v1.iso"
wget -O "$ISO_FILE" "$ISO_URL"

# Adjuntar la imagen ISO de Windows 10 a la máquina virtual
echo "Adjuntando la imagen ISO de Windows 10 a la máquina virtual..."
VBoxManage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 1 --device 0 --type dvddrive --medium "$ISO_FILE"

# Configurar el arranque desde la imagen ISO
echo "Configurando el arranque desde la imagen ISO..."
VBoxManage modifyvm "$VM_NAME" --boot1 dvd --boot2 disk --boot3 none --boot4 none

# Iniciar la máquina virtual
echo "Iniciando la máquina virtual..."
VBoxManage startvm "$VM_NAME"
