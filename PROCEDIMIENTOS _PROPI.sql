use mascotas_db;
DELIMITER //
<<<<<<< HEAD
CREATE PROCEDURE InsertarPropietario(
	IN p_tipo_documento ENUM('C.C','C.E','T.I'),
    IN p_n_documento VARCHAR(40),
=======

CREATE PROCEDURE InsertarPropietario(
    IN p_id_usuario INT,
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
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
=======
    IN estado_acceso enum ('ACTIVO','INACTIVO'),
    IN p_barrio VARCHAR(100)
)
BEGIN
    -- Verificar si el usuario ya existe
    IF EXISTS (SELECT 1 FROM usuarios WHERE id_usuario = p_id_usuario) THEN
        SELECT 'Usuario ya existe en la tabla usuarios';
    ELSE
        INSERT INTO usuarios (id_usuario, nombre, apellido, ciudad, direccion, telefono, es_propietario, es_veterinario, es_administrador, email, contraseña,estado_acceso)
        VALUES (p_id_usuario, p_nombre, p_apellido, p_ciudad, p_direccion, p_telefono, p_es_propietario, p_es_veterinario, p_es_administrador, p_email, p_contraseña,estado_acceso);
    END IF;

    -- Intentar insertar en la tabla administradores
    IF NOT EXISTS (SELECT 1 FROM propietarios WHERE id_usuario = p_id_usuario) THEN
        INSERT INTO propietarios (id_usuario, barrio)
        VALUES (p_id_usuario, p_barrio);
        SELECT 'Propietario insertado';
    ELSE
        SELECT 'Propietario ya existe en la tabla propietarios';
    END IF;
END//

DELIMITER ;

CALL InsertarPropietario(
    117,
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
    'ACTIVO',
=======
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    'Ventas'
);

DELIMITER //
<<<<<<< HEAD
=======

>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
CREATE PROCEDURE ObtenerPropietarioPorNombre (
    IN p_nombre VARCHAR(255)
)
BEGIN
    SELECT 
<<<<<<< HEAD
		u.tipo_documento,
        u.n_documento,
=======
        u.id_usuario,
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
        u.estado_acceso,
=======
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        p.barrio
    FROM 
        propietarios p
    JOIN 
<<<<<<< HEAD
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
=======
        usuarios u ON p.id_usuario = u.id_usuario
    WHERE 
        u.nombre LIKE CONCAT('%', p_nombre, '%');  -- Corrected to reference the "usuarios" table
END //

DELIMITER ;

CALL ObtenerPropietarioPorNombre ('Liliana');

DELIMITER //

CREATE PROCEDURE MostrarTodosPropietarios()
BEGIN
    SELECT 
        u.id_usuario,
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
        u.estado_acceso,
=======
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        p.barrio
    FROM 
        propietarios p
    JOIN 
<<<<<<< HEAD
        usuarios u ON p.n_documento = u.n_documento
	WHERE 
     u.estado_acceso ='ACTIVO';
END //
=======
        usuarios u ON p.id_usuario = u.id_usuario;
END //

>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
DELIMITER ;
CALL MostrarTodosPropietarios();

DELIMITER //
<<<<<<< HEAD
CREATE PROCEDURE ObtenerPropietarioPorID (
    IN p_n_documento VARCHAR(40)
)
BEGIN
    SELECT 
		u.tipo_documento,
        u.n_documento,
=======

CREATE PROCEDURE ObtenerPropietarioPorID (
    IN p_id_usuario INT
)
BEGIN
    SELECT 
        u.id_usuario,
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
        u.estado_acceso,
=======
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        p.barrio
    FROM 
        propietarios p
    JOIN 
<<<<<<< HEAD
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
=======
        usuarios u ON p.id_usuario = u.id_usuario
    WHERE 
        p.id_usuario = p_id_usuario;
END //

DELIMITER ;

CALL ObtenerPropietarioPorID(101);

DELIMITER //

CREATE PROCEDURE ActualizarPropietario(
    IN p_id_usuario INT,
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
        ROLLBACK;
    END;
    START TRANSACTION;
    UPDATE usuarios
    SET 
		tipo_documento=p_tipo_documento,
=======
        -- Rollback if there is any error
        ROLLBACK;
    END;

    -- Start the transaction
    START TRANSACTION;

    -- Update the 'usuarios' table
    UPDATE usuarios
    SET 
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
        n_documento = p_n_documento;
=======
        id_usuario = p_id_usuario;

    -- Update the 'propietarios' table
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    UPDATE propietarios
    SET 
        barrio = p_barrio
    WHERE 
<<<<<<< HEAD
        n_documento = p_n_documento;
=======
        id_usuario = p_id_usuario;

    -- Commit the transaction if both updates are successful
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    COMMIT;
END //

DELIMITER ;

CALL ActualizarPropietario(
<<<<<<< HEAD
	'C.C',
    '104',
=======
    104,
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
CREATE PROCEDURE EliminarUsuario(
    IN p_n_documento VARCHAR(40)
=======

CREATE PROCEDURE EliminarPropietario(
    IN p_id_usuario INT
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
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
=======

    START TRANSACTION;

    -- Delete from citas related to this user as a veterinario
    DELETE FROM citas WHERE id_veterinario = p_id_usuario;

    -- Delete from citas related to mascotas owned by this user
    DELETE FROM citas WHERE codigo_mascota IN (SELECT codigo FROM mascotas WHERE id_usuario = p_id_usuario);

    -- Delete from historial_medico related to mascotas owned by this user
    DELETE FROM historiales_medicos WHERE codigo_mascota IN (SELECT codigo FROM mascotas WHERE id_usuario = p_id_usuario);

    -- Delete from mascotas
    DELETE FROM mascotas WHERE id_usuario = p_id_usuario;

    -- Delete from propietarios
    DELETE FROM propietarios WHERE id_usuario = p_id_usuario;

    -- Delete from veterinarios
    DELETE FROM veterinarios WHERE id_usuario = p_id_usuario;

    -- Delete from administradores
    DELETE FROM administradores WHERE id_usuario = p_id_usuario;

    -- Finally, delete from usuarios
    DELETE FROM usuarios WHERE id_usuario = p_id_usuario;

    COMMIT;

>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    SELECT 'Propietario y registros relacionados eliminados con éxito.' AS Message;
END //

DELIMITER ;

<<<<<<< HEAD
CALL EliminarUsuario('117');

SELECT * FROM usuarios WHERE n_documento = 106;
SELECT * FROM propietarios WHERE n_documento = 106;
=======
CALL EliminarPropietario(106);

SELECT * FROM usuarios WHERE id_usuario = 106;
SELECT * FROM propietarios WHERE id_usuario = 106;
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
