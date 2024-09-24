DELIMITER //
CREATE PROCEDURE InsertarAdministrador(
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
    IN p_estado_acceso ENUM('ACTIVO', 'INACTIVO'),
    IN p_cargo VARCHAR(100),
    IN p_fecha_ingreso DATE
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
    'Ventas',
    '2024-02-25'
);
DELIMITER //
CREATE PROCEDURE ObtenerAdministradorPorNombre(
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
        a.cargo,
        a.fecha_ingreso
    FROM 
        administradores a
    JOIN 
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
        a.cargo,
        a.fecha_ingreso
    FROM 
        administradores a
    JOIN 
        usuarios u ON a.n_documento = u.n_documento
    WHERE
        u.estado_acceso = 'ACTIVO';
END //
DELIMITER ;
CALL MostrarTodosAdministradores();

DELIMITER //
CREATE PROCEDURE ObtenerAdministradorPorID(
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
        a.cargo,
        a.fecha_ingreso
    FROM 
        administradores a
    JOIN 
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
    IN p_cargo VARCHAR(100),
    IN p_fecha_ingreso DATE
)
BEGIN
    DECLARE exit handler for SQLEXCEPTION 
    BEGIN
        ROLLBACK;
    END;
    START TRANSACTION;
    UPDATE usuarios
    SET 
        tipo_documento = p_tipo_documento,
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
    UPDATE administradores
    SET 
        cargo = p_cargo,
        fecha_ingreso = p_fecha_ingreso
    WHERE 
        n_documento = p_n_documento;
    COMMIT;
END //
DELIMITER ;
CALL ActualizarAdministrador(
    'C.C','110', 'Juana', 'Perez', 'Barcelona', 'Calle Falsa 123', '1234567890', 
    1, 1, 1, 'juana.perez@example.com', 'contraseña123', 
    'Administrador General', '2021-02-28'
);
