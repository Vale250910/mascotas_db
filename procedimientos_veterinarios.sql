USE mascotas_db;
DELIMITER //
CREATE PROCEDURE InsertarVeterinario(
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
    IN p_especialidad VARCHAR(100),
    IN p_horario VARCHAR(255)
)
BEGIN
    DECLARE exit handler for SQLEXCEPTION
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
    IF NOT EXISTS (SELECT 1 FROM veterinarios WHERE n_documento = p_n_documento) THEN
        INSERT INTO veterinarios (n_documento, especialidad, horario)
        VALUES (p_n_documento, p_especialidad, p_horario);
        IF ROW_COUNT() = 0 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Error: No se pudo insertar en la tabla veterinarios';
        END IF;
        SELECT 'Veterinario insertado exitosamente' AS Mensaje;
    ELSE
        SELECT 'Veterinario ya existe en la tabla veterinarios' AS Mensaje;
    END IF;
    
    COMMIT;
END //

CREATE PROCEDURE ObtenerVeterinarioPorNombre(
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
        v.especialidad,
        v.horario
    FROM 
        veterinarios v
    JOIN 
        usuarios u ON v.n_documento = u.n_documento
    WHERE 
        u.nombre LIKE CONCAT('%', p_nombre, '%')
        AND u.estado_acceso = 'ACTIVO'; 
END //

CREATE PROCEDURE MostrarTodosVeterinarios()
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
        v.especialidad,
        v.horario
    FROM 
        veterinarios v
    JOIN 
        usuarios u ON v.n_documento = u.n_documento
    WHERE
        u.estado_acceso = 'ACTIVO'; 
END //

CREATE PROCEDURE ObtenerVeterinarioPorID(
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
        v.especialidad,
        v.horario
    FROM 
        veterinarios v
    JOIN 
        usuarios u ON v.n_documento = u.n_documento
    WHERE 
        v.n_documento = p_n_documento
        AND u.estado_acceso = 'ACTIVO';
END //

CREATE PROCEDURE ActualizarVeterinario(
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
    IN p_especialidad VARCHAR(100),
    IN p_horario VARCHAR(255)
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

    UPDATE veterinarios
    SET 
        especialidad = p_especialidad,
        horario = p_horario
    WHERE 
        n_documento = p_n_documento;
    COMMIT;
END //
DELIMITER ;
CALL InsertarVeterinario(
    'C.C',
    '118',
    'Ana', 
    'Gómez', 
    'Medellín', 
    'Calle 45', 
    '555-6789', 
    0,    
    1,
    0,
    'ana.gomez@example.com', 
    'xxxx', 
    'ACTIVO',
    'Especialista en cirugía',
    'Lunes a Viernes, 10:00-16:00'
);

CALL ObtenerVeterinarioPorNombre('Ana');
CALL MostrarTodosVeterinarios();
CALL ObtenerVeterinarioPorID('118');
CALL ActualizarVeterinario(
    'C.C',
    '118', 
    'Ana', 
    'Gómez', 
    'Medellín', 
    'Calle 45', 
    '555-6789', 
    0, 
    1, 
    0, 
    'ana.gomez@example.com', 
    'contraseña123', 
    'Especialista en cirugía', 
    'Lunes a Viernes, 10:00-16:00'
);
