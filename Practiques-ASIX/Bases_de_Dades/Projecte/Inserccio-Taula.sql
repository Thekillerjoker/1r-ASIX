INSERT INTO PILOTS (pilot_id, nom, cognom, pais, data_naixement, dorsal)
VALUES
(1, 'Max', 'Verstappen', 'Països Baixos', '1997-09-30', 1),
(2, 'Charles', 'Leclerc', 'Mònaco', '1997-10-16', 16),
(3, 'Lewis', 'Hamilton', 'Regne Unit', '1985-01-07', 44),
(4, 'Lando', 'Norris', 'Regne Unit', '1999-11-13', 4),
(5, 'Oscar', 'Piastri', 'Austràlia', '2001-04-06', 81),
(6, 'George', 'Russell', 'Regne Unit', '1998-02-15', 63),
(7, 'Fernando', 'Alonso', 'Espanya', '1981-07-29', 14),
(8, 'Lance', 'Stroll', 'Canadà', '1998-10-29', 18),
(9, 'Nico', 'Hulkenberg', 'Alemanya', '1987-08-19', 27),
(10, 'Pierre', 'Gasly', 'França', '1996-02-07', 10),
(11, 'Franco', 'Colapinto', 'Argentina', '2005-03-05', 11),
(12, 'Sergio', 'Perez', 'Mèxic', '1990-01-26', 11),
(13, 'Valtteri', 'Bottas', 'Finlàndia', '1989-08-28', 77),
(14, 'Isack', 'Hadjar', 'França', NULL, 10),
(15, 'Oliver', 'Bearman', 'Regne Unit', '2005-08-10', 21),
(16, 'Kimi', 'Antonelli', 'Itàlia', '2006-02-25', 81),
(17, 'Liam', 'Lawson', 'Nova Zelanda', '2002-02-11', 63),
(18, 'Arvid', 'Lindblad', 'Suècia', '2005-08-14', 68),
(19, 'Carlos', 'Sainz', 'Espanya', '1994-09-01', 55),
(20, 'Alexander', 'Albon', 'Tailàndia', '1996-03-23', 23);

INSERT INTO EQUIPS (equip_id, nom, pais, any_fundacio)
VALUES
(1, 'Red Bull Racing', 'Àustria', 2005),
(2, 'Ferrari', 'Itàlia', 1929),
(3, 'Mercedes', 'Alemanya', 2010),
(4, 'McLaren', 'Regne Unit', 1963),
(5, 'Alpine', 'França', 2021),
(6, 'Aston Martin', 'Regne Unit', 1913),
(7, 'Audi', 'Alemanya', 2026),
(8, 'Williams', 'Regne Unit', 1977),
(9, 'Haas F1 Team', 'Estats Units', 2016),
(10, 'Racing Bulls', 'Àustria', 2026);

INSERT INTO CIRCUITS (circuit_id, nom, ciutat, pais, longitud_km, record)
VALUES
(1, 'Silverstone Circuit', 'Silverstone', 'Regne Unit', 5.891, '00:01:27.097'),
(2, 'Monza', 'Monza', 'Itàlia', 5.793, '00:01:21.046'),
(3, 'Spa-Francorchamps', 'Spa', 'Bèlgica', 7.004, '00:01:46.286'),
(4, 'Circuit de Barcelona-Catalunya', 'Montmeló', 'Espanya', 4.655, '00:01:18.183'),
(5, 'Marina Bay Street Circuit', 'Singapur', 'Singapur', 5.063, '00:01:41.905'),
(6, 'Circuit Gilles Villeneuve', 'Mont-real', 'Canadà', 4.361, '00:01:13.078'),
(7, 'Suzuka Circuit', 'Suzuka', 'Japó', 5.807, '00:01:30.983'),
(8, 'Yas Marina Circuit', 'Abu Dhabi', 'Emirats Àrabs Units', 5.554, '00:01:26.103');

INSERT INTO GP (cursa_id, nom, data, voltes, circuit_id)
VALUES
(1, 'Gran Premi de Gran Bretanya', '2026-07-10', 52, 1),
(2, 'Gran Premi de Italia', '2026-09-05', 53, 2),
(3, 'Gran Premi de Bèlgica', '2026-08-23', 44, 3),
(4, 'Gran Premi d’Espanya', '2026-06-06', 66, 4),
(5, 'Gran Premi de Singapur', '2026-10-01', 61, 5),
(6, 'Gran Premi del Canadà', '2026-07-18', 70, 6),
(7, 'Gran Premi del Japó', '2026-09-20', 53, 7),
(8, 'Gran Premi dels Emirats', '2026-11-04', 55, 8);

INSERT INTO RESULTATS (cursa_id, pilot_id, posicio_inicial, posicio_final, punts)
VALUES
(1, 4, 3, '1r', 25),
(1, 5, 2, '2gn', 18),
(1, 9, 19, '3r', 15),
(1, 3, 5, '4rt', 12),
(1, 1, 1, '5e', 10),
(1, 10, 8, '6e', 8),
(1, 8, 17, '7e', 6),
(1, 20, 13, '8e', 4),
(1, 7, 7, '9e', 2),
(1, 6, 4, '10', 1),
(1, 15, 18, '11e', 0),
(1, 19, 9, '12e', 0),
(2, 1, 1, '1r', 25),
(2, 4, 2, '2gn', 18),
(2, 5, 3, '3r', 15),
(2, 2, 4, '4rt', 12),
(2, 6, 5, '5e', 10),
(3, 5, 2, '1er', 25),
(3, 4, 1, '2gn', 18),
(3, 2, 3, '3r', 15);

INSERT INTO CONTRACTES (pilot_id, equip_id, any_inici, any_fi)
VALUES
(1, 1, 2021, 2026),
(2, 2, 2019, 2026),
(3, 3, 2013, 2026),
(4, 4, 2019, 2026),
(5, 4, 2025, 2026),
(6, 3, 2022, 2026),
(7, 6, 2023, 2026),
(8, 6, 2023, 2026),
(9, 7, 2026, 2026),
(10, 5, 2023, 2026),
(11, 5, 2026, 2026),
(12, 8, 2021, 2026),
(13, 8, 2025, 2026),
(14, 10, 2026, 2026),
(15, 9, 2025, 2026),
(16, 3, 2026, 2026),
(17, 10, 2026, 2026),
(18, 10, 2026, 2026),
(19, 2, 2023, 2026),
(20, 8, 2024, 2026);
