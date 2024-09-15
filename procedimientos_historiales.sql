-- PROCEDIMIENTOS Y TRANSACCIONES - CITAS
USE mascotas_db;

DELIMITER //
CREATE PROCEDURE CrearHistorial(
    IN p_fecha DATE,
    IN p_descripcion TEXT,
    IN p_tratamiento TEXT,
    IN p_codigo_mascota INT
    
)
BEGIN
    INSERT INTO historiales_medicos (fecha,descripcion, tratamiento,codigo_mascota)
    VALUES (p_fecha, p_descripcion, p_tratamiento, p_codigo_mascota);
END //
DELIMITER ;

CALL CrearHistorial('2024-07-01', 'Revisión general', 'Administrar antiparasitarios', 1);

DELIMITER //
CREATE PROCEDURE BuscarHistorialId(
    IN p_codigo INT
)
BEGIN
    SELECT * FROM historiales_medicos
    WHERE codigo = p_codigo;
END //
DELIMITER ;
CALL BuscarHistorialId(1);


DELIMITER //
CREATE PROCEDURE BuscarHistoriales()
BEGIN
    SELECT * FROM historiales_medicos;
END //
DELIMITER ;

CALL BuscarHistoriales();

DELIMITER //
CREATE PROCEDURE ActualizarHistoriales(
	IN p_codigo INT,
    IN p_fecha DATE,
    IN p_descripcion TEXT,
    IN p_tratamiento TEXT,
    IN p_codigo_mascota INT
)
BEGIN 
UPDATE historiales_medicos
SET codigo = p_codigo,
	fecha = p_fecha,
	descripcion =p_descripcion,
    tratamiento = p_tratamiento,
    codigo_mascota = p_id_mascota
	
WHERE codigo =p_codigo;

END //
DELIMITER;
CALL ActualizarHistoriales(1,'2024-07-01', 'Revisiónes generales', 'Administrar antiparasitarios', 1)
DELIMITER //
CREATE PROCEDURE EliminarHistorialPorCodigo(
    IN p_codigo INT
)
BEGIN
    DELETE FROM historiales_medicos
    WHERE codigo = p_codigo;
END //
DELIMITER ;

CALL EliminarHistorialPorCodigo(6);