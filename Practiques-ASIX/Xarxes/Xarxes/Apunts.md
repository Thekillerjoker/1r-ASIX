## Capa de transport:
**Se'encarrega de:**
*Assegurar que la informació arribi a destí (confiança).Establir connexions de destí a destí.Si bé els protocols de fins a capa 2 ens permeten fer arribar dades a un host concret, no diferencien entre aplicacions. És la capa de transport qui afegeix informació addicional per fer-ho.*

*Controlar el flux dades. Ajustar el volum de dades enviades per no col·lapsar el receptor. D’aquesta manera si, per exemple, un servidor d’arxius s’està col·lapsant, la capa 3 de transport li permet demanar que el client envií la informació més lentament.*

## Capa tcp/ip:
*En el cas de TCP/IP es disposa de dos protocols diferents de capa de transport: UDP i TCP. Segons les necessitats, es pot utilitzar un o altre.*

*Les característiques bàsiques d’aquests dos protocols són:*
*UDP: No assegura que la comunicació arribi a destí i és un protocol bastant simple.*

*TCP: Afegeix més informació per poder garantir que les dades arribin a destí. És un protocol relativament complex.*

**Quan fer servir UDP i cuan TCP/IP.**
- *Per enviar vídeo o veu on és poden perdre part de les dades :UDP.*
- *Per enviar arxhius o dades importants on és important que no és perdi part de l'infomració TCP.*
## 6.2 Ports I conexions:
*És un concepte lògic que es on entra i surt la informació.*
*Normalment, poden haver-hi moltes aplicacions executant-se en cada host i comunicant-se a través de la xarxa.La capa de transport (tant TCP com UDP) afegeix el concepte de port per distingir el programa de destí dins d’un host.*

*No n’hi ha prou amb indicar l’adreça IP del destí, a més s’ha de conèixer l’aplicació que recollirà el missatge.A cada programa se li assigna un número de port, o més, per esperar la recepció de missatges.No es pot fer servir el mateix port per dues coses diferents.Es fan servir tant per l'enviament com per la recepció.*
*Podem veure la seva utilitat en la següent imatge, a on tres clients accedeixen al mateix servidor Telnet (Telnet permet connectar-nos en mode terminal a un ordinador remot):*

**Tipus de ports**
*Els números de port són de 16 bits i poden agafar qualsevol valor entre 0 i 65535.* 
**Es divideixen en tres grups:**
**Ports coneguts (del 0 al 1023):** 
*Són assignats a processos als quals només pot accedir el sistema operatiu o l’administrador del sistema.* 
*Reservats a serveis i programes d’ús molt estès (per exemple, correu electrònic, DNS, HTTP…).* 

*No es poden utilitzar lliurement.*

**Ports registrats (del 1024 al 49151):**
*Registrats per la IANA normalment per aplicacions comercials.*
**Ports dinàmics o privats (del 49152 al 65535):**
*Són ports lliures que l’usuari pot fer servir sense restriccions.*

### Ports:
- 21: FTP.
- 80: HTTP.
- 443: HTTPS.
- 22: SSH.
- 23: Telnet.
- 53: DNS.
## 6.2.2 Sockets:
*Anomenem **Socket** a una conexió virtual entre dos extrems. La ínformació bàsica d'un socket és*
```powerhsell
IP_origen:port_origen - IP_destí:port_destí.
```
*La comanda netstat ens permet veure tant en Linux com en Windows els sockets oberts que te el nostre ordinador. En la següent captura podem veure com tenim moltes connexions (sockets) obertes:*
```powershell 
netstat -n
```
## 6.3: UDP:
## 6.3.1 Descripció:

*El protocol UDP és el més simple de la capa de transport. 
Bàsicament consisteix en afegir números de port als paquets IP per distingir diferents comunicacions de/al mateix host. D’aquesta manera, quan el nostre ordinador rep un datagrama, sap pel número de port quina aplicació l’està esperant.
Les característiques més importants d'UDP són:
No està orientat a la connexió
No s’estableix cap connexió prèvia amb l’altre ordinador per poder transmetre el missatge. Simplement enviem el paquet.
No fiable
Els missatges UDP es poden perdre o arribar en mal estat.
Ha de ser el programa qui ho comprovi.
UDP no realitza el reenviament dels missatges perduts.
Reconstrucció de dades no ordenada.
No proporciona mecanismes per reordenar les dades en la seva seqüència original.
Sense control de flux	
No disposa de mecanismes per controlar la quantitat de dades que transmet el host d’origen per evitar la saturació del host de destí.*
## 6.3.2 ÚS d'UDP:
*S’utilitza UDP en aplicacions on:*
- **No s’admeten retards.**
  - Es pot tolerar certa pèrdua de dades durant la transmissió.
  - Per exemple:
    - Streaming de audio, video
    - Veu sobre IP (VoIP)
    - Jocs online
- Aplicacions de pregunta resposta.
  - No val la pena enviar tants missatges (establir la connexió, tancar-la…) 
    - Per exemple: DHCP o DNS
    - Tràfic multicast o Broadcast
    - Mai es pot enviar per TCP
