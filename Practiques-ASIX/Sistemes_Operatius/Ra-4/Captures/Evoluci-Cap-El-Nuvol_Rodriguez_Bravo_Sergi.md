# Projecte: Evolució cap al Núvol i Serveis Multimèdia:

*L'empresa InnovaTech, on ja vas muntar el domini local, té nous requeriments. Els empleats es queixen que accedir als vídeos de* *formació va lent i volen treballar des de casa sense VPN. El gerent t'ha demanat un informe tècnic per solucionar-ho.*

**Format de lliurament: Un document PDF amb les respostes, gràfics o taules comparatives.**
---

## Exercici 1: El Repte del Vídeo (Client-Servidor vs. Streaming):

**Context:** *Actualment, els vídeos de formació (arxius .MP4 de 2GB) estan en una carpeta compartida del servidor*
*(\\SRV-DC01\Videos). Quan 10 persones intenten obrir el vídeo alhora, la xarxa es col·lapsa. Valoreu passar cap a una configuració d’Streaming.*

**Tasca d'investigació:** *Explica la diferència entre Descarregar un fitxer (File Server) i fer Streaming (com YouTube/Netflix).*

1. **Protocols:** *Quina diferència hi ha entre transferir un fitxer per protocol SMB (el de Windows) i utilitzar protocols de streaming com **HLS** o **DASH**?*
2. **L'experiència d'usuari:** *Què passa si l'ample de banda baixa? (Pista: Parla del Buffering i de la qualitat adaptativa).*
3. **Proposta:** *Busca informació sobre "Plex Media Server" o "Microsoft Stream". Què aportarien a l'empresa en lloc de tenir els vídeos en una carpeta simple?*



**Exercici 2:** *Active Directory vs. Entra ID (Azure AD)
Context: L'empresa sent a parlar molt del "Núvol de Microsoft" i vol saber si ha de llençar el servidor que vas instal·lar.
Tasca d'investigació: Fes una taula comparativa entre l'Active Directory tradicional (el que tens instal·lat a la màquina virtual) i l'Azure Active Directory (ara anomenat Microsoft Entra ID).
Ha d'incloure:
On s'executa? (Local vs. Centre de dades de Microsoft).
Què gestiona? (Ordinadors i servidors vs. Aplicacions web i dispositius mòbils).
Protocol principal: (Kerberos/LDAP vs. HTTP/SAML/OIDC).
Conclusió: Podem tenir els dos alhora? Investiga què és un "Entorn Híbrid" i l'eina Azure AD Connect.

Exercici 3: Emmagatzematge: Disc Dur vs. OneDrive/Sharepoint
Context: El departament de Màrqueting té por de perdre dades si es crema el servidor local (Disaster Recovery).
Tasca d'investigació: L'empresa dubta entre ampliar els discos durs del servidor local o comprar llicències de núvol.
Seguretat: Què és el model de responsabilitat compartida al núvol? Si esborres un fitxer a OneDrive, qui és responsable de recuperar-lo, Microsoft o tu?
Accessibilitat: Com accedeix un client a un fitxer al servidor local (estant fora de l'oficina) vs. com accedeix a SharePoint/OneDrive?
Costos: Fes una simulació ràpida. Què surt més a compte a 5 anys: comprar un servidor físic nou de 5.000€ o pagar 10€/mes per usuari (suposant 20 usuaris) al núvol?

Exercici 4 (Creatiu): Dibuixa l'Arquitectura de Xarxa
Context: Cal explicar visualment als caps com quedarà l'empresa.
Tasca: Fes un diagrama (pots fer-lo a mà, amb PowerPoint, Canva o draw.io) que mostri l'arquitectura "Híbrida" d'InnovaTech. Ha d'aparèixer:
L'oficina física amb el teu Servidor AD i els Clients PC.
El Núvol (Azure/Microsoft 365).
Una "canonada" o connexió entre ells (sincronització d'usuaris).
Un treballador amb portàtil treballant des de casa connectant-se al núvol.

