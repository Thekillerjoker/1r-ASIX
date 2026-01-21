# 🪟 🐧Exercici 2: Repte de conexió a Active Directory:
---
## 🏢🪟 A partir d'un client Linux amb Ubuntu 24.04, connectat a l'Active Directory que has creat al Windows server 2019:
---
### 1. Instalar els paquets necessaris:
*Instalarem els paquets necessaris que són:* **realmd, sssd, sssd-tools, adcli, samba-common-bin, package-git i krb5-user**

![Instalacio-Paquets](./Linux/Captura-1.png)

*Una vegada s'han instalat alguns paquets ens apreixara una finestra de la configuració del kerberos.*

![Definició-Domini](./Linux/Captura-2.png)

*En la finestra el primer que ens demanara és especificar el domini al que ens volem connectar "ha d'estar tot en majuscules encara que el domini sigui en minuscules".*

![Definició-Domini-2](./Linux/Captura-3.png)

*En el següent pas et demana indicar el "**hostname**" de kerberos del servidor SRODRIGUEZ.LOCAL separat per espais, és ha dir has d'indicar el "**nomservidor.nomdomini.local**".*

![Definicio-Domini-3](./Linux/Captura-4.png)

*En el següent pas et demana indicar el hostname de l'administrador del servidor SRODRIGUEZ.LOCAL.* *,és ha dir has d'indicar el nom del servidor "**hostname**" seguit del domini. "servidordhcp.srodriguez.local".*

---
### 2. Verificar que el client pot veure el servidor:

![Verificar-Conexió](./Linux/Captura-5.png)

### 3. Connectar el client linux a un usuari del servidor:

![Descobrir-Domini](./Linux/Captura-6.png)

**Unir el client al domini:**

![Unir-Client](./Linux/Captura-7.png)

**Conectarse a un usuari del Domini:**

![Conectar-Usuari](./Linux/Captura-8.png)

**Verificació:**

![Verificació](./Linux/Captura-9.png)