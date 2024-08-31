-- PROCEDIMIENTOS Y TRANSACCIONES - CITAS
USE mascotas_db;

DELIMITER //
CREATE PROCEDURE InsertarCita(
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

DELIMITER //
CREATE PROCEDURE BuscarCitaPorFecha(
    IN p_fecha DATE
)
BEGIN
    SELECT * FROM citas
    WHERE fecha = p_fecha;
END //
DELIMITER ;
CALL BuscarCitaPorFecha('2024-02-25');

DELIMITER //
CREATE PROCEDURE BuscarCitas()
BEGIN
    SELECT * FROM citas;
END //
DELIMITER ;

CALL BuscarCitas();

DELIMITER //
CREATE PROCEDURE ActualizarCitas(
	IN p_codigo INT,
	IN p_fecha DATE,
    IN p_hora TIME,
    IN p_id_servicio INT,
    IN p_id_veterinario INT,
    IN p_codigo_mascota INT,
    IN p_estado ENUM('PENDIENTE', 'CONFIRMADA', 'CANCELADA', 'REALIZADA', 'NO_ASISTIDA')
)
BEGIN 
UPDATE citas
SET codigo = p_codigo,
	fecha = p_fecha,
	hora =p_hora,
    id_servicio = p_id_servicio,
    id_veterinario = p_id_veterinario,
    codigo_mascota = p_codigo_mascota,
	estado = p_estado
WHERE codigo =p_codigo;

END //
DELIMITER;
CALL ActualizarCitas(1,'2024-02-23','02:02:00',1,107,2,'PENDIENTE')
DELIMITER //
CREATE PROCEDURE EliminarCitaPorCodigo(
    IN p_codigo INT
)
BEGIN
    DELETE FROM citas
    WHERE codigo = p_codigo;
END //
DELIMITER ;

CALL EliminarCitaPorCodigo(7);