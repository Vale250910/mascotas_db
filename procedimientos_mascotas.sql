use mascotas_db;
DELIMITER //
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
    IN p_nombre VARCHAR(255),
    IN p_especie VARCHAR(255),
    IN p_raza VARCHAR(255),
    IN p_edad DECIMAL,
    IN p_peso DECIMAL,
    IN p_n_documento VARCHAR(40)
)
BEGIN
    UPDATE mascotas
    SET 
		nombre = p_nombre,
        especie = p_especie,
        raza = p_raza,
        edad = p_edad,
        peso = p_peso,
        n_documento = p_n_documento
    WHERE codigo = p_codigo;
END //
DELIMITER ;
call ActualizarMascota('1','MELSA','GATA','PERZA',5.00,12.00,'101');

DELIMITER //
CREATE PROCEDURE EliminarMascota(
    IN p_codigo VARCHAR(40)
)
BEGIN
    DELETE FROM mascotas WHERE codigo = p_codigo;
END //
DELIMITER ;
call EliminarMascota('M001');
