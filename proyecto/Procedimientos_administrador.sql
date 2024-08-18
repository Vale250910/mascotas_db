use mascotas_db;
DELIMITER //

CREATE PROCEDURE InsertarAdministrador(
    IN p_id_usuario INT,
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_ciudad VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(100),
    IN p_es_propietario BOOLEAN,
    IN p_es_veterinario BOOLEAN,
    IN p_es_administrador BOOLEAN,
    IN p_email VARCHAR(100),
    IN p_contraseña VARBINARY(255),
    IN p_cargo VARCHAR(100),
    IN p_fecha_ingreso DATE-- Coma añadida antes de este parámetro
)
BEGIN
DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		-- Deshacer los cambios en la BD si algo falla
		ROLLBACK;
        RESIGNAL;
	END;
    
    SET autocommit = 0;
    -- Arrancar la transacción:
    START TRANSACTION;
    -- Insertar en la tabla 'usuarios'
    INSERT INTO usuarios (id_usuario, nombre, apellido, ciudad, direccion, telefono, es_propietario, es_veterinario, es_administrador, email, contraseña)
    VALUES (p_id_usuario, p_nombre, p_apellido, p_ciudad, p_direccion, p_telefono, p_es_propietario, p_es_veterinario, p_es_administrador, p_email,p_contraseña);
    
    -- Insertar en la tabla 'propietarios'
    INSERT INTO administradores (id_usuario, cargo,fecha_ingreso)
    VALUES (p_id_usuario,p_cargo,p_fecha_ingreso);
    
    -- Confirmar la transacción si ambas operaciones son exitosas
    COMMIT;
    SET autocommit = 1;
    
END //
DELIMITER ;
CALL InsertarAdministrador(
    1100,
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
    'Ventas',
    '2024-02-25'
);
DELIMITER //

CREATE PROCEDURE ObtenerAdministradorPorNombre (
    IN p_nombre VARCHAR(255)
)
BEGIN
    SELECT 
        u.id_usuario,
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
        a.cargo,
        a.fecha_ingreso
    FROM 
        administradores a
    JOIN 
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
        a.cargo,
        a.fecha_ingreso
    FROM 
      administradores a
    JOIN 
        usuarios u ON a.id_usuario = u.id_usuario;
END //

DELIMITER ;
CALL MostrarTodosAdministradores();

DELIMITER //

CREATE PROCEDURE ObtenerAdministradorPorID (
    IN p_id_usuario INT
)
BEGIN
    SELECT 
        u.id_usuario,
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
		a.cargo,
        a.fecha_ingreso
    FROM 
        administradores a
    JOIN 
        usuarios u ON a.id_usuario = u.id_usuario
    WHERE 
        a.id_usuario = p_id_usuario;
END //

DELIMITER ;

CALL ObtenerAdministradorPorID(103);

DELIMITER //

CREATE PROCEDURE ActualizarAdministrador(
    IN p_id_usuario INT,
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
        -- Rollback if there is any error
        ROLLBACK;
    END;

    -- Start the transaction
    START TRANSACTION;

    -- Update the 'usuarios' table
    UPDATE usuarios
    SET 
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
        id_usuario = p_id_usuario;

    -- Update the 'propietarios' table
    UPDATE administradores
    SET 
        cargo = p_cargo,
        fecha_ingreso = p_fecha_ingreso
    WHERE 
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
        -- Rollback if there is any error
        ROLLBACK;
    END;

    -- Start the transaction
    START TRANSACTION;

    -- Delete from related tables first
    DELETE FROM propietarios WHERE id_usuario = p_id_usuario;
    DELETE FROM veterinarios WHERE id_usuario = p_id_usuario;
    DELETE FROM administradores WHERE id_usuario = p_id_usuario;
    
    -- Delete from 'usuarios' table
    DELETE FROM usuarios WHERE id_usuario = p_id_usuario;

    -- Commit the transaction if all deletions are successful
    COMMIT;
END //

DELIMITER ;

CALL EliminarAdministrador(104);