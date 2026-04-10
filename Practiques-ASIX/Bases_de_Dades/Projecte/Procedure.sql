/* Procedure para mostrar la clasificación completa de  una carrera concreta*/

DELIMITER //

CREATE PROCEDURE classificacio_gp(IN id_cursa INT)
BEGIN
    SELECT 
        r.posicio_final,
        p.nom,
        p.cognom,
        r.punts
    FROM RESULTATS r
    JOIN PILOTS p ON r.pilot_id = p.pilot_id
    WHERE r.cursa_id = id_cursa
    ORDER BY r.punts DESC;
END //

DELIMITER ;

/* Procedure para mostrar que ppilotos han estado en un equipo durante un año completo*/

DELIMITER //

CREATE PROCEDURE pilots_equip_any(IN id_equip INT, IN any_cerca INT)
BEGIN
    SELECT 
        p.nom,
        p.cognom,
        c.any_inici,
        c.any_fi
    FROM CONTRACTES c
    JOIN PILOTS p ON c.pilot_id = p.pilot_id
    WHERE c.equip_id = id_equip
      AND any_cerca BETWEEN c.any_inici AND c.any_fi;
END //

DELIMITER ;

/* Funcio 1 per Devuelve los puntos totales de un piloto */
DELIMITER //

CREATE FUNCTION total_punts_pilot(p_id INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total INT;

    SELECT IFNULL(SUM(punts), 0)
    INTO total
    FROM RESULTATS
    WHERE pilot_id = p_id;

    RETURN total;
END//

DELIMITER ;

/* Funcio 2 per Devuelve cuántas carreras ha corrido un piloto*/
DELIMITER //

CREATE FUNCTION total_curses_pilot(p_id INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total INT;

    SELECT COUNT(*)
    INTO total
    FROM RESULTATS
    WHERE pilot_id = p_id;

    RETURN total;
END//

DELIMITER ;