## 6.3.3 DaTAGRAMA:
La capçalera UDP, a la pràctica només afegeix un número de port.
El seu funcionament és simple: 
A les dades que es volen enviar se'ls hi afegeix el port d'origen i el de destí. 
I s'envien a la capa IP perquè hi afegeixi les IPs d'origen i destí i la resta d'informació associada a la capa IP.
Un datagrama UDP té el següent aspecte:
La descripció dels camps és:
Port origen: Quin port del dispositiu d’origen ha enviat el datagrama.
Port destí: A quin port del dispositiu de destí va dirigit el datagrama.
Longitud: Tamany en bytes del datagrama incloent capçalera i dades.
Checksum: Suma de verificació de la capçalera i les dades. És opcional i es pot omplir amb zeros si no es vol utilitzar.
Dades: Les dades que vol enviar l’aplicació que està utilitzant UDP.

Cal observar que amb la informació que afegim a les dades, si volem enviar molts paquets de dades, no podem

Ethernet + IP + UDP

En la següent figura podem veure un datagrama UDP dins d’un paquet IP que viatja dins d’una trama Ethernet (no s’inclouen els set bytes de preamble de la trama Ethernet):
Podem veure que, d’un total de 256 bytes, 46 bytes són de capçaleres:
18 de Ethernet (el CRC final també forma part d’Ethernet)
20 de IP
8 de UDP
El nombre de dades que s’envien (Payload) depèn de les necessitats de l’aplicació. En total tindrà un tamany d’entre 0 i 1472 bytes (per no superar el tamany màxim de 1518 bytes de la trama Ethernet).

TCP
Descripció
TCP és un protocol que, a més del número de port, afegeix més informació per fer el que no fa UDP:
Assegurar que arribin tots els paquets.
Assegurar que arribin per ordre.
Assegurar que no continguin errors.
Controlar el flux de dades.
Ús de TCP
S’utilitza TCP en aplicacions on:
Els segments han d’arribar en un ordre determinat perquè es puguin processar la informació correctament.
Totes les dades s’han de rebre de forma completa per considerar-se útils.
Per exemple:
Exploradors web (HTTP)
Correu electrònic (SMTP)
Transmissió de fitxers (FTP)
Segment
Per aconseguir les funcionalitats de TCP, cal una capçalera bastant més complexa:

La descripció dels camps és:
Port origen: Quin port del dispositiu d’origen ha enviat el datagrama.
Port destí: A quin port del dispositiu de destí va dirigit el datagrama.
Nombre de seqüència: Número de 32 bits amb el nombre de byte que s’està enviant. Permet ordenar les dades a destí.
Nombre d’acusament de rebut (ACK): Número de 32 bits amb el nombre de bytes rebuts correctament.
Long. Capçalera: Longitud de la capçalera en múltiples de 4 bytes. Si la capçalera no conté el camp opcions te el valor de 5 (20 bytes).
Flags: Una sèrie de bits que ens permeten afegir informació. Els més importants són:
ACK: Indica que el camp nombre d’ACK és important. 
SYN: S’utilitza a l’iniciar la connexió.
FIN: S’utilitza al finalitzar la connexió. 
Mida finestra: Nombre de bytes que acceptem rebre sense confirmar-ne la recepció.
Longitud: Tamany en bytes del datagrama incloent capçalera i dades.
Checksum: Suma de verificació de la capçalera i les dades. És opcional i es pot omplir amb zeros si no es vol utilitzar.
Urgent pointer: Permet indicar quines dades de l’enviament són urgents.
Opcions: El protocol TCP permet una sèrie d’opcions que no veurem. Les més importants són la selecció de l’escala del tamany de la finestra i els ACK selectius.
Dades: Les dades que vol enviar l’aplicació que està utilitzant TCP.
Ethernet + IP + TCP
En la següent figura podem veure un segment TCP dins d’un paquet IP que viatja dins d’una trama Ethernet (no s’inclouen els set bytes de preamble de la trama Ethernet):

Podem veure que, d’un total de 256 bytes, 58 bytes són de capçaleres:
18 de Ethernet (el CRC final també forma part d’Ethernet)
20 de IP
20 de TCP
El nombre de dades que s’envien (Payload) depèn de les necessitats de l’aplicació. En total tindrà un tamany d’entre 0 i 1460 bytes (per no superar el tamany màxim de 1518 bytes de la trama Ethernet).
Inici de la connexió
Abans de començar a enviar informació per TCP, els dos dispositius han d’obrir la connexió. Per fer-ho es segueixen tres passos:
El client envia un segment al servidor indicant que volem iniciar la comunicació. Aquest datagrama porta:
Ports d’origen i destí adequats.
Nombre de seqüència (aleatori, aquí en direm A)
El flag SYN activat.
El servidor respon amb un segment acceptant la connexió. Aquest datagrama porta:
Ports origen i destí adequats.
Nombre de seqüència (aleatori, aquí en direm B)
Num. ACK = A + 1
El flag SYN activat.
El client respon amb un segment confirmant que han iniciat la connexió. Aquest datagrama porta:
Ports origen i destí adequats.
Nombre de seqüència = A+1.
Num. ACK = B + 1
