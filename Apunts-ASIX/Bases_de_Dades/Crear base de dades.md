# ***Crear base de dades:***


## Motors d'emegazematge:

* myISAM és mes rapid 
* InnoDB.



**ShOW ENGINES:** Mostrar cuales son los motores que puede soportar MySQL, si permet punts de restauración, si permet transacions.


---
### Variables del sistema relacionadas con los motores de bases de datos


* &#x20;   **default-storage-engine:** Determina el motor de bases de datos por defecto.
* &#x20;   **disabled\_storage\_engines:** Determina que motores de bases de datos no pueden ser utilizados.
* &#x20;   **default\_tmp\_storage\_engine:** Determina el motor de bases de datos por defecto para tablas temporales.

---
## Motor MyISAM:
![Imatge-myISAM](https://wiki.cifprodolfoucha.es/images/6/6b/Mysql_motores_4.jpg)

**myISAM:** cada taula és guarda fisicament en 3 fitchers:


* **nombre_tabla.frm:** Guarda la definición del formato de la tabla.
* **nombre_tabla.myd (MyData):** Guarda los datos de la tabla.
* **nombre_tabla.myi (MyIndex):** Guarda los índices que tenga creada la tabla.

### Orden SQL para crear una tabla con este motor:
```sql
CREATE TABLE nombre_tabla (nombre_col tipo_dato) ENGINE = MYISAM;
```



### Características principales:


* &#x20;       **Tamaño máximo de la tabla:** 256TB.
* &#x20;       **Capacidad de almacenamiento en filas (registros):** (2^32)^2 (1.844E+19)
* &#x20;       **Número máximo de índices que podemos guardar en una tabla:** 64
* &#x20;       **Número máximo de columnas por índice:** 16

* &#x20;       **Tipos de datos sobre los que podemos crear índices:** BLOB, TEXT, y columnas con valor NULL.
* &#x20;       Bloqueo a nivel de tabla cuando hay múltiples operaciones de modificación sobre la tabla.
* &#x20;       No soporta integridad referencial.
* &#x20;       No soporta transacciones.

---

## Motor InnoDB:

![Imatge](https://wiki.cifprodolfoucha.es/images/f/f4/Mysql_motores_4B.jpg)


### Físicamente:



* &#x20;       Anteriormente a la versión 5.6.6 de Mysql, todas los datos e índices de las tablas Innodb se guardaban en un conjunto de archivos de nombre ibdata1, ibdata2, dentro del directorio de datos de Mysql. Esta forma tiene como principal inconveniente la recuperación del espacio físico por parte de tablas que hubieran crecido mucho de tamaño y que después fueran borradas.

&#x20;      Una vez ocupado el espacio, ya no se reduce.

&#x20;La forma de solucionarlo era la de hacer un backup de las bases de datos, borrar los archivos ibd y volver a recuperarlas.



* &#x20;A partir de la versión 5.7 está activada la variable del sistema innodb_file_per_table que provoca que cada tabla ocupe un archivo con extensión nombre_tabla.ibd. 

&#x20;  Existe un archivo con extensión .frm que guarda la estructura de la tabla.



### Orden SQL para crear una tabla con este motor:
```sql
CREATE TABLE nombre_tabla (nombre_col tipo_dato) ENGINE = INNODB;
```



### Características principales:

* **Tamaño máximo de la tabla:** 256TB para un tamaño de página de 64KB. Por defecto, el tamaño de página es de 16KB para un almacenamiento máximo de 64TB. El tamaño de la página viene determinado por la variable del sistema innodb_page_size.



* **Capacidad de almacenamiento en filas (registros):** Dependerá del tamaño de la fila y este depende del tamaño de la página. En el caso de un tamaño de página de 16KB el tamaño máximo por fila es de 8KB, por lo tanto el número máximo de filas sería: 64TB / 8000b = 8796093022,21 (sin contar los campos BLOB y TEXT).
* **Número de columnas:** 1017
* **Número máximo de índices que podemos guardar en una tabla:** 64
* **Número máximo de columnas por índice:** 16
* El acceso a los datos utilizando la clave primaria es muy rápido (utiliza un clustered index).
* Hacer un count(*) sobre una tabla le lleva más tiempo que en el motor anterior ya que no guarda un contador interno de filas.
* **Tipos de datos sobre los que podemos crear índices:** BLOB, TEXT, y columnas con valor NULL.
* Bloqueo a nivel de fila de datos (permite mayor concurrencia)
* Soporta integridad referencial.
* Soporta transacciones.

---


## MyIsam vs InnoDB

---

* &#x20;   Estos son los dos principales motores de almacenamiento y normalmente vais a tener que escoger uno u otro.



* &#x20;   Si los comparamos podemos llegar a las siguientes conclusiones:



* &#x20;       A nivel de velocidad, a priori, el motor MyIsam es más rápido ya que no tiene reglas de integrad referencial y no soporta transacciones, que hacen que las operaciones contra las tablas sean más lentas.
* &#x20;       En contra, MyIsam tiene un bloqueo a nivel de tabla, por lo que si vamos a realizar operaciones que impliquen modificaciones sobre los datos, las consultas se van a ralentizar.
* &#x20;       InnoDB por otro lado posee mecanismos para implementar la integridad referencial y transacciones que pueden ser necesarios en nuestra base de datos, ya que le da una mayor seguridad sobre los datos.
* &#x20;       En caso de caída del sistema, Innodb posee mecanismos de recuperación para volver a dejar a la base de datos en el estado anterior a la caída del sistema, mientras que el motor MyIsam no.

### Ventajas de InnoDB:

* &#x20;       **Velocidad:** Innodb sigue siendo más lento que MyIsam en la inserción de datos pero la diferencia cada vez es menor.
* &#x20;       **Concurrencia:** Cuando tenemos operaciones de INSERT y SELECT al mismo tiempo (de forma concurrente) al tener InnoDB un bloqueo por registro, su velocidad es mayor.
* &#x20;       **Fiabilidad:** InnoDB soporta transacciones e integridad referencial.
* &#x20;       **Seguridad de los datos:** Capacidad de recuperarse de caídas del sistema.

### Ventajas de MyISAM:

* &#x20;       **Simplicidad:** Las opciones de configuración para este motor son mínimas.
* &#x20;       **Optimización:** Es el motor que más tiempo lleva siendo utilizado por Mysql, por lo que está mas optimizado. Las aplicaciones web que en su mayor parte hacen consulta, suelen usar este motor.

Anteriormente, sólo el motor MyIsam permitía realizar búsquedas de varias palabras en cadenas de texto (denominadas búsquedas FULLTEXT) pero ahora InnoBD también las soporta, por lo que ha dejado de ser una ventaja de MyIsam.


* &#x20;       **Uso de recursos:** En general consumen menos CPU y menos espacio en disco.







