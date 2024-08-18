-- PROCEDIMIENTOS Y TRANSACCIONES - CITAS
USE mascotas_db;

DELIMITER //
CREATE PROCEDURE InsertarCita(
	IN p_codigo INT,
    IN p_fecha DATE,
    IN p_hora TIME,
    IN p_id_servicio INT,
    IN p_id_veterinario INT,
    IN p_codigo_mascota INT,
    IN p_estado ENUM('PENDIENTE', 'CONFIRMADA', 'CANCELADA', 'REALIZADA', 'NO_ASISTIDA')
)
BEGIN
    INSERT INTO citas (codigo,fecha, hora, id_servicio, id_veterinario, codigo_mascota, estado)
    VALUES (p_codigo,p_fecha, p_hora, p_id_servicio, p_id_veterinario, p_codigo_mascota, p_estado);
END //
DELIMITER ;

CALL InsertarCita(101,'2024-08-16', '14:30:00', 1, 105, 1001, 'PENDIENTE');

DELIMITER //
CREATE PROCEDURE BuscarCitaPorFecha(
    IN p_fecha DATE
)
BEGIN
    SELECT * FROM citas
    WHERE fecha = p_fecha;
END //
DELIMITER ;
CALL BuscarCitaPorFecha('2024-08-16');

DELIMITER //
CREATE PROCEDURE BuscarCitaPorMascota(
    IN p_codigo_mascota INT
)
BEGIN
    SELECT * FROM citas
    WHERE codigo_mascota = p_codigo_mascota;
END //
DELIMITER ;

CALL BuscarCitaPorMascota(1001);

DELIMITER //
CREATE PROCEDURE BuscarCitas()
BEGIN
    SELECT * FROM citas;
END //
DELIMITER ;

CALL BuscarCitas();

DELIMITER //
CREATE PROCEDURE EliminarCitaPorCodigo(
    IN p_codigo INT
)
BEGIN
    DELETE FROM citas
    WHERE codigo = p_codigo;
END //
DELIMITER ;

CALL EliminarCitaPorCodigo(101);