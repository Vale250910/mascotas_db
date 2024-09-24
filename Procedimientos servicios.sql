DELIMITER //
CREATE PROCEDURE InsertarServicio(
<<<<<<< HEAD
    IN p_codigo VARCHAR(40),
    IN p_nombre VARCHAR(100),
    IN p_descripcion TEXT,
    IN p_precio DECIMAL(20,2),
    IN p_estado_acceso ENUM('ACTIVO', 'INACTIVO')
)
BEGIN
    INSERT INTO servicios (codigo, nombre, descripcion, precio,estado_acceso)
    VALUES (p_codigo, p_nombre, p_descripcion, p_precio,p_estado_acceso);
END //
DELIMITER ;

CALL InsertarServicio('2001', 'Baño Completo', 'Servicio de baño completo para mascotas, incluye corte de pelo.', 50.00,'ACTIVO');
=======
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
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
#Buscar servicio por codigo

DELIMITER //
CREATE PROCEDURE BuscarServicioPorCodigo(
<<<<<<< HEAD
    IN p_codigo VARCHAR(40)
)
BEGIN
    SELECT * FROM servicios
    WHERE codigo = p_codigo
    AND estado_acceso='ACTIVO';
END //
DELIMITER ;

CALL BuscarServicioPorCodigo('1');
=======
    IN p_codigo INT UNSIGNED
)
BEGIN
    SELECT * FROM servicios
    WHERE codigo = p_codigo;
END //
DELIMITER ;

CALL BuscarServicioPorCodigo(1);
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
#Buscar Servicio por nombre

DELIMITER //
CREATE PROCEDURE BuscarServicioPorNombre(
    IN p_nombre VARCHAR(100)
)
BEGIN
    SELECT * FROM servicios
<<<<<<< HEAD
    WHERE nombre LIKE CONCAT('%', p_nombre, '%')
    AND estado_acceso='ACTIVO';
=======
    WHERE nombre LIKE CONCAT('%', p_nombre, '%');
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
END //
DELIMITER ;

CALL BuscarServicioPorNombre('Baño Completo');
#Buscar servicios

DELIMITER //
CREATE PROCEDURE BuscarServicios()
BEGIN
<<<<<<< HEAD
    SELECT * FROM servicios
    WHERE estado_acceso='ACTIVO';
=======
    SELECT * FROM servicios;
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
END //
DELIMITER ;

CALL BuscarServicios();
<<<<<<< HEAD
DELIMITER //
CREATE PROCEDURE ActualizarEstadoServicios(
    IN p_codigo VARCHAR(40),
    IN p_nuevo_estado_acceso ENUM('ACTIVO', 'INACTIVO')
)
BEGIN
    UPDATE servicios
    SET estado_acceso = p_nuevo_estado_acceso
    WHERE codigo = p_codigo;

    SELECT codigo,nombre,estado_acceso
    FROM servicios
    WHERE codigo = p_codigo;
END//
DELIMITER ;
CALL ActualizarEstadoServicios('1','INACTIVO');

DELIMITER //
CREATE PROCEDURE EliminarServicio(
    IN p_codigo VARCHAR(40)
=======

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
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
)
BEGIN
    DELETE FROM servicios
    WHERE codigo = p_codigo;
END //
DELIMITER ;

<<<<<<< HEAD
CALL EliminarServicio('2001');

DELIMITER //
CREATE PROCEDURE ActualizarServicios(
	IN p_codigo VARCHAR(40),
	IN p_nombre VARCHAR(100),
    IN p_descripcion TEXT,
    IN p_precio DECIMAL(20,2)
)
BEGIN 
UPDATE servicios
SET
	nombre = p_nombre,
	descripcion = p_descripcion,
	precio =p_precio
WHERE codigo =p_codigo;

END //
CALL ActualizarServicios('1','Baño Completo', 'Servicio de baño completo para mascotas, incluye corte de pelo.', 50.00);
#Buscar eliminar

=======
CALL EliminarServicio(6);
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
