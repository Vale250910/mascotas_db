CREATE DATABASE IF NOT EXISTS mascotas_db;
USE mascotas_db;

CREATE TABLE usuarios (
id_usuario INT UNSIGNED PRIMARY KEY NOT NULL,
nombre VARCHAR(50) NOT NULL,
apellido VARCHAR(30) NOT NULL,
ciudad VARCHAR(50) NOT NULL,
direccion VARCHAR(100) NOT NULL,
telefono VARCHAR(20) NOT NULL,
es_propietario BOOLEAN DEFAULT FALSE,
es_veterinario BOOLEAN DEFAULT FALSE,
es_administrador BOOLEAN DEFAULT FALSE,
email VARCHAR(100) NOT NULL UNIQUE,
contraseña VARCHAR(255) NOT NULL
);

CREATE TABLE administradores (
id_usuario INT UNSIGNED PRIMARY KEY NOT NULL,
cargo VARCHAR(100) NOT NULL,
fecha_ingreso DATE NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION
);

CREATE TABLE propietarios (
id_usuario INT UNSIGNED PRIMARY KEY NOT NULL,
barrio VARCHAR(100) NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION
);

CREATE TABLE veterinarios (
id_usuario INT UNSIGNED PRIMARY KEY NOT NULL,
especialidad VARCHAR(100)NOT NULL,
horario VARCHAR(255)NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION
);

CREATE TABLE mascotas (
codigo INT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
nombre VARCHAR (100) NOT NULL,
especie VARCHAR (100) NOT NULL,
raza VARCHAR (100) NOT NULL,
edad DECIMAL (10,2) NOT NULL,
peso DECIMAL (10,2) NOT NULL,
id_usuario INT UNSIGNED NOT NULL,
FOREIGN KEY (id_usuario) references propietarios(id_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION
);
CREATE TABLE historiales_medicos(
codigo INT UNSIGNED  NOT NULL AUTO_INCREMENT,
fecha DATE NOT NULL,
descripcion TEXT,
tratamiento TEXT,
codigo_mascota INT UNSIGNED NOT NULL,
PRIMARY KEY(codigo,codigo_mascota),
FOREIGN KEY (codigo_mascota) REFERENCES mascotas(codigo)
);
CREATE TABLE servicios(
codigo INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100)NOT NULL,
descripcion TEXT,
precio DECIMAL (20,2)NOT NULL
);
CREATE TABLE citas(
codigo INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
fecha DATE NOT NULL,
hora TIME,
id_servicio INT UNSIGNED NOT NULL,
id_veterinario INT UNSIGNED NOT NULL,
codigo_mascota INT UNSIGNED NOT NULL,
estado ENUM('PENDIENTE', 'CONFIRMADA', 'CANCELADA', 'REALIZADA', 'NO_ASISTIDA') NOT NULL DEFAULT 'PENDIENTE',
FOREIGN KEY (id_servicio) REFERENCES servicios(codigo),
FOREIGN KEY (id_veterinario) REFERENCES veterinarios(id_usuario),
FOREIGN KEY (codigo_mascota) REFERENCES mascotas(codigo)
);
CREATE TABLE productos(
    codigo INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    descripcion TEXT(100),
    precio DECIMAL(10,2), -- Especificar precisión y escala
    stock SMALLINT UNSIGNED NOT NULL
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

INSERT INTO propietarios (id_usuario,barrio) VALUES
(101,'SOACHA'),
(104,'BOSA'),
(106,'GUATAPE'),
(109,'SOACHA COMPARTIR'),
(110,'SAN MATEO');
SELECT * FROM propietarios;

INSERT INTO mascotas (nombre, especie, raza, edad, peso, id_usuario) VALUES
('MELSO', 'PERRO', 'BULL DOG', 5.00, 12.00, 101),
('PULGAS', 'PERRO', 'FRENCH PULGA', 4.00, 3.00, 101),
('PELROJO', 'GATO', 'CRILLO COLOMBIANO', 2.00, 2.00, 106);
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

INSERT INTO servicios (nombre, descripcion, precio) VALUES
('Consulta General', 'Consulta veterinaria general', 50000.00),
('Vacunación', 'Aplicación de vacunas', 35000.00),
('Desparasitación', 'Tratamiento antiparasitario', 30000.00),
('Cirugía', 'Procedimiento quirúrgico', 200000.00),
('Peluquería', 'Servicio de peluquería para mascotas', 40000.00);
SELECT * FROM servicios;

INSERT INTO citas (fecha, hora, id_servicio, id_veterinario, codigo_mascota, estado) VALUES
('2024-08-20', '10:00:00', 1, 105, 1, 'CONFIRMADA'),
('2024-08-21', '11:00:00', 2, 106, 2, 'PENDIENTE'),
('2024-08-22', '12:00:00', 3, 107, 3, 'CANCELADA'),
('2024-08-23', '09:00:00', 4, 108, 1, 'REALIZADA'),
('2024-08-24', '14:00:00', 5, 109, 2, 'NO_ASISTIDA');
SELECT*FROM citas;

INSERT INTO historiales_medicos ( fecha, descripcion, tratamiento, codigo_mascota) VALUES
('2024-07-01', 'Revisión general', 'Administrar antiparasitarios', 1),
('2024-07-10', 'Vacunación', 'Vacuna contra la rabia aplicada', 2),
('2024-07-15', 'Cirugía menor', 'Extracción de quiste', 3),
('2024-08-05', 'Consulta por alergias', 'Administrar antihistamínicos', 1),
('2024-08-10', 'Consulta de control', 'Chequeo general', 2);
SELECT*FROM historiales_medicos;

INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
('Alimento para Perro', 'Alimento balanceado para perros adultos', 45000.00, 50),
('Alimento para Gato', 'Alimento balanceado para gatos adultos', 50000.00, 40),
('Juguete para Perro', 'Pelota resistente para perros', 15000.00, 100),
('Collar Antipulgas', 'Collar para prevención de pulgas y garrapatas', 35000.00, 75),
('Arena para Gatos', 'Arena higiénica para gatos', 20000.00, 60);
SELECT * FROM productos;
-- inner join

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



