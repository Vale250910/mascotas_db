CREATE DATABASE IF NOT EXISTS mascotas_db;
USE mascotas_db;

CREATE TABLE usuarios (
id_usuario INT PRIMARY KEY NOT NULL,
nombre VARCHAR(50) NOT NULL,
apellido VARCHAR(30) NOT NULL,
ciudad VARCHAR(50) NOT NULL,
direccion VARCHAR(100) NOT NULL,
telefono VARCHAR(20) NOT NULL,
es_propietario BOOLEAN DEFAULT FALSE,
es_veterinario BOOLEAN DEFAULT FALSE,
es_administrador BOOLEAN DEFAULT FALSE,
email VARCHAR(100) NOT NULL,
contraseña VARCHAR(255) NOT NULL
);

CREATE TABLE administradores (
id_usuario INT PRIMARY KEY NOT NULL,
cargo VARCHAR(100) NOT NULL,
fecha_ingreso DATE NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE propietarios (
id_usuario INT PRIMARY KEY NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE veterinarios (
id_usuario INT PRIMARY KEY NOT NULL,
especialidad VARCHAR(100)NOT NULL,
horario VARCHAR(255)NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE mascotas (
codigo INT PRIMARY KEY NOT NULL,
nombre VARCHAR (100) NOT NULL,
especie VARCHAR (100) NOT NULL,
raza VARCHAR (100) NOT NULL,
edad DECIMAL (10,2) NOT NULL,
peso DECIMAL (10,2) NOT NULL,
id_usuario int,
FOREIGN KEY (id_usuario) references propietarios(id_usuario)ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE historial_medico(
id INT PRIMARY KEY NOT NULL,
fecha DATE,
descripcion VARCHAR(100)NOT NULL,
tratamiento VARCHAR(100)NOT NULL,
codigo_mascota INT NOT NULL,
FOREIGN KEY (codigo_mascota) REFERENCES mascotas(codigo)
);

INSERT INTO usuarios (id_usuario, nombre, apellido, ciudad, direccion, telefono, es_propietario, es_veterinario, es_administrador, email, contraseña) VALUES
(101, 'ALBERTO', 'DI CAPRIO', 'PALMIRA', 'CALLE 45', '31295858', 1, 0, 0, 'alberto@gmail.com', '4321'),
(102, 'JAQUELINE', 'ACOSTA', 'FACATATIVA', 'CALLE 51', '313409449', 0, 0, 0, 'jaqueline@gmail.com', '987'),
(103, 'MARIANA', 'URQUIJO', 'SOACHA', 'CALLE 84', '31404534', 0, 0, 0, 'mariana@gmail.com', '98712'),
(104, 'RICARDO JORGE', 'ESPITIA', 'COTA', 'CALLE 31', '31343333', 1, 0, 0, 'jorge@gmail.com', '12345678'),
(105, 'PEPE', 'CORTISONIA', 'SIBATE', 'CALLE 88', '3114393', 0, 0, 0, 'pepe@gmail.com', '4321'),
(106, 'LILIANA', 'MANRIQUE', 'SOACHA', 'CALLE 99 14-44', '3103559658', 1, 0, 0, 'liliana@gmail.com', '54321'),
(107, 'HAROLD', 'LOZANO', 'SIBATE', 'CALLE 12-3', '313598', 0, 0, 0, 'harold@gmail.com', '54321'),
(108, 'FRANCISCO', 'PARRA', 'MOSQUERA', 'CALLE 13 12-44', '311857372', 0, 0, 0, 'francisco@gmail.com', '123'),
(109, 'SOFIA', 'MENDIETE', 'BOGOTA', 'CALLE 80 4-8', '312987', 1, 0, 0, 'sofia@gmail.com', '123'),
(110, 'MARIO', 'CHIPOLLINI', 'NAPOLES - ITALIA', 'CALLE 12 13-43', '311857372', 1, 0, 0, 'mario@gmail.com', '123');

INSERT INTO propietarios (id_usuario) VALUES
(101),
(104),
(106),
(109),
(110);
SELECT * FROM propietarios;

INSERT INTO mascotas (codigo, nombre, especie, raza, edad, peso, id_usuario) VALUES
(1001, 'MELSO', 'PERRO', 'BULL DOG', 5.00, 12.00, 101),
(1002, 'PULGAS', 'PERRO', 'FRENCH PULGA', 4.00, 3.00, 101),
(1003, 'PELROJO', 'GATO', 'CRILLO COLOMBIANO', 2.00, 2.00, 106);
SELECT * FROM mascotas;

INSERT INTO administradores (id_usuario, cargo, fecha_ingreso) VALUES
(102, 'Administrador General', '2023-01-15'),
(103, 'Administrador de Recursos Humanos', '2023-02-20'),
(104, 'Administrador de TI', '2023-03-05'),
(108, 'Administrador Financiero', '2023-04-10'),
(110, 'Administrador de Operaciones', '2023-05-25');
SELECT * FROM administradores;

INSERT INTO veterinarios (id_usuario, especialidad, horario) VALUES
(105, 'Cirugía', 'Lunes a Viernes, 8:00 - 17:00'),
(106, 'Dermatología', 'Martes a Sábado, 9:00 - 18:00'),
(107, 'Oftalmología', 'Lunes a Viernes, 8:00 - 17:00'),
(108, 'Cardiología', 'Miércoles a Domingo, 10:00 - 19:00'),
(109, 'Neurología', 'Jueves a Lunes, 9:00 - 18:00');

SELECT * FROM veterinarios;

CREATE TABLE producto(
    codigo INT UNSIGNED NOT NULL PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT(100),
    precio DECIMAL(10,2), -- Especificar precisión y escala
    stock INT UNSIGNED NOT NULL
);
SELECT 
    u.id_usuario, u.nombre AS nombre_usuario, u.apellido, u.ciudad, u.direccion, u.telefono, u.email,
    p.id_usuario AS id_propietario,
    m.codigo AS codigo_mascota, m.nombre AS nombre_mascota, m.especie, m.raza, m.edad, m.peso
FROM 
    usuarios u
INNER JOIN 
    propietarios p ON u.id_usuario = p.id_usuario
INNER JOIN 
    mascotas m ON p.id_usuario = m.id_usuario;
    
SELECT 
    u.id_usuario, u.nombre AS nombre_usuario, u.apellido, u.ciudad, u.direccion, u.telefono, u.email,
    p.id_usuario AS id_propietario
FROM 
    usuarios u
INNER JOIN 
    propietarios p ON u.id_usuario = p.id_usuario;
    
SELECT 
    u.id_usuario, u.nombre AS nombre_usuario, u.apellido, u.ciudad, u.direccion, u.telefono, u.email,
    a.id_usuario,a.cargo,a.fecha_ingreso AS id_administrador,cargo,fecha_ingreso
FROM 
    usuarios u
INNER JOIN 
    administradores a ON u.id_usuario = a.id_usuario;
    
SELECT 
    u.id_usuario, u.nombre AS nombre_usuario, u.apellido, u.ciudad, u.direccion, u.telefono, u.email,
    v.id_usuario,v.especialidad,v.horario AS id_veterinario,especialidad,horario
FROM 
    usuarios u
INNER JOIN 
    veterinarios v ON u.id_usuario = v.id_usuario;

SELECT 
    u.id_usuario, 
    UPPER(u.nombre) AS nombre_usuario, 
    UPPER(u.apellido) AS apellido, 
    UPPER(u.ciudad) AS ciudad, 
    UPPER(u.direccion) AS direccion, 
    u.telefono, 
    LOWER(u.email) AS email,
    p.id_usuario AS id_propietario,
    m.codigo AS codigo_mascota, 
    UPPER(m.nombre) AS nombre_mascota, 
    UPPER(m.especie) AS especie, 
    UPPER(m.raza) AS raza, 
    m.edad, 
    m.peso
FROM 
    usuarios u
INNER JOIN 
    propietarios p ON u.id_usuario = p.id_usuario
INNER JOIN 
    mascotas m ON p.id_usuario = m.id_usuario;

DELIMITER //

CREATE PROCEDURE CrearMascota(
    IN p_codigo INT,
    IN p_nombre VARCHAR(255),
    IN p_especie VARCHAR(255),
    IN p_raza VARCHAR(255),
    IN p_edad FLOAT,
    IN p_peso FLOAT,
    IN p_usuario INT
)
BEGIN
    INSERT INTO mascotas (codigo, nombre, especie, raza, edad, peso,id_usuario)
    VALUES (p_codigo, p_nombre, p_especie, p_raza, p_edad, p_peso, p_usuario);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE BuscarMascota(
    IN p_codigo INT
)
BEGIN
    SELECT *
    FROM mascotas
    WHERE codigo = p_codigo;
END //

DELIMITER ;

call BuscarMascota(10);

DELIMITER //

CREATE PROCEDURE ActualizarMascota(
    IN p_codigo INT,
    IN p_nombre VARCHAR(255),
    IN p_especie VARCHAR(255),
    IN p_raza VARCHAR(255),
    IN p_edad FLOAT,
    IN p_peso FLOAT
)
BEGIN
    UPDATE mascotas
    SET 
		nombre = p_nombre,
        especie = p_especie,
        raza = p_raza,
        edad = p_edad,
        peso = p_peso
    WHERE codigo = p_codigo;
END //

DELIMITER ;

call ActualizarMascota(1001,'MELSA','GATA','PERZA',5.00,12.00);

DELIMITER //

CREATE PROCEDURE EliminarMascota(
    IN p_codigo INT
)
BEGIN
    DELETE FROM mascotas WHERE codigo = p_codigo;
END //

DELIMITER ;

call EliminarMascota(1022);

DELIMITER //

CREATE PROCEDURE CrearHistorial(
    IN p_id INT,
    IN p_fecha DATE,
    IN p_descripcion VARCHAR(255),
    IN p_tratamiento VARCHAR(255),
    IN p_codigo_mascota INT
)
BEGIN
     INSERT INTO historial_medico (id,fecha,descripcion,tratamiento,codigo_mascota)
    VALUES (p_id, p_fecha, p_descripcion, p_tratamiento, p_codigo_mascota);
END //

DELIMITER ;
call CrearHistorial (1001,'2024-02-09','VACUNA DE RABIA','VACUNA NOBIVAC',1000);