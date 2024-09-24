use mascotas_db;
DELIMITER //
CREATE PROCEDURE InsertarPropietario(
	IN p_tipo_documento ENUM('C.C','C.E','T.I'),
    IN p_n_documento VARCHAR(40),
    IN p_nombre VARCHAR(50),
    IN p_apellido VARCHAR(30),
    IN p_ciudad VARCHAR(50),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(20),
    IN p_es_propietario BOOLEAN,
    IN p_es_veterinario BOOLEAN,
    IN p_es_administrador BOOLEAN,
    IN p_email VARCHAR(100),
    IN p_contraseña VARCHAR(255),
    IN p_estado_acceso ENUM('ACTIVO', 'INACTIVO') ,
    IN p_barrio VARCHAR(100)
)
BEGIN
    DECLARE exit handler for sqlexception
    BEGIN
        ROLLBACK;
        SELECT 'Error: La transacción ha sido revertida' AS Mensaje;
    END;
    START TRANSACTION;
    IF EXISTS (SELECT 1 FROM usuarios WHERE n_documento = p_n_documento) THEN
        SELECT 'Usuario ya existe en la tabla usuarios' AS Mensaje;
    ELSE
        INSERT INTO usuarios (tipo_documento,n_documento, nombre, apellido, ciudad, direccion, telefono, es_propietario, es_veterinario, es_administrador, email, contraseña, estado_acceso)
        VALUES (p_tipo_documento,p_n_documento, p_nombre, p_apellido, p_ciudad, p_direccion, p_telefono, p_es_propietario, p_es_veterinario, p_es_administrador, p_email, p_contraseña, p_estado_acceso);
        IF ROW_COUNT() = 0 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Error: No se pudo insertar en la tabla usuarios';
        END IF;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM propietarios WHERE n_documento = p_n_documento) THEN
        INSERT INTO propietarios (n_documento, barrio)
        VALUES (p_n_documento, p_barrio);
        IF ROW_COUNT() = 0 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Error: No se pudo insertar en la tabla propietarios';
        END IF;
        SELECT 'Propietario insertado exitosamente' AS Mensaje;
    ELSE
        SELECT 'Propietario ya existe en la tabla propietarios' AS Mensaje;
    END IF;
    COMMIT;
END//
DELIMITER ;

CALL InsertarPropietario(
	'C.C',
    '117',
    'Juan', 
    'Pérez', 
    'Bogotá', 
    'Calle23', 
    '555-1234', 
    1,    
    0,
    1,
    'juan.perez1278@example.com', 
    'xxxx', 
    'ACTIVO',
    'Ventas'
);

DELIMITER //
CREATE PROCEDURE ObtenerPropietarioPorNombre (
    IN p_nombre VARCHAR(255)
)
BEGIN
    SELECT 
		u.tipo_documento,
        u.n_documento,
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
        u.es_propietario,
        u.es_veterinario,
        u.es_administrador,
        u.email,
        u.contraseña,
        u.estado_acceso,
        p.barrio
    FROM 
        propietarios p
    JOIN 
        usuarios u ON p.n_documento = u.n_documento
    WHERE 
        u.nombre LIKE CONCAT('%', p_nombre, '%')
        AND u.estado_acceso ='ACTIVO';  -- Corrected to reference the "usuarios" table
END //
DELIMITER ;
CALL ObtenerPropietarioPorNombre ('Liliana');

DELIMITER //
CREATE PROCEDURE MostrarTodosPropietarios()
BEGIN
    SELECT 
		u.tipo_documento,
        u.n_documento,
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
		u.es_propietario,
        u.es_veterinario,
        u.es_administrador,
        u.email,
        u.contraseña,
        u.estado_acceso,
        p.barrio
    FROM 
        propietarios p
    JOIN 
        usuarios u ON p.n_documento = u.n_documento
	WHERE 
     u.estado_acceso ='ACTIVO';
END //
DELIMITER ;
CALL MostrarTodosPropietarios();

DELIMITER //
CREATE PROCEDURE ObtenerPropietarioPorID (
    IN p_n_documento VARCHAR(40)
)
BEGIN
    SELECT 
		u.tipo_documento,
        u.n_documento,
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
		u.es_propietario,
        u.es_veterinario,
        u.es_administrador,
        u.email,
        u.contraseña,
        u.estado_acceso,
        p.barrio
    FROM 
        propietarios p
    JOIN 
        usuarios u ON p.n_documento = u.n_documento
    WHERE 
        p.n_documento = p_n_documento
        AND u.estado_acceso ='ACTIVO';
