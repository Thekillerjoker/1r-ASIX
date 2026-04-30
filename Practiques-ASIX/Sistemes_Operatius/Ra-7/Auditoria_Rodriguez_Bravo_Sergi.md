![Portada](https://raw.githubusercontent.com/Thekillerjoker/1r-ASIX/main/Portada-2.png)

***Autor:*** *Sergi Rodríguez Bravo*

***Data de Cració:*** *30 d'abril de 2026*

***Versio del document:*** *V1.0*
----

🏫 **Centre / Curs**
-----------------------
- **CFGS ASIX**
- ***Mòdul:*** *Implementació de Sistemas Operatius*

*
---
# Index:
- [Index:](#index)
  - [Activitat Practica 1: Pla d'Auditoria:](#activitat-practica-1-pla-dauditoria)
    - [1. Creació del Pla:](#1-creació-del-pla)
    - [2. Simulació de Directives (GPO)](#2-simulació-de-directives-gpo)
    - [3. Troballa](#3-troballa)
  - [**Reccomanació:** *`Aplicar el principi de mínim privilegi i restringir els permisos només als usuaris necessaris.`*](#reccomanació-aplicar-el-principi-de-mínim-privilegi-i-restringir-els-permisos-només-als-usuaris-necessaris)
    - [4. Reflexió RGPD](#4-reflexió-rgpd)
  - [**Conclusió:** *Mesura desproporcionada i no recomendada segons el RGPD.*](#conclusió-mesura-desproporcionada-i-no-recomendada-segons-el-rgpd)
    - [5. Anàlisi d'esdeveniments.](#5-anàlisi-desdeveniments)
  - [Activitat 2: L'estandard ISO/IEC 27001:](#activitat-2-lestandard-isoiec-27001)
    - [1. Explicació CICLE PDCA.](#1-explicació-cicle-pdca)
    - [2. SOA:](#2-soa)
  - [Activitat 3: Eines d'auditoria (Open Source)](#activitat-3-eines-dauditoria-open-source)
    - [1. Lynis:](#1-lynis)
    - [2. OpenVAS (Escàner de vulnerabilitats)](#2-openvas-escàner-de-vulnerabilitats)
    - [3. Nmap (Auditoria de xarxa i ports)](#3-nmap-auditoria-de-xarxa-i-ports)
    - [4. BloodHound (Active Directory)](#4-bloodhound-active-directory)
  - [Activitat 4: Situació urgent diumenge:](#activitat-4-situació-urgent-diumenge)
    - [Evidència:](#evidència)
    - [Mesura immediata:](#mesura-immediata)
    - [Directiva de Futur:](#directiva-de-futur)
  - [Activitat 5 Auditoria de seguretat:](#activitat-5-auditoria-de-seguretat)
    - [A. Aduitoria d'Usuaris i Grups.](#a-aduitoria-dusuaris-i-grups)
    - [B. Auditoria d'Estat de Seguretat:](#b-auditoria-destat-de-seguretat)
    - [C. Auditoria de Hardware (USB).](#c-auditoria-de-hardware-usb)
---
## Activitat Practica 1: Pla d'Auditoria:

**Context:** *Una empresa de logística ha detectat que s'estan filtrant dades de clients. Tens l'encàrrec d'auditar el servidor de fitxers principal.*

### 1. Creació del Pla:

| Apartat  | Descripció                                  |
|----------|---------------------------------------------|
| Abast    | Servidor de fitxers principal               |
| Objectiu | Detectar filtracions de dades de clients    |
| Duracio  | 1 Setmana                                   |


| Eines        | Funcio                                |
|--------------|---------------------------------------|
| Wireshark    | Analitzar el trafic de xarxa          |
| Event Viewer | Revisar logs de seguretat             |
| Powershell   | Auditoria de comptes i configuracions |




| Punts clau a revisar      | Descripció                               |
|---------------------------|------------------------------------------|
| Control d'accessos        | Verificar qui accediex a dades sensibles |
| Permisos de carpetes      |      Detectar configuracions incorrectes |
| Logs de Seguretat         |        Identificar activitats sospitoses |


### 2. Simulació de Directives (GPO)
1. Bloqueig del compte després de 4 intents fallits
2. Restrincció d'horaris d'inici de sessió.
3. Deshabilitar dispositius USB no autoritzats.


### 3. Troballa

*S'ha detectat que diverses carpetes del servidor tenen permisos assignats al grup **Everyone (Tots els usuaris)**, permetent accés total a qualsevol usuari.*

**Nivell de risc:** *`Alt`*

**Impacte:** *`Possible accés no autoritzat i filtració de dades sensibles`*


**Reccomanació:** *`Aplicar el principi de mínim privilegi i restringir els permisos només als usuaris necessaris.`*
---

### 4. Reflexió RGPD

*La instal·lació d'un `Keylogger` **No respecta el RGPD**.*

Aquesta mesura viola el principi de minimització de dades, ja que recull molta més informació de la necessària, incloent dades personals i credencials.

A més , afecta greument la privacitat dels treballadors i no és proporciona al problema que es vol solucionar.


**Conclusió:** *Mesura desproporcionada i no recomendada segons el RGPD.*
---

### 5. Anàlisi d'esdeveniments.

| Esdeveniment                                              | Tipus d’atac            | Risc  |
| --------------------------------------------------------- | ----------------------- | ----- |
| 50 intents fallits d’inici de sessió admin (192.168.1.45) | Força bruta             | ALT   |
| Inici de sessió fora d’horari (treballador_temporal)      | Robatori de credencials | MITJÀ |
| Còpia de 5GB a disc extern                                | Exfiltració de dades    | ALT   |

*
---

## Activitat 2: L'estandard ISO/IEC 27001:

*L'auditoria sovint es basa en normatives internacionals. Cerca informació sobre la norma ISO 27001:*

### 1. Explicació CICLE PDCA.

*El cicle  **PDCA (Plan-Do-Check-Act)** és un model de millora contínua utilitzat en la gestió de la següretat de la informació:*

- **Plan (Planificar):** Identificar riscos, definir polítiques de seguretat i establlir objectius.

- **Do (Fer):** Implementar les mesures de seguretat definides (controls, procediments, tecnologies).

- **Check (Verificar):** Revisar i auditar el sistema per comprovar si les mesures funcionen correctament.
  
- **Act (Actuar):** Corregir errors i millorar el sistema de seguretat de manera contínua.

Aquest cicle garanteix que la seguretat no sigui estàtica, sinó que evolucioni constantment.


### 2. SOA:

*El **SOA (Declaració d’Aplicabilitat)** és un document clau dins de la norma ISO 27001.*

**Serveix per:**

- Indicar quins controls de seguretat s’apliquen a l’organització  

- Justificar per què s’apliquen o no determinats controls  

- Relacionar els controls amb els riscos identificats  

*
---

## Activitat 3: Eines d'auditoria (Open Source)

*Cerca i descriu breument la funció de 3 de les següents eines que un auditor podria utilitzar per recollir evidències tècniques. Posa un exemple d’ús de cada una d’elles:*

### 1. Lynis:

**Funció:**  
Lynis és una eina d’auditoria de seguretat per a sistemes Linux que analitza la configuració del sistema i detecta vulnerabilitats, males configuracions i possibles riscos.

**Exemple d’ús:**  
Executar una auditoria en un servidor Linux per comprovar si hi ha serveis insegurs activats o configuracions incorrectes.


### 2. OpenVAS (Escàner de vulnerabilitats)

**Funció:**  
OpenVAS és una eina que escaneja sistemes i xarxes per detectar vulnerabilitats conegudes, com programari desactualitzat o errors de configuració.

**Exemple d’ús:**  
Analitzar un servidor web per detectar si té vulnerabilitats conegudes que podrien ser explotades per atacants.



### 3. Nmap (Auditoria de xarxa i ports)

**Funció:**  
Nmap és una eina per escanejar xarxes i descobrir dispositius, ports oberts i serveis actius.

**Exemple d’ús:**  
Fer un escaneig d’un servidor per veure quins ports estan oberts i detectar serveis que no haurien d’estar accessibles.


### 4. BloodHound (Active Directory)

**Funció:**  
BloodHound analitza entorns d’Active Directory per identificar camins d’atac i possibles escalades de privilegis.

**Exemple d’ús:**  
Detectar si un usuari amb pocs privilegis pot arribar a ser administrador del domini mitjançant relacions incorrectes.

*
---

## Activitat 4: Situació urgent diumenge:

*S'ha detectat que un usuari del departament de RRHH ha accedit a la base de dades de comptabilitat a les 3:00 AM del diumenge.*


### Evidència:

El primer que cal sevisar és el **log de seguretat del sistema** per comprovar l’inici de sessió de l’usuari.

*Per exemple amb Powershell:*
```powershell
Get-EventLog -LogName Security
```
>[!IMPORTANT]- Event Viewer:
> També és pot utilitzar el Visor d'esdevediments per analitzar:
>- Inicis de ssesió (Logon).
>- Hora exacta d'accés.
>- Equip o IP d'origen.
>

### Mesura immediata:

- *Deshabilitar temporalment el compte d'usuari.*
- *Bloquejar l'accés a la base de dades.*
- *Iniciar una investigació per determinar si ha estat un accés legítim o compromès.*


### Directiva de Futur:

***Implementar una restricció d'horaris de sessió, de manera que:***

- Els usuaris només puguin accedir dins del seu horari laboral.
- És bloquejin accessos fora d'horari automàticament.


***També es recomana:***
- Activar alertes per accessos fora d'horari.
- Aplicar el principi de mínim privilegi.

*
---

## Activitat 5 Auditoria de seguretat:

*Se sospita que un antic administrador ha creat un usuari "backdoor" (porta del darrere) al sistema i que s'han connectat dispositius USB no autoritzats per extreure informació.*
*Utilitzant la línia de comandes a Windows executa i documenta els resultats dels següents punts al teu fitxer Markdown:*

### A. Aduitoria d'Usuaris i Grups.

***Executa un comandament per llistar tots els usuaris del sistema i la seva darrera data d'inici de sessió.***

```powershell
Get-LocalUser | select Name, Enabled, LastLogon
#Resultat:
Name               Enabled LastLogon
----               ------- ---------
Administrador        False
DefaultAccount       False
Invitado             False
sergi                 True
UsuarioPrueba         True
UsuarioPrueba1        True
WDAGUtilityAccount   False
WsiAccount           False 18/12/2025 13:00:43
 ```

**Anàlisi:**
- **Sergi:** -> Usuari prinipal actiu (Correcte).
- **UsuarioPrueba i UsuarioPruba1:** -> Usuaris acius que poden ser de proves però podrien ser innecessaris o un possible risc si no s'utilitzen.
- **Administrador desactivat:** -> Bona pràctica de seguretat el tenir-ho desactivat si no s'utilitza.
- **DefaultAccount, Invitado, WDAGUtilityAccount:** -> Bona pràctica tenir-los desactivats ja que son comptes del sistema.
- **WsiAccount:** -> Compte del sistema amb activitat antiga , és correcte tenir-ho desactivat.

**Conclusió:**
*No és detecta cap usuari "Backdoor", però és deveria revisar els comptes UsuarioPrueba i UsuarioPrueba1 i si no s'utilitzen desactivar-los.*

### B. Auditoria d'Estat de Seguretat:
*Verifica si els sistemes de protecció estan actius i actualitzats.*

```powershell
Get-MpComputerStatus | Select AntivirusEnabled, RealTimeProtectionEnabled
#Resultat
AntivirusEnabled RealTimeProtectionEnabled
---------------- -------------------------
           False                     False
```

*Jo tinc els dos desactivats ja que tinc l'antivirus Mcafee de pagament que ja el tinc activat i també en temps real.*

*Però en cas de no tenir cap antivirus de pagament hi annar amb el de Windows si hauria d'estar els dos activats de nor estar-ho podría ser una possible manipulació del sistema.*

### C. Auditoria de Hardware (USB).
*Cerca al registre quins dispositius USB s'han connectat darrerament al servidor.*

![Catura](https://raw.githubusercontent.com/Thekillerjoker/1r-ASIX/main/USBS.png)

**Anàlisi:**
*S'han detectat els dispositius USB connectats reentment si son esl que se que sons necessaris o tinc el control bé, però si hi ha un USB que no identifiquem o no sabem que és podría haver estat utilitzat per copiar informació sensible.*