#!/bin/bash
# Nombre de la máquina virtual y ubicación del archivo VDI
VM_NAME="Ubuntu22.04.2"
VDI_PATH="/home/	N/VirtualBox VMs/${VM_NAME}.vdi"

# Crear la máquina virtual
VBoxManage createvm --name "$VM_NAME" --ostype "Ubuntu_64" --register

# Configurar la cantidad de memoria RAM
VBoxManage modifyvm "$VM_NAME" --memory 2048

# Configurar el disco duro
VBoxManage createhd --filename "$VDI_PATH" --size 81920

# Asignar el disco duro a la máquina virtual
VBoxManage storagectl "$VM_NAME" --name "SATA Controller" --add sata --controller IntelAhci
VBoxManage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "$VDI_PATH"

# Descargar la imagen ISO de Ubuntu 22.04.2
ISO_URL="https://releases.ubuntu.com/22.04.2/ubuntu-22.04.2-live-server-amd64.iso"
ISO_PATH="/home/thekillerjoker1433/Documents/Isos/ubuntu-22.04.2-live-server-amd64.iso"
wget "$ISO_URL" -O "$ISO_PATH"

# Configurar el controlador de CD/DVD y montar la imagen ISO
VBoxManage storagectl "$VM_NAME" --name "IDE Controller" --add ide
VBoxManage storageattach "$VM_NAME" --storagectl "IDE Controller" --port 0 --device 0 --type dvddrive --medium "$ISO_PATH"

# Iniciar la máquina virtual
VBoxManage startvm "$VM_NAME"

