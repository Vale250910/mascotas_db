use mascotas_db;
DELIMITER //
<<<<<<< HEAD
CREATE PROCEDURE CrearMascota(
	IN p_codigo VARCHAR(40),
    IN p_nombre VARCHAR(255),
    IN p_especie VARCHAR(255),
    IN p_raza VARCHAR(255),
    IN p_edad DECIMAL (10,2) ,
    IN p_peso DECIMAL (10,2),
    IN p_n_documento VARCHAR(40),
    IN p_estado_acceso ENUM('ACTIVO', 'INACTIVO')
)
BEGIN
    INSERT INTO mascotas (codigo,nombre, especie, raza, edad, peso,n_documento,estado_acceso)
    VALUES (p_codigo,p_nombre, p_especie, p_raza, p_edad, p_peso, p_n_documento,p_estado_acceso);
END //
DELIMITER ;
CALL CrearMascota(
    'M001',
    'Rex',
    'Perro',
    'Labrador',
    5.5,
    30.0,
    '110', -- ID del usuario
    'ACTIVO'
);

DELIMITER //
CREATE PROCEDURE MostrarTodasLasMascotas(
)
BEGIN
    SELECT *FROM mascotas
    WHERE estado_acceso='ACTIVO';
END //
DELIMITER ;
call MostrarTodasLasMascotas();

DELIMITER //
CREATE PROCEDURE BuscarMascotaCodigo(
    IN p_codigo VARCHAR(40)
)
BEGIN
    SELECT *FROM mascotas WHERE codigo = p_codigo
    AND estado_acceso= 'ACTIVO';
END //
DELIMITER ;
call BuscarMascotaCodigo('1');

DELIMITER //
CREATE PROCEDURE BuscarMascotaNombre(
    IN p_nombre VARCHAR(255)
)
BEGIN
    SELECT *FROM mascotas WHERE nombre LIKE CONCAT('%', p_nombre, '%')
    AND estado_acceso='ACTIVO';
END //
DELIMITER ;
call BuscarMascotaNombre('MELSA');

DELIMITER //
CREATE PROCEDURE ActualizarEstadoMascotas(
    IN p_codigo VARCHAR(40),
    IN p_nuevo_estado_acceso ENUM('ACTIVO', 'INACTIVO')
)
BEGIN
    UPDATE mascotas
    SET estado_acceso = p_nuevo_estado_acceso
    WHERE codigo = p_codigo;

    SELECT codigo,nombre,estado_acceso
    FROM mascotas
    WHERE codigo = p_codigo;
END//
DELIMITER ;
CALL ActualizarEstadoMascotas('1','INACTIVO');

DELIMITER //
CREATE PROCEDURE ActualizarMascota(
    IN p_codigo VARCHAR(40),
=======

CREATE PROCEDURE CrearMascota(
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    IN p_nombre VARCHAR(255),
    IN p_especie VARCHAR(255),
    IN p_raza VARCHAR(255),
    IN p_edad DECIMAL,
    IN p_peso DECIMAL,
<<<<<<< HEAD
    IN p_n_documento VARCHAR(40)
=======
    IN p_usuario INT
)
BEGIN
    INSERT INTO mascotas (nombre, especie, raza, edad, peso,id_usuario)
    VALUES (p_nombre, p_especie, p_raza, p_edad, p_peso, p_usuario);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE MostrarTodasLasMascotas(
)
BEGIN
    SELECT *FROM mascotas;
END //
DELIMITER ;
call MostrarTodasLasMascotas();

DELIMITER //

CREATE PROCEDURE BuscarMascotaCodigo(
    IN p_codigo INT
)
BEGIN
    SELECT *FROM mascotas WHERE codigo = p_codigo;
END //

DELIMITER ;

call BuscarMascotaCodigo(1);

DELIMITER //

CREATE PROCEDURE BuscarMascotaNombre(
    IN p_nombre VARCHAR(255)
)
BEGIN
    SELECT *FROM mascotas WHERE nombre LIKE CONCAT('%', p_nombre, '%');
END //

DELIMITER ;

call BuscarMascotaNombre('MELSA');

DELIMITER //

CREATE PROCEDURE ActualizarMascota(
    IN p_codigo INT,
    IN p_nombre VARCHAR(255),
    IN p_especie VARCHAR(255),
    IN p_raza VARCHAR(255),
    IN p_edad FLOAT,
    IN p_peso FLOAT,
    IN p_id_usuario INT
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
)
BEGIN
    UPDATE mascotas
    SET 
		nombre = p_nombre,
        especie = p_especie,
        raza = p_raza,
        edad = p_edad,
        peso = p_peso,
<<<<<<< HEAD
        n_documento = p_n_documento
    WHERE codigo = p_codigo;
END //
DELIMITER ;
call ActualizarMascota('1','MELSA','GATA','PERZA',5.00,12.00,'101');

DELIMITER //
CREATE PROCEDURE EliminarMascota(
    IN p_codigo VARCHAR(40)
=======
        id_usuario = p_id_usuario
    WHERE codigo = p_codigo;
END //

DELIMITER ;

call ActualizarMascota(1,'MELSA','GATA','PERZA',5.00,12.00,101);

DELIMITER //

CREATE PROCEDURE EliminarMascota(
    IN p_codigo INT
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
)
BEGIN
    DELETE FROM mascotas WHERE codigo = p_codigo;
END //
<<<<<<< HEAD
DELIMITER ;
call EliminarMascota('M001');
=======

DELIMITER ;

call EliminarMascota(6);
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
