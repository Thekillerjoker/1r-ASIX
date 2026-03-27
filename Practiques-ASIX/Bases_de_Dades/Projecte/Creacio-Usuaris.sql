CREATE USER 'admin_f1'@'localhost' IDENTIFIED BY 'Puertollano0101!';
GRANT ALL PRIVILEGES ON Formula1.* TO 'admin_f1'@'localhost';
FLUSH PRIVILEGES;

CREATE USER 'programador_f1'@'localhost' IDENTIFIED BY 'Programdor1234!';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER ON Formula1.* TO 'programador_f1'@'localhost';
FLUSH PRIVILEGES;

CREATE USER 'usuarir_f1'@'localhost' IDENTIFIED BY 'UsuariSegura123!';
GRANT SELECT ON Formula1.* TO 'usuarir_f1'@'localhost';
FLUSH PRIVILEGES;