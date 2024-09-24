use mascotas_db
DELIMITER //

CREATE PROCEDURE InsertarProducto(
<<<<<<< HEAD
	IN p_codigo VARCHAR(40),
    IN p_nombre VARCHAR(100),
    IN p_descripcion TEXT,
    IN p_precio DECIMAL(20,2),
    IN p_stock SMALLINT,
    IN p_estado_acceso ENUM('ACTIVO', 'INACTIVO')
=======
    IN p_nombre VARCHAR(100),
    IN p_descripcion TEXT,
    IN p_precio DECIMAL(20,2),
    IN p_stock SMALLINT
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Señalar que ocurrió un error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al insertar el producto';
    END;

    -- Insertar el nuevo producto en la tabla 'productos'
<<<<<<< HEAD
    INSERT INTO productos(codigo,nombre, descripcion, precio, stock,estado_acceso)
    VALUES(p_codigo,p_nombre, p_descripcion, p_precio, p_stock,p_estado_acceso);
END //

DELIMITER ;
CALL InsertarProducto(5,'COMIDA DE PERRO', 'LABRADOR.PES', 199.99, 50,'ACTIVO');
=======
    INSERT INTO productos(nombre, descripcion, precio, stock)
    VALUES(p_nombre, p_descripcion, p_precio, p_stock);
END //

DELIMITER ;
CALL InsertarProducto('COMIDA DE PERRO', 'LABRADOR.PES', 199.99, 50);
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6


-- Procedimiento para buscar un producto por codigo

DELIMITER //

CREATE PROCEDURE BuscarProductoCodigo(
<<<<<<< HEAD
    IN p_codigo VARCHAR(40)
)
BEGIN
    SELECT *FROM productos WHERE codigo = p_codigo
    AND estado_acceso ='ACTIVO';
END //

DELIMITER ;
CALL BuscarProductoCodigo('1');
=======
    IN p_codigo INT
)
BEGIN
    SELECT *FROM productos WHERE codigo = p_codigo;
END //

DELIMITER ;
CALL BuscarProductoCodigo(1);
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
-- Buscar producto por el nombre

DELIMITER //

CREATE PROCEDURE BuscarProductosPorNombre(
    IN p_nombre VARCHAR(100)
)
BEGIN
    -- Variable para contar el número de productos encontrados
    DECLARE v_count INT DEFAULT 0;

    -- Seleccionar los productos que coinciden con el nombre proporcionado
    SELECT COUNT(*) INTO v_count
    FROM productos
<<<<<<< HEAD
    WHERE nombre LIKE CONCAT('%', p_nombre, '%')
    AND estado_acceso='ACTIVO';
=======
    WHERE nombre LIKE CONCAT('%', p_nombre, '%');
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6

    -- Comprobar si no se encontraron registros
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontraron productos con el nombre escrito';
    ELSE
        -- Seleccionar los detalles de los productos encontrados
<<<<<<< HEAD
        SELECT codigo, nombre, descripcion, precio, stock,estado_acceso
        FROM productos
        WHERE nombre LIKE CONCAT('%', p_nombre, '%')
        AND estado_acceso='ACTIVO';
=======
        SELECT codigo, nombre, descripcion, precio, stock
        FROM productos
        WHERE nombre LIKE CONCAT('%', p_nombre, '%');
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    END IF;
END //

DELIMITER ;
<<<<<<< HEAD
CALL BuscarProductosPorNombre('c');
=======
CALL BuscarProductosPorNombre('Alimento para Perro');
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
-- Buscar varios productos por el nombre
DELIMITER //

CREATE PROCEDURE BuscarTodosLosProductos(
)
BEGIN
    -- Seleccionar todos los productos que coinciden con el nombre proporcionado
    SELECT *
<<<<<<< HEAD
    FROM productos
    WHERE estado_acceso='ACTIVO';
=======
    FROM productos;
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
END //

DELIMITER ;
CALL BuscarTodosLosProductos();
-- Eliminar productos por codigo
<<<<<<< HEAD
DELIMITER //
CREATE PROCEDURE ActualizarEstadoProductos(
    IN p_codigo VARCHAR(40),
    IN p_nuevo_estado_acceso ENUM('ACTIVO', 'INACTIVO')
)
BEGIN
    UPDATE productos
    SET estado_acceso = p_nuevo_estado_acceso
    WHERE codigo = p_codigo;

    SELECT codigo,nombre,estado_acceso
    FROM productos
    WHERE codigo = p_codigo;
END//
DELIMITER ;
CALL ActualizarEstadoProductos('1','INACTIVO');

DELIMITER //
CREATE PROCEDURE ActualizarProducto(
	IN p_codigo VARCHAR(40),
=======



DELIMITER //
CREATE PROCEDURE ActualizarProducto(
	IN p_codigo INT,
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    IN p_nombre VARCHAR(100),
	IN p_descripcion TEXT,
    IN p_precio DECIMAL(20,2),
    IN p_stock SMALLINT
)
BEGIN 
UPDATE productos
SET codigo = p_codigo,
	nombre = p_nombre,
	descripcion = p_descripcion,
	precio =p_precio,
	stock = p_stock
WHERE codigo =p_codigo;

END //
<<<<<<< HEAD

CALL ActualizarProducto('1','COMIDA DE PERRO', 'LABRADOR.PES', 199.99, 50);

CREATE PROCEDURE EliminarProductoPorCodigo(
    IN p_codigo VARCHAR(40)
=======
DELIMITER;
CALL ActualizarProducto(1,'COMIDA DE PERRO', 'LABRADOR.PES', 199.99, 50)

DELIMITER //
CREATE PROCEDURE EliminarProductoPorCodigo(
    IN p_codigo INT
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
)
BEGIN
-- Declarar variable para contar productos
DECLARE v_count INT DEFAULT 0;
    -- Declarar manejador de excepciones
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
-- Señalar que ocurrió un error
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al borrar el producto';
    END;
   
    -- Verificar si el producto existe antes de intentar borrarlo
    SELECT COUNT(*)
    INTO v_count
    FROM productos
    WHERE codigo = p_codigo;

    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se encontró el producto con el código especificado';
    ELSE
        -- Borrar el producto
        DELETE FROM productos
        WHERE codigo = p_codigo;
    END IF;
END //

DELIMITER ;
CALL EliminarProductoPorCodigo(5);