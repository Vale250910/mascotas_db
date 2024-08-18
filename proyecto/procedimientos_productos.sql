use mascotas_db
DELIMITER //

CREATE PROCEDURE InsertarProducto(
	IN p_codigo INT,
    IN p_nombre VARCHAR(100),
    IN p_descripcion TEXT,
    IN p_precio DECIMAL(20,2),
    IN p_stock SMALLINT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Señalar que ocurrió un error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al insertar el producto';
    END;

    -- Insertar el nuevo producto en la tabla 'productos'
    INSERT INTO productos(codigo,nombre, descripcion, precio, stock)
    VALUES(p_codigo,p_nombre, p_descripcion, p_precio, p_stock);
END //

DELIMITER ;
CALL InsertarProducto(5,'COMIDA DE PERRO', 'LABRADOR.PES', 199.99, 50);


-- Procedimiento para buscar un producto por codigo

DELIMITER //

CREATE PROCEDURE BuscarProductoPorCodigo(
    IN p_codigo INT
)
BEGIN
    -- Variable para almacenar el resultado
    DECLARE v_nombre VARCHAR(100);
    DECLARE v_descripcion TEXT;
    DECLARE v_precio DECIMAL(20, 2);
    DECLARE v_stock SMALLINT;

    -- Variable para comprobar si existe el producto
    DECLARE v_count INT DEFAULT 0;

    -- Contar el número de registros que coinciden
    SELECT COUNT(*)
    INTO v_count
    FROM productos
    WHERE codigo = p_codigo;

    -- Comprobar si no se encontraron registros
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró el producto con el código especificado';
    ELSE
        -- Obtener los datos del producto
        SELECT nombre, descripcion, precio, stock
        INTO v_nombre, v_descripcion, v_precio, v_stock
        FROM productos
        WHERE codigo = p_codigo;

        -- Devolver los resultados
        SELECT v_nombre AS nombre,
               v_descripcion AS descripcion,
               v_precio AS precio,
               v_stock AS stock;
    END IF;
END //

DELIMITER ;
CALL BuscarProductoPorCodigo(1);
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
    WHERE nombre LIKE CONCAT('%', p_nombre, '%');

    -- Comprobar si no se encontraron registros
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontraron productos con el nombre escrito';
    ELSE
        -- Seleccionar los detalles de los productos encontrados
        SELECT codigo, nombre, descripcion, precio, stock
        FROM productos
        WHERE nombre LIKE CONCAT('%', p_nombre, '%');
    END IF;
END //

DELIMITER ;
CALL BuscarProductosPorNombre('Alimento para Perro');
-- Buscar varios productos por el nombre
DELIMITER //

CREATE PROCEDURE BuscarTodosLosProductos(
)
BEGIN
    -- Seleccionar todos los productos que coinciden con el nombre proporcionado
    SELECT *
    FROM productos;
END //

DELIMITER ;
CALL BuscarTodosLosProductos();
-- Eliminar productos por codigo

DELIMITER //

CREATE PROCEDURE EliminarProductoPorCodigo(
    IN p_codigo INT
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