END //
DELIMITER ;
CALL ObtenerPropietarioPorID('101');

DELIMITER //
CREATE PROCEDURE ActualizarEstadoUsuario(
    IN p_n_documento VARCHAR(40),
    IN p_nuevo_estado_acceso ENUM('ACTIVO', 'INACTIVO')
)
BEGIN
    UPDATE usuarios
    SET estado_acceso = p_nuevo_estado_acceso
    WHERE n_documento = p_n_documento;

    SELECT n_documento, nombre, apellido, estado_acceso
    FROM usuarios
    WHERE n_documento = p_n_documento;
END//
DELIMITER ;
CALL ActualizarEstadoUsuario('101','INACTIVO');
DELIMITER //
CREATE PROCEDURE ActualizarPropietario(
	IN p_tipo_documento ENUM('C.C','C.E','T.I'),
    IN p_n_documento VARCHAR(40),
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_ciudad VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(100),
    IN p_es_propietario BOOLEAN,
    IN p_es_veterinario BOOLEAN,
    IN p_es_administrador BOOLEAN,
    IN p_email VARCHAR(100),
    IN p_contraseña VARCHAR(255),
    IN p_barrio VARCHAR(100)
)
BEGIN
    DECLARE exit handler for SQLEXCEPTION 
    BEGIN
        ROLLBACK;
    END;
    START TRANSACTION;
    UPDATE usuarios
    SET 
		tipo_documento=p_tipo_documento,
        nombre = p_nombre,
        apellido = p_apellido,
        ciudad = p_ciudad,
        direccion = p_direccion,
        telefono = p_telefono,
        es_propietario = p_es_propietario,
        es_veterinario = p_es_veterinario,
        es_administrador = p_es_administrador,
        email = p_email,
        contraseña = p_contraseña
    WHERE 
        n_documento = p_n_documento;
    UPDATE propietarios
    SET 
        barrio = p_barrio
    WHERE 
        n_documento = p_n_documento;
    COMMIT;
END //

DELIMITER ;

CALL ActualizarPropietario(
	'C.C',
    '104',
    'Juan', 
    'Pérez', 
    'Bogotá', 
    'Calle23', 
    '555-1234', 
    1,    
    0,
    1,
    'juan.perez12@example.com', 
    'xxxx', 
    'BOSA'
);

DELIMITER //
CREATE PROCEDURE EliminarUsuario(
    IN p_n_documento VARCHAR(40)
)
BEGIN
    DECLARE exit handler for SQLEXCEPTION 
    BEGIN
        GET DIAGNOSTICS CONDITION 1 @sqlstate = RETURNED_SQLSTATE, 
            @errno = MYSQL_ERRNO, @text = MESSAGE_TEXT;
        SET @full_error = CONCAT("ERROR ", @errno, " (", @sqlstate, "): ", @text);
        
        ROLLBACK;
        SELECT @full_error AS ErrorMessage;
    END;
    START TRANSACTION;
    
    DELETE FROM citas WHERE n_documento = p_n_documento;
    DELETE FROM citas WHERE codigo_mascota IN (SELECT codigo FROM mascotas WHERE n_documento = p_n_documento);
    DELETE FROM historiales_medicos WHERE codigo_mascota IN (SELECT codigo FROM mascotas WHERE n_documento = p_n_documento);
    DELETE FROM mascotas WHERE n_documento = p_n_documento;
    DELETE FROM propietarios WHERE n_documento = p_n_documento;
    DELETE FROM veterinarios WHERE n_documento = p_n_documento;
    DELETE FROM administradores WHERE n_documento= p_n_documento;
    DELETE FROM usuarios WHERE n_documento= p_n_documento;
    
    COMMIT;
    SELECT 'Propietario y registros relacionados eliminados con éxito.' AS Message;
END //

DELIMITER ;

CALL EliminarUsuario('117');

SELECT * FROM usuarios WHERE n_documento = 106;
SELECT * FROM propietarios WHERE n_documento = 106;