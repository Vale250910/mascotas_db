use mascotas_db;
DELIMITER //

CREATE PROCEDURE CrearMascota(
    IN p_nombre VARCHAR(255),
    IN p_especie VARCHAR(255),
    IN p_raza VARCHAR(255),
    IN p_edad DECIMAL,
    IN p_peso DECIMAL,
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
)
BEGIN
    UPDATE mascotas
    SET 
		nombre = p_nombre,
        especie = p_especie,
        raza = p_raza,
        edad = p_edad,
        peso = p_peso,
        id_usuario = p_id_usuario
    WHERE codigo = p_codigo;
END //

DELIMITER ;

call ActualizarMascota(1,'MELSA','GATA','PERZA',5.00,12.00,101);

DELIMITER //

CREATE PROCEDURE EliminarMascota(
    IN p_codigo INT
)
BEGIN
    DELETE FROM mascotas WHERE codigo = p_codigo;
END //

DELIMITER ;

call EliminarMascota(6);
