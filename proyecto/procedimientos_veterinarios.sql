use mascotas_db;
DELIMITER //

CREATE PROCEDURE InsertarVeterinario(
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
    IN p_especialidad VARCHAR(100),
    IN p_horario VARCHAR(255)-- Coma añadida antes de este parámetro
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
    INSERT INTO veterinarios (id_usuario, especialidad,horario)
    VALUES (p_id_usuario, p_especialidad,p_horario);
    
    -- Confirmar la transacción si ambas operaciones son exitosas
    COMMIT;
    SET autocommit = 1;
    
END //
DELIMITER ;
CALL InsertarVeterinario(
    1009,
    'Juan', 
    'Pérez', 
    'Bogotá', 
    'Calle23', 
    '555-1234', 
    1,    
    0,
    1,
    'juan.perez127@example.com', 
    'xxxx', 
    'CIRUGIA',
    'Lunes a Viernes 9:00 a 11:00 pm'
);
DELIMITER //

CREATE PROCEDURE ObtenerVeterinarioPorNombre (
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
        v.especialidad,
        v.horario
    FROM 
        veterinarios v
    JOIN 
        usuarios u ON v.id_usuario = u.id_usuario
    WHERE 
        u.nombre LIKE CONCAT('%', p_nombre, '%');    -- Corrected to reference the "usuarios" table
END //

DELIMITER ;

CALL ObtenerVeterinarioPorNombre ('juan');

DELIMITER //

CREATE PROCEDURE MostrarTodosVeterinarios()
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
        v.especialidad,
        v.horario
    FROM 
      veterinarios v
    JOIN 
        usuarios u ON v.id_usuario = u.id_usuario;
END //

DELIMITER ;
CALL MostrarTodosVeterinarios();

DELIMITER //

CREATE PROCEDURE ObtenerVeterinarioPorID (
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
		v.especialidad,
        v.horario
    FROM 
        veterinarios v
    JOIN 
        usuarios u ON v.id_usuario = u.id_usuario
    WHERE 
        v.id_usuario = p_id_usuario;
END //

DELIMITER ;

CALL ObtenerVeterinarioPorID(105);

DELIMITER //

CREATE PROCEDURE ActualizarVeterinario(
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
	IN p_especialidad VARCHAR(100),
    IN p_horario VARCHAR(255)
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
    UPDATE veterinarios
    SET 
        especialidad = p_especialidad,
        horario = p_horario
    WHERE 
        id_usuario = p_id_usuario;

    -- Commit the transaction if both updates are successful
    COMMIT;
END //

DELIMITER ;

CALL ActualizarVeterinario(
    105, 'Juana', 'Perez', 'Barcelona', 'Calle Falsa 123', '1234567890', 
    TRUE, TRUE, FALSE, 'juana.perez@example.com', 'contraseña123', 
    'Cirugía', 'Lunes a Viernes, 9:00-17:00'
);

DELIMITER //

CREATE PROCEDURE EliminarVeterinario(
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

CALL EliminarVeterinario(105);