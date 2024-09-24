DELIMITER //
<<<<<<< HEAD
CREATE PROCEDURE InsertarAdministrador(
    IN p_tipo_documento ENUM('C.C','C.E','T.I'),
    IN p_n_documento VARCHAR(40),
=======

CREATE PROCEDURE InsertarAdministrador(
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
    IN p_estado_acceso ENUM('ACTIVO', 'INACTIVO'),
=======
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    IN p_cargo VARCHAR(100),
    IN p_fecha_ingreso DATE
)
BEGIN
<<<<<<< HEAD
    DECLARE exit handler for sqlexception
    BEGIN
        ROLLBACK;
        SELECT 'Error: La transacción ha sido revertida' AS Mensaje;
    END;
    START TRANSACTION;
    IF EXISTS (SELECT 1 FROM usuarios WHERE n_documento = p_n_documento) THEN
        SELECT 'Usuario ya existe en la tabla usuarios' AS Mensaje;
    ELSE
        INSERT INTO usuarios (tipo_documento, n_documento, nombre, apellido, ciudad, direccion, telefono, es_propietario, es_veterinario, es_administrador, email, contraseña, estado_acceso)
        VALUES (p_tipo_documento, p_n_documento, p_nombre, p_apellido, p_ciudad, p_direccion, p_telefono, p_es_propietario, p_es_veterinario, p_es_administrador, p_email, p_contraseña, p_estado_acceso);
        IF ROW_COUNT() = 0 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Error: No se pudo insertar en la tabla usuarios';
        END IF;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM administradores WHERE n_documento = p_n_documento) THEN
        INSERT INTO administradores (n_documento, cargo, fecha_ingreso)
        VALUES (p_n_documento, p_cargo, p_fecha_ingreso);
        IF ROW_COUNT() = 0 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Error: No se pudo insertar en la tabla administradores';
        END IF;
        SELECT 'Administrador insertado exitosamente' AS Mensaje;
    ELSE
        SELECT 'Administrador ya existe en la tabla administradores' AS Mensaje;
    END IF;
    COMMIT;
