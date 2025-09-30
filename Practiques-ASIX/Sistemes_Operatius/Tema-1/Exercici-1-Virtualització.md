# 📘 Exercicis de Virtualització:
---
## 🖥️ Exercici 1: VirtualBox - Part teòrica

### Limitacions de les màquines virtuals:
*Explica les limitacions (de hardware màxim) de les màquines virtuals per a la última versió. Ho trobaràs quan crees una màquina virtual nova:*
- **Base Memory:** *És la RAM de la màquina virtual, i està limitada a **1TB (1024GB)***
 
- **Number of CPUs:** *És el número de CPU que vols tenir a la màquina virtual; i aquest en la ultima versiò pot variar.*

*Per defecte el màxim és **32 cpu**, però si tens un processador amb 24 nuclis físics amb la tecnologia Hyper-Threading, VirtualBox permet **48 cpu***

- **Tamany del disc:** *El màxim és **2 TB**.*

---
### 2. Tipus de Xarxa:
*Explica detalladament els tipus de xarxa bridge, NAT i Host-Only.*
#### Adaptador Pont (Bridge) 🌉:
*funciona de la següent manera: Si selecciones adaptador pont, virtualbox connecta la maquina virtual directament a la xarxa real. Per defecte virtualbox configura l’adaptador en autòmatic DHCP, amb la cual cosa la maquina virtual demanara una peticiò d’IP al servidor DHCP de la xarxa real, i aquest detectara la maquina virtual com un host real mes i l’adreçara una IP de la xarxa, el que permatra a la maquina virtual accedir a internet,i comunicar-se amb les MV connectades al mateix node (Switch, Punt d’accés etc.. ), i també a les altres maquines reals.*