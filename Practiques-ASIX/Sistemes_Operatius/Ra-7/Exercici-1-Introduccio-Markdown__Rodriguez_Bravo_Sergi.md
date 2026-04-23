![Portada](https://raw.githubusercontent.com/Thekillerjoker/1r-ASIX/main/Portada.png)

***Autor:*** *Sergi Rodríguez Bravo*

***Data de Cració:*** *22 d'abril de 2026*

***Versio del document:*** *V1.0*
----

🏫 **Centre / Curs**
-----------------------
- **CFGS ASIX**
- ***Mòdul:*** *Implementació de Sistemas Operatius*



---

# Index:
- [Introducció](#introducció)
- [Objectiu](#objectiu)
- [Contingut](#contingut)
  - [Teoria](#teoria)
  - [Part 1](#part-1-requisits-de-seguretat-del-sistema-i-de-les-dades-cerca-la-informació-per-internet)
  - [Part 2](#part-2-drets-dusuari)

---
# Introducció:

## *Objectiu*

Documentar els requisits de seguretat i la política de privilegis d'un servidor de fitxers utilitzant sintaxi Markdown completa (taules, llistes, blocs de codi i ressaltats).
---
# Contingut

## Teoria
1. ### ***Requisits de seguretat del sistema i de les dades.***

La seguretat no és un producte que es compra, sinó un procés continu. Es basa en mantenir l'equilibri de la **Triada de la Seguretat (CIA)**:


- **Confidencialitat:** Garantir que la informació només sigui accesible per a qui té autorització. (Exemple: Xifrat de dades).
- **Integritat:** Assegurar que les dades no han estat modificades de forma no autoritzada o accidental. (Exemple:Firmes digitals o hashes).
- **Disponibilitat:** Garantir que els sistemes i les dades esstiguin operatius quan es necessitin.(Exemple:Backups i redundància).

### Tipus de requisits

1. **Requisits Físics:** Proteció del maquinari(Servidors tancats sota clau, càmeres, proteció contra incendis).
   
2. **Requisits Lògics:** Protecció del programari (antivirus, tallafocs, actualitzacions de seguretat).
3. **Requisits Legals:** Compliment de lleis com la _LOPDGDD_ (Protecció de dades).
**
---
2. ### Drets d'usuari

Molt sovint es confonen els **"Drets"** amb els **"Permisos"**, però en administració de sistemes (especialment en entorns Windows/Active Directory i Linux) són conceptes diferents:
 
### A. Drets d'usuari (User Rights)

Són les capacitats que té un usuari per realitzar tasques que afecten a **tot el sistema.** No es refereixen a un fitxer concret, sinó al comportament del S.O.

- *Exemples:* Poder canviar l'hora del sistema, carregar controladors de dispositiu, tancar el sistema remotament o fer còpies de seguretat.

### B. Permisos (Permissions)

Són les regles associades a **objectes específics** (fitxers, carpetes, impressores).

- *Exemples:* Lectura, escriptura, execució o control total sobre una carpeta compartida.

### El Principi de Mínim Privilegi (PoLP)
**Cada usuari ha de tenir només els drets i permisos estrictament necessaris per fer la seva feina, i durant el temps mínim necessari.**

- Si un administratiu només ha de llegir un PDF, no ha de tenir permisos d'escriptura.
- Si un tècnic ha d'instal·lar un programa, usarà un compte d'admin només per a aquesta tasca, no per navegar per Internet.


## Part 1: Requisits de seguretat del sistema i de les dades (cerca la informació per Internet)
>[!NOTE]- Explicació:
En aquest apartat, has de definir les tres potes de la seguretat (**C-I-A**): Confidencialitat, Integritat i Disponibilitat.
>
**Tasca:** Omple el següent esquema en el teu fitxer `.md`:

- Crea una **taula** que compari les amenaces físiques vs. lògiques.
  
- Utilitza **llistes de tasques `(-[ ])`** per definir els requisits mínims d'enduriment (*hardering*) del sistema que s'han de tenir en compte o que hauríem d'aplicar sempre.

>[!IMPORTANT]- Taula comparativa:
Aqui faig una taula comporativa de les amenaces físiques vs lògiques de les tres potes de la (C-I-A).
>

| Tipus d'amenaça | Descripció                                              | Exemples                                                        |
|-----------------|---------------------------------------------------------|-----------------------------------------------------------------|
| Fisíques        | Afecten els components materials del sistema (Hardware) | Incendis, inundacions, robatori d'equips, talls de llum        |
| Lògiques        | Afecten el programari (Software) i a les dades          | Virus, malware, atacs de hackers, phishing, accés no autoritzat |

### *Hardering del sistema (per categories):*
#### Sistema
- [ ] Actualitza el sistema operatiu i paquets
- [ ] Eliminar serveis innecessaris
- [ ] Configurar permisos correctament

#### Autentificació i accés
- [ ] Contrasenyes robustes
- [ ] Activar 2FA
- [ ] Principi de menor privilegi
- [ ] Desactivar login root

#### Xarxa
- [ ] Configurar firewall
- [ ] Tancar ports no utilitzats
- [ ] No obrir ports innecessaris només els indispensables
- [ ] Canviar configuracions per defecte

#### Monitoratge
- [ ] Revisar logs del sistema
- [ ] Detectar accessos sospitosos

#### Dades
- [ ] Fer còpies de seguretat
- [ ] Xifrar dades sensibles

#### Altres
- [ ] Antivirus actualitzat
- [ ] Protecció física dels equips
- [ ] Bloqueig automàtic de sessió

## Part 2: Drets d'usuari

Aquí documentaràs el sistema de permisos seguint el principi de **mínim privilegi.**

**Tasca:** Imagina la jerarquia d'usuaris en un Institut (Admin, Director, Professor).
- Explica quins drets aplicaries a cada un dels usuaris (mínim 3 per cada un) i explica on i com aplicaries els permisos (el com vol dir explicar-ho tècnicament). Utilitza una taula.

### Sistema de permisos (Principi de mnínim privilegi).

>[!TIP]- Explicació:
El principi de mínim privilegi estableix que cada usuari només ha de tenir els permisos estrictament necessaris per realitzar la seva feina.
>

#### Sistema de permisos per rols (Principi de mínim privilegi)

| Usuari    | Permis                        | Descripció                                                      | Com aplicar-lo tècnicament                                            |
|-----------|-------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------------|
| Admin     | Gestió completa del sistema   | Pot instal·lar software, crear usuaris i configurar el sistema  | Afegir a grup sudo (`usermod -aG sudo admin`)                         |
| Admin     | Accés a tots els fitxers      | Pot llegir, modificar i eliminar qualsevol fitxer               | Permisos root (`chmod`, `chown`)                                      |
| Admin     | Configuració de xarxa         | Pot modificar configuracions de xarxa i firewall                | Accés a `/etc/network`, `ufw`, `iptables`                             |
| Director  | Accés a dades Administraitves | Pot consultar i modificar dades del centre                      | Permisos de lectura/escriptura en carpetes específiques (`chmod 770`) |
| Director  | Gestió de documents           | Pot crear i editar documents institucionals                     | Carpeta compartida amb grup (`chown :directors`)                      |
| Director  | Accés a informes              |  Pot visualitzar informes però no configuració del sistema      | Permisos només lectura (`chmod 750`)                                  |
| Professor | Accés a materials docents     |  Pot llegir i editar continguts educatius                       | Carpeta compartida amb grup professors (`chmod 770`)                  |
| Professor | Introducció de notes          |  Pot modificar només les seves dades                            | Aplicació amb control d’accés per usuari                              |
| Professor | Accés limitat al sistema      | No pot instal·lar software ni accedir a configuració            | Usuari estàndard sense sudo                                           |
| Alumne    | Accés a materials             | Pot consultar continguts educatius                              | Permisos de només lectura (`chmod 750` o `chmod 755`)                 |
| Alumne    | Entrega de treballs           | Pot pujar fitxers en carpetes específiques                      | Carpeta amb permisos d’escriptura controlada (`chmod 730`)            |
| Alumne    | Accés restringit al sistema   |  No pot modificar configuracions ni instal·lar software         |  Usuari sense sudo i sense accés a directoris del sistema             |

#### Explicació tècnica:
- **Gestió d'usuaris i grups (Linux):**
  - *Crear grups:* `groupadd Admin`, `groupadd Director`, `groupadd Professor`, `groupadd Alumne`.
  - *Assignar usuaris:* `usermod -aG Admin usuari`, `usermod -aG Director usuari`, `usermod -aG Professor usuari`, `usermod -aG Alumne usuari`
- **Permisos de fitxers:**
  - *`chmod`:* Definir permisos (lectura,escriptura,execució).
  - *`chown`:* assignar propietari i grup.
- **Accés administratiu:**
  - Només l'Admin té `sudo` (Control del sistema).
- **Control d'accés en aplicacions:**
  - Sistemes com Moodle o similars gestionen rols (professor,alumne,admin).





