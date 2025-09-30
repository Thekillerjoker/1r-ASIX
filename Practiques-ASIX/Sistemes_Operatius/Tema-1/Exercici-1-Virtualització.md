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
1. 🌉**Adaptador Pont (Bridge) :**
   *Funciona de la següent manera: si selecciones adaptador pont, VirtualBox connecta la màquina virtual directament a la xarxa real.*
 
  *Per defecte, VirtualBox configura l’adaptador en automàtic **DHCP**, amb la qual cosa:*
- *La màquina virtual demanarà una petició d’IP al servidor DHCP de la xarxa real. Aquest detectarà la màquina virtual com un host real més i li assignarà una IP de la xarxa.Això permet que la màquina virtual accedeixi a internet.*  
- *Es pot comunicar amb les MV connectades al mateix node (Switch, Punt d’accés, etc.) i també amb altres màquines reals.*
