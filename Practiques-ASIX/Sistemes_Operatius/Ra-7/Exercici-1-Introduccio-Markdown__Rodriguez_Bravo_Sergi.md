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

