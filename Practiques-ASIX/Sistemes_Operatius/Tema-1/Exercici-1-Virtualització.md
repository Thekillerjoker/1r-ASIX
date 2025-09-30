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
### 1. Tipus de Xarxa:
*Explica detalladament els tipus de xarxa bridge, NAT i Host-Only.*
1. 🌉**Adaptador Pont (Bridge) :**
   *Funciona de la següent manera: si selecciones adaptador pont, VirtualBox connecta la màquina virtual directament a la xarxa real.*
 
  *Per defecte, VirtualBox configura l’adaptador en automàtic **DHCP**, amb la qual cosa:*
- *La màquina virtual demanarà una petició d’IP al servidor DHCP de la xarxa real. Aquest detectarà la màquina virtual com un host real més i li assignarà una IP de la xarxa.Això permet que la màquina virtual accedeixi a internet.*  
- *Es pot comunicar amb les MV connectades al mateix node (Switch, Punt d’accés, etc.) i també amb altres màquines reals.*

2. 🌐 **Xarxa nat:***

*És el tipus de xarxa que selecciona VirtualBox per defecte.*

*La xarxa NAT funciona de la següent manera:* *VirtualBox crea un router amb un servidor **DHCP** per les MV,a diferència de l’adaptador pont que pots configurar la màquina en DHCP o amb una IP estàtica, en la xarxa NAT es recomana utilitzar només **DHCP**.*

*Diferencies:*
- *Dona menys opcions que l’adaptador pont (no permet seleccionar l’adaptador de xarxa real, l’opció de **Mode promiscu està deshabilitada**).*
- *Permet fer renviament de ports.*
- *Les MV es poden comunicar amb la resta de màquines de la xarxa real, també amb les màquines virtuals, però a diferència de l’adaptador pont, les màquines reals no es podran comunicar amb les MV.*
 

3. 🔒 **Host-Only:**
   
*És un tipus de xarxa que crea una xarxa virtual privada entre el teu ordinador i les màquines virtuals.*

*Observacions:*
- *La màquina virtual només es podrà comunicar amb el **host** (l’ordinador real) i amb altres MV connectades a la mateixa xarxa Host-Only.*
- *Aquesta xarxa privada **no té connexió a internet** a no ser que configuris un altre adaptador de xarxa en NAT o Adaptador Pont.*

----
### 2.Si veiem que el disc dur no és prou gran, sabries dir si hi ha cap opció de fer-lo més gran un cop s’ha creat?

*Sí, en el menú de **Archivo** i **Administrador de medis virtual** o fent **Ctrl+D**, i seleccionant el disc de la màquina virtual fent dos clics i en l’apartat de **Tamany** el podem augmentar.*  

⚠️ *Amb cura: una vegada augmentat **no es pot tornar a reduir**.*