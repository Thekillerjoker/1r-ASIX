# Seguretat i Drets d'Usuari

***Autor:*** *Sergi Rodríguez Bravo*

***Data de Cració:*** *22 d'abril de 2026*

***Versio del document:*** *V1.0*
----

🏫 **Centre / Curs**
-----------------------
- **CFGS ASIX**
- ***Mòdul:*** *Implementació de Sistemas Operatius*

![Portada](https://www.markdownguide.org/assets/images/generated/assets/images/shiprock-1080.webp)
---

# Index:
- [Introducció](#introducció)
- [Objectiu](#objectiu)
- [Contingut](#contingut)
  - [Teoria](#teoria)
  - [Part 1](#part-1-requisits-de-seguretat-del-sistema-i-de-les-dades-cerca-la-informació-per-internet)

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

