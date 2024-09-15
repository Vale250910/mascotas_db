DELIMITER //
CREATE PROCEDURE InsertarServicio(
    IN p_nombre VARCHAR(100),
    IN p_descripcion TEXT,
    IN p_precio DECIMAL(20,2)
)
BEGIN
    INSERT INTO servicios (nombre, descripcion, precio)
    VALUES (p_nombre, p_descripcion, p_precio);
END //
DELIMITER ;

CALL InsertarServicio('Baño Completo', 'Servicio de baño completo para mascotas, incluye corte de pelo.', 50.00);
#Buscar servicio por codigo

DELIMITER //
CREATE PROCEDURE BuscarServicioPorCodigo(
    IN p_codigo INT UNSIGNED
)
BEGIN
    SELECT * FROM servicios
    WHERE codigo = p_codigo;
END //
DELIMITER ;

CALL BuscarServicioPorCodigo(1);
#Buscar Servicio por nombre

DELIMITER //
CREATE PROCEDURE BuscarServicioPorNombre(
    IN p_nombre VARCHAR(100)
)
BEGIN
    SELECT * FROM servicios
    WHERE nombre LIKE CONCAT('%', p_nombre, '%');
END //
DELIMITER ;

CALL BuscarServicioPorNombre('Baño Completo');
#Buscar servicios

DELIMITER //
CREATE PROCEDURE BuscarServicios()
BEGIN
    SELECT * FROM servicios;
END //
DELIMITER ;

CALL BuscarServicios();

DELIMITER //
CREATE PROCEDURE ActualizarServicios(
	IN p_codigo INT,
	IN p_nombre VARCHAR(100),
    IN p_descripcion TEXT,
    IN p_precio DECIMAL(20,2)
)
BEGIN 
UPDATE servicios
SET codigo = p_codigo,
	nombre = p_nombre,
	descripcion = p_descripcion,
	precio =p_precio
WHERE codigo =p_codigo;

END //
DELIMITER;
CALL ActualizarServicios(1,'Baño Completo', 'Servicio de baño completo para mascotas, incluye corte de pelo.', 50.00);
#Buscar eliminar

DELIMITER //
CREATE PROCEDURE EliminarServicio(
    IN p_codigo INT UNSIGNED
)
BEGIN
    DELETE FROM servicios
    WHERE codigo = p_codigo;
END //
DELIMITER ;

CALL EliminarServicio(6);