END //
DELIMITER ;
CALL InsertarAdministrador(
	'C.C',
    '117',
=======
    -- Verificar si el usuario ya existe
    IF EXISTS (SELECT 1 FROM usuarios WHERE id_usuario = p_id_usuario) THEN
        SELECT 'Usuario ya existe en la tabla usuarios';
    ELSE
        INSERT INTO usuarios (id_usuario, nombre, apellido, ciudad, direccion, telefono, es_propietario, es_veterinario, es_administrador, email, contraseña)
        VALUES (p_id_usuario, p_nombre, p_apellido, p_ciudad, p_direccion, p_telefono, p_es_propietario, p_es_veterinario, p_es_administrador, p_email, p_contraseña);
    END IF;

    -- Intentar insertar en la tabla administradores
    IF NOT EXISTS (SELECT 1 FROM administradores WHERE id_usuario = p_id_usuario) THEN
        INSERT INTO administradores (id_usuario, cargo, fecha_ingreso)
        VALUES (p_id_usuario, p_cargo, p_fecha_ingreso);
        SELECT 'Administrador insertado';
    ELSE
        SELECT 'Administrador ya existe en la tabla administradores';
    END IF;
END//

DELIMITER ;


CALL InsertarAdministrador(
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
    'Ventas',
    '2024-02-25'
);
DELIMITER //
<<<<<<< HEAD
CREATE PROCEDURE ObtenerAdministradorPorNombre(
=======

CREATE PROCEDURE ObtenerAdministradorPorNombre (
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
        u.contraseña,
        u.estado_acceso,
=======
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        a.cargo,
        a.fecha_ingreso
    FROM 
        administradores a
    JOIN 
<<<<<<< HEAD
        usuarios u ON a.n_documento = u.n_documento
    WHERE 
        u.nombre LIKE CONCAT('%', p_nombre, '%')
        AND u.estado_acceso = 'ACTIVO';
END //
DELIMITER ;
CALL ObtenerAdministradorPorNombre ('JUAN');

DELIMITER //
CREATE PROCEDURE MostrarTodosAdministradores()
BEGIN
    SELECT 
        u.tipo_documento,
        u.n_documento,
=======
        usuarios u ON a.id_usuario = u.id_usuario
    WHERE 
        u.nombre LIKE CONCAT('%', p_nombre, '%');  -- Asegúrate de que esta es la condición que deseas
END //
DELIMITER ;


CALL ObtenerAdministradorPorNombre ('JUAN');

DELIMITER //

CREATE PROCEDURE MostrarTodosAdministradores()
BEGIN
    SELECT 
        u.id_usuario,
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
<<<<<<< HEAD
        u.es_propietario,
        u.es_veterinario,
        u.es_administrador,
        u.email,
        u.contraseña,
        u.estado_acceso,
        a.cargo,
        a.fecha_ingreso
    FROM 
        administradores a
    JOIN 
        usuarios u ON a.n_documento = u.n_documento
    WHERE
        u.estado_acceso = 'ACTIVO';
END //
=======
		u.es_propietario,
        u.es_veterinario,
        u.es_administrador,
        u.email,
        a.cargo,
        a.fecha_ingreso
    FROM 
      administradores a
    JOIN 
        usuarios u ON a.id_usuario = u.id_usuario;
END //

>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
DELIMITER ;
CALL MostrarTodosAdministradores();

DELIMITER //
<<<<<<< HEAD
CREATE PROCEDURE ObtenerAdministradorPorID(
    IN p_n_documento VARCHAR(40)
)
BEGIN
    SELECT 
        u.tipo_documento,
        u.n_documento,
=======

CREATE PROCEDURE ObtenerAdministradorPorID (
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
<<<<<<< HEAD
        u.es_propietario,
        u.es_veterinario,
        u.es_administrador,
        u.email,
        u.contraseña,
        u.estado_acceso,
        a.cargo,
=======
		u.es_propietario,
        u.es_veterinario,
        u.es_administrador,
        u.email,
		a.cargo,
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        a.fecha_ingreso
    FROM 
        administradores a
    JOIN 
<<<<<<< HEAD
        usuarios u ON a.n_documento = u.n_documento
    WHERE 
        a.n_documento = p_n_documento
        AND u.estado_acceso = 'ACTIVO';
END //
DELIMITER ;
CALL ObtenerAdministradorPorID('103');

DELIMITER //
CREATE PROCEDURE ActualizarAdministrador(
    IN p_tipo_documento ENUM('C.C','C.E','T.I'),
    IN p_n_documento VARCHAR(40),
=======
        usuarios u ON a.id_usuario = u.id_usuario
    WHERE 
        a.id_usuario = p_id_usuario;
END //

DELIMITER ;

CALL ObtenerAdministradorPorID(103);

DELIMITER //

CREATE PROCEDURE ActualizarAdministrador(
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
<<<<<<< HEAD
    IN p_cargo VARCHAR(100),
=======
	IN p_cargo VARCHAR(100),
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    IN p_fecha_ingreso DATE
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
        tipo_documento = p_tipo_documento,
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
    UPDATE administradores
    SET 
        cargo = p_cargo,
        fecha_ingreso = p_fecha_ingreso
    WHERE 
<<<<<<< HEAD
        n_documento = p_n_documento;
    COMMIT;
END //
DELIMITER ;
CALL ActualizarAdministrador(
    'C.C','110', 'Juana', 'Perez', 'Barcelona', 'Calle Falsa 123', '1234567890', 
    1, 1, 1, 'juana.perez@example.com', 'contraseña123', 
    'Administrador General', '2021-02-28'
);
=======
        id_usuario = p_id_usuario;

    -- Commit the transaction if both updates are successful
    COMMIT;
END //

DELIMITER ;

CALL ActualizarAdministrador(
    110, 'Juana', 'Perez', 'Barcelona', 'Calle Falsa 123', '1234567890', 
    TRUE, TRUE, TRUE, 'juana.perez@example.com', 'contraseña123', 
    'Administrador General', '2021-02-28'
);

DELIMITER //

CREATE PROCEDURE EliminarAdministrador(
    IN p_id_usuario INT
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

    SELECT 'Propietario y registros relacionados eliminados con éxito.' AS Message;
END //

DELIMITER ;

CALL EliminarAdministrador(10023);
SELECT * FROM usuarios WHERE id_usuario = 106;
SELECT * FROM propietarios WHERE id_usuario = 106;
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
