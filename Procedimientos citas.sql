-- PROCEDIMIENTOS Y TRANSACCIONES - CITAS
USE mascotas_db;

DELIMITER //
CREATE PROCEDURE InsertarCita(
	IN p_codigo VARCHAR(40),
    IN p_fecha DATE,
    IN p_hora TIME,
    IN p_id_servicio VARCHAR(40),
    IN p_n_documento VARCHAR(40),
    IN p_codigo_mascota VARCHAR(40),
    IN p_estado ENUM('PENDIENTE', 'CONFIRMADA', 'CANCELADA', 'REALIZADA', 'NO_ASISTIDA'),
    IN p_estado_acceso ENUM('ACTIVO', 'INACTIVO')
)
BEGIN
    INSERT INTO citas (codigo,fecha, hora, id_servicio, n_documento, codigo_mascota, estado,estado_acceso)
    VALUES (p_codigo,p_fecha, p_hora, p_id_servicio, p_n_documento, p_codigo_mascota, p_estado,p_estado_acceso);
END //
DELIMITER ;

CALL InsertarCita('101','2024-08-16', '14:30:00', 1, 105, 1, 'PENDIENTE','ACTIVO');

DELIMITER //
CREATE PROCEDURE BuscarCitaPorId(
    IN p_codigo VARCHAR(40)
)
BEGIN
    SELECT * FROM citas
    WHERE codigo = p_codigo
	AND estado_acceso='ACTIVO';
END //
DELIMITER ;
CALL BuscarCitaPorId('1');

DELIMITER //
CREATE PROCEDURE BuscarCitaPorFecha(
    IN p_fecha DATE
)
BEGIN
    SELECT * FROM citas
    WHERE fecha = p_fecha
     AND estado_acceso='ACTIVO';
END //
DELIMITER ;
CALL BuscarCitaPorFecha('2024-02-25');

DELIMITER //
CREATE PROCEDURE BuscarCitas()
BEGIN
    SELECT * FROM citas
    WHERE estado_acceso='ACTIVO';
END //
DELIMITER ;

CALL BuscarCitas();

DELIMITER //
CREATE PROCEDURE ActualizarEstadoCitas(
    IN p_codigo VARCHAR(40),
    IN p_nuevo_estado_acceso ENUM('ACTIVO', 'INACTIVO')
)
BEGIN
    UPDATE citas
    SET estado_acceso = p_nuevo_estado_acceso
    WHERE codigo = p_codigo;

    SELECT codigo,estado_acceso
    FROM citas
    WHERE codigo = p_codigo;
END//
DELIMITER ;
CALL ActualizarEstadoCitas('1','INACTIVO');

DELIMITER //
CREATE PROCEDURE ActualizarCitas(
	IN p_codigo VARCHAR(40),
    IN p_fecha DATE,
    IN p_hora TIME,
    IN p_id_servicio VARCHAR(40),
    IN p_n_documento VARCHAR(40),
    IN p_codigo_mascota VARCHAR(40),
    IN p_estado ENUM('PENDIENTE', 'CONFIRMADA', 'CANCELADA', 'REALIZADA', 'NO_ASISTIDA')
)
BEGIN 
UPDATE citas
SET 
	fecha = p_fecha,
	hora =p_hora,
    id_servicio =p_id_servicio,
    n_documento = p_n_documento,
    codigo_mascota = p_codigo_mascota,
	estado = p_estado
WHERE codigo =p_codigo;

END //
DELIMITER;
CALL ActualizarCitas('1','2024-02-23','02:02:00','PENDIENTE')
DELIMITER //
CREATE PROCEDURE EliminarCitaPorCodigo(
    IN p_codigo VARCHAR(40)
)
BEGIN
    DELETE FROM citas
    WHERE codigo = p_codigo;
END //
DELIMITER ;

CALL EliminarCitaPorCodigo('101');