# 🖥️ Gestors d'arrencada i sistemes duals (Windows 11 + Ubuntu 24.04):
----
1. ## 📘 Introducció:
*Quan s’inicia un ordinador modern amb **UEFI**, aquest firmware comprova el maquinari i busca a la partició especial **EFI System Partition (ESP)** els fitxers d’arrencada. (Abans de **l’UEFI**, el que dominava era el **BIOS clàssic** (Basic Input/Output System))*
**Resum històric:**
**Anys 1980 fins a mitjans 2000** →*gairebé tots els PCs feien servir BIOS.*


*El BIOS estava gravat en una memòria ROM de la placa base i:*


*Inicialitzava el maquinari bàsic (CPU, memòria, teclat, disc dur...).*


*Buscava el primer dispositiu d’arrencada i llegia el primer sector (els **512 bytes del MBR**).*


*Cedia el control al codi del gestor d’arrencada.*


**Limitacions del BIOS + MBR:**


*Només podia gestionar **discos fins a 2 TB**(perquè el MBR només té 32 bits per adreces de sectors). GPT permet discs de fins a 9,4 ZB (zetabytes)*


*Només admetia 4 particions primàries (o 3 + una estesa amb lògiques).*


*Interfície molt bàsica en mode text (no gràfica).*


*Inicialització lenta i poc flexible.*


*Sense seguretat: qualsevol codi al MBR podia executar-se.*


**Transició:**


*Cap al 2005–2010, es va començar a introduir UEFI (Unified Extensible Firmware Interface), impulsat per Intel.*


*Windows va adoptar UEFI de manera generalitzada a partir de Windows 8 (2012).*


*Avui, tots els ordinadors nous venen amb UEFI i disc particionat en GPT en lloc de MBR.*
---

2. ## Pràctica guiada.Realitzar captures de pantalla de cada pas.
>[!TIP] - objectiu
>*Configurar un sistema >**dual-boot** 
>amb **Windows 11** i >**Ubuntu 24.04** i
>apendre a reparar el gestor d'arrancada.*
>

>[!IMPORTANT]- Explicació:
>*Jo degut a les caracteristiques del meu ordinador he tingut que fer servir **Windows 10** i **Ubuntu 18.04**.*
>

### 1. Instal·lació i configuració de windows 10 i crecacio de particions :
1. **Pasos preinstalació:**
   1. **RAM:***En aquest cas sel·leciono (4096MB) 4GB, que es la meitat de la meva RAM.*
   ![RAM](./Captures/pt-2/Ejemplo-2/Ram.png)
   2. **Disc:** *Seleccionem crear un disc dinàmic en format vdi i en aquest cas li donem un espai de **130GB**.*
   ![Disc](./Captures/pt-2/Ejemplo-2/Disco.png)
    3. **Sistema:** *En l'ordre d'arrancada posem la iso per debant del disc.*
  > **⚠️ Important:** Desactivar el Sistema EFI
  > 
  > *Encara que amb el sistema EFI és mes recomenable que el sitema bios ja que l'EFI permet mes particions que EFI,pero el sistema EFI dona problemes amb el dualBoot a virtualbox , axi que per que no doni problemes es important desactivaro.*
   >
   ![Sistema](./Captures/pt-2/Ejemplo-2/Configuración.png)
   4. **CPU:Configuració→Sistema →Processador:** *Seleccionar dos CPU.*
   ![CPU](./Captures/pt-2/Ejemplo-2/Processador.png)

2. **Instalacio Windows 10:**
   1.**Tipus d'instalació:** *Seleccionar personalizada: instalar solo windows 10 (avanzado).*
   2.**Creacio de les particions:** 
   *Per defecte auria de sortir així:*
   ![Discos-1](./Captures/pt-2/Ejemplo-2/Disco-1.png)
   
   **En aquest cas ens demana crear les particions ESP, una particio per el sistema i deixar espai lliure per l'ubuntu.** 
   *El primer pas es afegir una nova partició i en el tamany seleccionar 61440MB (60GB), i Windows ja ens creara automaticament la particio ESP.*

   ![Discos-2](./Captures/pt-2/Ejemplo-2/Discos-2.png)
   3. **Comprobacio:** *Comprobarem que les particions del disc son les correctes una vegada instalat windows.*
   ![Discos-3](./Captures/pt-2/Ejemplo-2/Discos-3.png)
----
3. **Preparacio de windows per dual abans de instalar ubuntu.**
  
  *Desactivarem **Fast Startup** obrint el cmd com administrador i executarem:*
  
```powershell
 powercfg /h off
 ```
-------
### 2. Instalació d'Ubuntu 18.04:
1. **Comprovacions abans d'arrencar:**
   - Comprovem que EFI estigui desactivat.
   - Treurem l'ISO de Windows i afegirem la d'Ubuntu.
  ![ISO](./Captures/pt-2/Ejemplo-2/Iso-Ubuntu.png)
2. **Seleccionem Instalar Ubuntu:**
   ![Instalacio-Ubuntu](./Captures/pt-2/Ejemplo-2/sELECIONAR-INSTALAR-UBUNTU.png)
>[!TIP] -Impotant
>he comprobat que ha varis companys
>els i fallaba el dualboot a l'hora
>d'actualitzar.
>per aixo es millor desactivar l'opcio
>d¡instalar les actualitzacions.
>
3. **Seleccionar Instalacio i crear particions:**
   1. **Sel·lecio manual:** *En cas de haber fet tots els pasos correctament l'ubuntu ja auria de detectar el windows 10 com a l'altre sistema operatiu i podriem fer la instalaciò automatica pero la farem manual.*
   ![Instalacio-Ubuntu-2](./Captures/pt-2/Ejemplo-2/Instalacuin-Ubuntu.png)
   2. **


