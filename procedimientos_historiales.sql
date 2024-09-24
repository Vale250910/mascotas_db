-- PROCEDIMIENTOS Y TRANSACCIONES - CITAS
USE mascotas_db;
DELIMITER //
CREATE PROCEDURE CrearHistorial(
	IN p_codigo VARCHAR(40),
    IN p_fecha DATE,
    IN p_descripcion TEXT,
    IN p_tratamiento TEXT,
    IN p_codigo_mascota VARCHAR(40),
    IN p_estado_acceso  ENUM('ACTIVO', 'INACTIVO')
)
BEGIN
    INSERT INTO historiales_medicos (codigo,fecha,descripcion, tratamiento,codigo_mascota,estado_acceso)
    VALUES (p_codigo,p_fecha, p_descripcion, p_tratamiento,p_codigo_mascota ,p_estado_acceso);
END //
DELIMITER ;

CALL CrearHistorial('5','2024-07-01', 'Revisión general', 'Administrar antiparasitarios','1','ACTIVO');

DELIMITER //
CREATE PROCEDURE BuscarHistorialId(
    IN p_codigo VARCHAR(40)
)
BEGIN
    SELECT * FROM historiales_medicos
    WHERE codigo = p_codigo
    AND estado_acceso ='ACTIVO';
END //
DELIMITER ;
CALL BuscarHistorialId('1');


DELIMITER //
CREATE PROCEDURE BuscarHistoriales()
BEGIN
    SELECT * FROM historiales_medicos
    WHERE estado_acceso='ACTIVO';
END //
DELIMITER ;
CALL BuscarHistoriales();

DELIMITER //
CREATE PROCEDURE ActualizarEstadoHistoriales(
    IN p_codigo VARCHAR(40),
    IN p_nuevo_estado_acceso ENUM('ACTIVO', 'INACTIVO')
)
BEGIN
    UPDATE historiales_medicos
    SET estado_acceso = p_nuevo_estado_acceso
    WHERE codigo = p_codigo;

    SELECT codigo,descripcion,estado_acceso
    FROM historiales_medicos
    WHERE codigo = p_codigo;
END//
DELIMITER ;
CALL ActualizarEstadoHistoriales('1','INACTIVO');
DELIMITER //
CREATE PROCEDURE ActualizarHistoriales(
	IN p_codigo VARCHAR(40),
    IN p_fecha DATE,
    IN p_descripcion TEXT,
    IN p_tratamiento TEXT,
    IN p_codigo_mascota VARCHAR(40)
)
BEGIN 
UPDATE historiales_medicos
SET fecha = p_fecha,
	descripcion =p_descripcion,
    tratamiento = p_tratamiento,
    codigo_mascota = p_codigo_mascota
	
WHERE codigo =p_codigo;

END //
DELIMITER;
CALL ActualizarHistoriales('1','2024-07-01', 'Revisiónes generales', 'Administrar antiparasitarios', '1')
DELIMITER //
CREATE PROCEDURE EliminarHistorialPorCodigo(
    IN p_codigo VARCHAR(40)
)
BEGIN
    DELETE FROM historiales_medicos
    WHERE codigo = p_codigo;
END //
DELIMITER ;

CALL EliminarHistorialPorCodigo('6');