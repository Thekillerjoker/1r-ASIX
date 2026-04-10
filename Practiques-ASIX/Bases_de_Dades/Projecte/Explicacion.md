No he pogut fer Funcions ni trigers perque no hem deixaba crearlos perque al ferho hem deia aixo:
SQL Error [1419] [HY000]: (conn=186) You do not have the SUPER privilege and binary logging is enabled (you *might* want to use the less safe log_bin_trust_function_creators variable) (conn=186) You do not have the SUPER privilege and binary logging is enabled (you *might* want to use the less safe log_bin_trust_function_creators variable)

Aixo vol dir que :
💥 El servidor tiene restricciones de seguridad (binlog activo)
💥 Tu usuario NO tiene permisos globales (SUPER / BINLOG ADMIN)
💥 Y RDS NO te deja cambiarlos

“Estoy usando Amazon Aurora RDS, que es un entorno gestionado. Los grupos de parámetros por defecto no permiten habilitar la creación de funciones y triggers porque requieren privilegios de sistema (SUPER o BINLOG ADMIN), que AWS no expone en este tipo de instancias. Por eso he implementado la lógica mediante procedimientos almacenados.”


Por parte de los porcedure:
El procedure de classificacio_gp :
Mostra la classificació completa d’una cursa concreta.

📌 Exemple:

li passes cursa 1
et treu:
pilots
posició final
punts

➡️ resultat: taula amb la classificació del GP

Per part del procedure pilots_equip_any:
👉 Què fa?

Mostra quins pilots han estat en un equip durant un any concret.

📌 Exemple:

equip = Red Bull
any = 2026

➡️ retorna:

noms dels pilots
contracte (any inici i fi)

#Vistes:
👁️ 2. Convé crear vistes?

👉 SÍ, és molt recomanable per
simplificar consultes
evitar JOINs repetitius
donar accés limitat als usuaris
“Les vistes permeten als usuaris consultar informació sense accedir directament a totes les taules.”
La vista classificacio_gp:

🎯 FUNCIÓN DE LA VISTA

👉 Esta vista sirve para:

Mostrar la clasificación de los pilotos en cada Gran Premio, incluyendo su información personal y sus resultados.

EXPLICACIÓN PASO A PASO
🧩 1. Usa la tabla RESULTATS

Contiene:

qué piloto participó
en qué carrera (cursa_id)
su posición final
los puntos


🧩 2. Hace un JOIN con PILOTS
JOIN PILOTS p ON r.pilot_id = p.pilot_id;

👉 Para añadir:

nombre (nom)
apellido (cognom)

EN UNA FRASE (IMPORTANTE PARA EXAMEN)

“La vista vista_classificacio_gp permite consultar de forma sencilla la clasificación de los pilotos en cada Gran Premio, combinando los resultados con la información de los pilotos sin necesidad de realizar joins manualmente.”

Segunda vista:
🎯 FUNCIÓN DE LA VISTA

👉 Esta vista sirve para:

Calcular y mostrar el total de puntos acumulados por cada piloto en todas las carreras.

🔍 EXPLICACIÓN PASO A PASO
🧩 1. Usa la tabla PILOTS
```sql
JOIN RESULTATS r ON p.pilot_id = r.pilot_id
```

Contiene:

ID del piloto
nombre (nom)
apellido (cognom)


🧩 2. Hace un JOIN con RESULTATS
JOIN RESULTATS r ON p.pilot_id = r.pilot_id

👉 Para obtener los puntos (punts) de cada carrera


🧩 3. Suma los puntos
```sql
SUM(r.punts) AS total_punts
```
👉 Calcula los puntos totales de cada piloto

4. Agrupa por piloto
```sql
GROUP BY p.pilot_id;
```

👉 Junta todas las carreras de cada piloto en una sola fila

EN UNA FRASE (IMPORTANTE PARA EXAMEN)

“La vista vista_punts_pilots permite obtener el total de puntos acumulados por cada piloto, agregando los resultados de todas las carreras mediante una función de suma y agrupación.”
⚡ 3. Cal indexar columnes?

👉 SÍ, per millorar:

JOINs
filtres (WHERE)
agrupacions (GROUP BY).
