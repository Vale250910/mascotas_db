-- PROCEDIMIENTOS Y TRANSACCIONES - CITAS
USE mascotas_db;

DELIMITER //
CREATE PROCEDURE InsertarCita(
<<<<<<< HEAD
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
=======
    IN p_fecha DATE,
    IN p_hora TIME,
    IN p_id_servicio INT,
    IN p_id_veterinario INT,
    IN p_codigo_mascota INT,
    IN p_estado ENUM('PENDIENTE', 'CONFIRMADA', 'CANCELADA', 'REALIZADA', 'NO_ASISTIDA')
)
BEGIN
    INSERT INTO citas (fecha, hora, id_servicio, id_veterinario, codigo_mascota, estado)
    VALUES (p_fecha, p_hora, p_id_servicio, p_id_veterinario, p_codigo_mascota, p_estado);
END //
DELIMITER ;

CALL InsertarCita('2024-08-16', '14:30:00', 1, 105, 1, 'PENDIENTE');

DELIMITER //
CREATE PROCEDURE BuscarCitaPorId(
    IN p_codigo INT
)
BEGIN
    SELECT * FROM citas
    WHERE codigo = p_codigo;
END //
DELIMITER ;
CALL BuscarCitaPorId(1);
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6

DELIMITER //
CREATE PROCEDURE BuscarCitaPorFecha(
    IN p_fecha DATE
)
BEGIN
    SELECT * FROM citas
<<<<<<< HEAD
    WHERE fecha = p_fecha
     AND estado_acceso='ACTIVO';
=======
    WHERE fecha = p_fecha;
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
END //
DELIMITER ;
CALL BuscarCitaPorFecha('2024-02-25');

DELIMITER //
CREATE PROCEDURE BuscarCitas()
BEGIN
<<<<<<< HEAD
    SELECT * FROM citas
    WHERE estado_acceso='ACTIVO';
=======
    SELECT * FROM citas;
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
END //
DELIMITER ;

CALL BuscarCitas();

DELIMITER //
<<<<<<< HEAD
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
=======
CREATE PROCEDURE ActualizarCitas(
	IN p_codigo INT,
	IN p_fecha DATE,
    IN p_hora TIME,
    IN p_id_servicio INT,
    IN p_id_veterinario INT,
    IN p_codigo_mascota INT,
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    IN p_estado ENUM('PENDIENTE', 'CONFIRMADA', 'CANCELADA', 'REALIZADA', 'NO_ASISTIDA')
)
BEGIN 
UPDATE citas
<<<<<<< HEAD
SET 
	fecha = p_fecha,
	hora =p_hora,
    id_servicio =p_id_servicio,
    n_documento = p_n_documento,
=======
SET codigo = p_codigo,
	fecha = p_fecha,
	hora =p_hora,
    id_servicio = p_id_servicio,
    id_veterinario = p_id_veterinario,
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    codigo_mascota = p_codigo_mascota,
	estado = p_estado
WHERE codigo =p_codigo;

END //
DELIMITER;
<<<<<<< HEAD
CALL ActualizarCitas('1','2024-02-23','02:02:00','PENDIENTE')
DELIMITER //
CREATE PROCEDURE EliminarCitaPorCodigo(
    IN p_codigo VARCHAR(40)
=======
CALL ActualizarCitas(1,'2024-02-23','02:02:00',1,107,2,'PENDIENTE')
DELIMITER //
CREATE PROCEDURE EliminarCitaPorCodigo(
    IN p_codigo INT
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
)
BEGIN
    DELETE FROM citas
    WHERE codigo = p_codigo;
END //
DELIMITER ;

<<<<<<< HEAD
CALL EliminarCitaPorCodigo('101');
=======
CALL EliminarCitaPorCodigo(7);
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
