CREATE TABLE PILOTS (
	pilot_id INT,
	nom VARCHAR(20) NOT NULL,
	cognom VARCHAR(30) NOT NULL,
	pais VARCHAR(20),
	data_naixement DATE,
	dorsal INT NOT NULL,
	CONSTRAINT PK_pilots PRIMARY KEY (pilot_id)
);
CREATE TABLE EQUIPS (
	equip_id INT,
	nom VARCHAR(20) NOT NULL,
	pais VARCHAR(20),
	any_fundacio YEAR NOT NULL,
	CONSTRAINT PK_equips PRIMARY KEY (equip_id)
);
CREATE TABLE CIRCUITS (
	circuit_id INT,
	nom VARCHAR(50) NOT NULL,
	ciutat VARCHAR(30) NOT NULL,
	pais VARCHAR(30) NOT NULL,
	longitud_km DECIMAL(5,3) NOT NULL,
	record TIME(3),
	CONSTRAINT PK_circuits PRIMARY KEY (circuit_id),
	CONSTRAINT UK_nom_circuit UNIQUE (nom, ciutat)
);
CREATE TABLE GP (
	cursa_id INT,
	nom VARCHAR(30) NOT NULL,
	data DATE NOT NULL,
	voltes INT,
	circuit_id INT,
	CONSTRAINT PK_GP PRIMARY KEY (cursa_id),
	CONSTRAINT FK_circuit FOREIGN KEY (circuit_id)
				REFERENCES CIRCUITS(circuit_id)
);

CREATE TABLE RESULTATS (
	cursa_id INT,
	pilot_id INT,
	posicio_inicial INT NOT NULL,
	posicio_final VARCHAR(4) NOT NULL,
	punts INT DEFAULT 0,
	CONSTRAINT PK_Resultats PRIMARY KEY (cursa_id, pilot_id),
	CONSTRAINT FK_Resultats_GP FOREIGN KEY (cursa_id)
				REFERENCES GP(cursa_id),
	CONSTRAINT FK_Resultats_Pilot FOREIGN KEY (pilot_id)
				REFERENCES PILOTS(pilot_id)
);
CREATE TABLE CONTRACTES (
	pilot_id INT,
	equip_id INT,
	any_inici YEAR NOT NULL,
	any_fi YEAR NOT NULL,
	CONSTRAINT PK_Contractes PRIMARY KEY (pilot_id, equip_id, any_inici),
	CONSTRAINT FK_Contractes_Pilots FOREIGN KEY (pilot_id)
				REFERENCES PILOTS(pilot_id),
	CONSTRAINT FK_Contractes_Equip FOREIGN KEY (equip_id)
				REFERENCES EQUIPS(equip_id),
	CONSTRAINT CK_Any CHECK (any_fi >= any_inici)
);