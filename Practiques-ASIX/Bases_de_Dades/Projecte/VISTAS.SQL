/*Vista Clasificacio d'un gp*/
CREATE VIEW vista_classificacio_gp AS
SELECT 
    r.cursa_id,
    r.pilot_id,
    p.nom,
    p.cognom,
    r.posicio_final,
    r.punts
FROM RESULTATS r
JOIN PILOTS p ON r.pilot_id = p.pilot_id;


/* Vista de punts totals */

CREATE VIEW vista_punts_pilots AS
SELECT 
    p.pilot_id,
    p.nom,
    p.cognom,
    SUM(r.punts) AS total_punts
FROM PILOTS p
JOIN RESULTATS r ON p.pilot_id = r.pilot_id
GROUP BY p.pilot_id;