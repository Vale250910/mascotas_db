CREATE DATABASE IF NOT EXISTS mascotas_db;
USE mascotas_db;

CREATE TABLE usuarios (
tipo_documento ENUM ('C.C','C.E','T.I')DEFAULT 'C.C',
n_documento VARCHAR(40)PRIMARY KEY NOT NULL,
nombre VARCHAR(50) NOT NULL,
apellido VARCHAR(30) NOT NULL,
ciudad VARCHAR(50) NOT NULL,
direccion VARCHAR(100) NOT NULL,
telefono VARCHAR(20) NOT NULL,
es_propietario BOOLEAN DEFAULT 1 NOT NULL,
es_veterinario BOOLEAN DEFAULT 1 NOT NULL,
es_administrador BOOLEAN DEFAULT 1 NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
contraseña VARCHAR(255) NOT NULL,
estado_acceso ENUM('ACTIVO', 'INACTIVO') DEFAULT 'ACTIVO'
);

CREATE TABLE administradores (
n_documento VARCHAR(40)PRIMARY KEY NOT NULL,
cargo VARCHAR(100) NOT NULL,
fecha_ingreso DATE NOT NULL,
FOREIGN KEY (n_documento) REFERENCES usuarios(n_documento)
ON DELETE NO ACTION
ON UPDATE NO ACTION
);

CREATE TABLE propietarios (
n_documento VARCHAR(40)PRIMARY KEY NOT NULL,
barrio VARCHAR(100) NOT NULL,
FOREIGN KEY (n_documento) REFERENCES usuarios(n_documento)
ON DELETE NO ACTION
ON UPDATE NO ACTION
);

CREATE TABLE veterinarios (
n_documento VARCHAR(40)PRIMARY KEY NOT NULL,
especialidad VARCHAR(100)NOT NULL,
horario VARCHAR(255)NOT NULL,
FOREIGN KEY (n_documento) REFERENCES usuarios(n_documento)
ON DELETE NO ACTION
ON UPDATE NO ACTION
);

CREATE TABLE mascotas (
codigo VARCHAR(40)PRIMARY KEY NOT NULL,
nombre VARCHAR (100) NOT NULL,
especie VARCHAR (100) NOT NULL,
raza VARCHAR (100) NOT NULL,
edad DECIMAL (10,2) NOT NULL,
peso DECIMAL (10,2) NOT NULL,
n_documento VARCHAR(40) NOT NULL,
estado_acceso ENUM('ACTIVO', 'INACTIVO') DEFAULT 'ACTIVO',
FOREIGN KEY (n_documento) references propietarios(n_documento)
ON DELETE NO ACTION
ON UPDATE NO ACTION
);
CREATE TABLE historiales_medicos(
codigo VARCHAR(40)NOT NULL ,
fecha DATE NOT NULL,
descripcion TEXT,
tratamiento TEXT,
codigo_mascota VARCHAR(40) NOT NULL,
estado_acceso ENUM('ACTIVO', 'INACTIVO') DEFAULT 'ACTIVO',
PRIMARY KEY(codigo,codigo_mascota),
FOREIGN KEY (codigo_mascota) REFERENCES mascotas(codigo)
);
CREATE TABLE servicios(
codigo VARCHAR(40) NOT NULL PRIMARY KEY ,
nombre VARCHAR(100)NOT NULL,
descripcion TEXT,
precio DECIMAL (20,2)NOT NULL,
estado_acceso ENUM('ACTIVO', 'INACTIVO') DEFAULT 'ACTIVO'
);
CREATE TABLE citas(
codigo VARCHAR(40) NOT NULL PRIMARY KEY ,
fecha DATE NOT NULL,
hora TIME,
id_servicio VARCHAR(40) NOT NULL,
n_documento VARCHAR(40) NOT NULL,
codigo_mascota VARCHAR(40) NOT NULL,
estado ENUM('PENDIENTE', 'CONFIRMADA', 'CANCELADA', 'REALIZADA', 'NO_ASISTIDA') NOT NULL DEFAULT 'PENDIENTE',
estado_acceso ENUM('ACTIVO', 'INACTIVO') DEFAULT 'ACTIVO',
FOREIGN KEY (id_servicio) REFERENCES servicios(codigo),
FOREIGN KEY (n_documento) REFERENCES veterinarios(n_documento),
FOREIGN KEY (codigo_mascota) REFERENCES mascotas(codigo)
);
CREATE TABLE productos(
    codigo VARCHAR(40) NOT NULL PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT(100),
    precio DECIMAL(10,2), -- Especificar precisión y escala
    stock SMALLINT UNSIGNED NOT NULL,
    estado_acceso ENUM('ACTIVO', 'INACTIVO') DEFAULT 'ACTIVO'
);

-- Usuarios
INSERT INTO usuarios (n_documento, nombre, apellido, ciudad, direccion, telefono, es_propietario, es_veterinario, es_administrador, email, contraseña) VALUES
('101', 'ALBERTO', 'DI CAPRIO', 'PALMIRA', 'CALLE 45', '31295858', 1, 0, 0, 'alberto@gmail.com', '4321'),
('102', 'JAQUELINE', 'ACOSTA', 'FACATATIVA', 'CALLE 51', '313409449', 0, 0, 0, 'jaqueline@gmail.com', '987'),
('103', 'MARIANA', 'URQUIJO', 'SOACHA', 'CALLE 84', '31404534', 0, 0, 0, 'mariana@gmail.com', '98712'),
('104', 'RICARDO JORGE', 'ESPITIA', 'COTA', 'CALLE 31', '31343333', 1, 0, 0, 'jorge@gmail.com', '12345678'),
('105', 'PEPE', 'CORTISONIA', 'SIBATE', 'CALLE 88', '3114393', 0, 0, 0, 'pepe@gmail.com', '4321'),
('106', 'LILIANA', 'MANRIQUE', 'SOACHA', 'CALLE 99 14-44', '3103559658', 1, 0, 0, 'liliana@gmail.com', '54321'),
('107', 'HAROLD', 'LOZANO', 'SIBATE', 'CALLE 12-3', '313598', 0, 0, 0, 'harold@gmail.com', '54321'),
('108', 'FRANCISCO', 'PARRA', 'MOSQUERA', 'CALLE 13 12-44', '311857372', 0, 0, 0, 'francisco@gmail.com', '123'),
('109', 'SOFIA', 'MENDIETE', 'BOGOTA', 'CALLE 80 4-8', '312987', 1, 0, 0, 'sofia@gmail.com', '123'),
('110', 'MARIO', 'CHIPOLLINI', 'NAPOLES - ITALIA', 'CALLE 12 13-43', '311857372', 1, 0, 0, 'mario@gmail.com', '123');

-- Propietarios
INSERT INTO propietarios (n_documento, barrio) VALUES
('101', 'SOACHA'),
('104', 'BOSA'),
('106', 'GUATAPE'),
('109', 'SOACHA COMPARTIR'),
('110', 'SAN MATEO');

-- Mascotas
INSERT INTO mascotas (codigo, nombre, especie, raza, edad, peso, n_documento) VALUES
('1', 'Firulais', 'Perro', 'Pastor Alemán', 5, 30.5, '101'),
('2', 'Mishi', 'Gato', 'Siames', 3, 5.2, '104'),
('3', 'Bunny', 'Conejo', 'Mini Lop', 2, 1.8, '106');

-- Administradores
INSERT INTO administradores (n_documento, cargo, fecha_ingreso) VALUES
('102', 'Administrador General', '2023-01-15'),
('103', 'Administrador de Recursos Humanos', '2023-02-20'),
('104', 'Administrador de TI', '2023-03-05'),
('108', 'Administrador Financiero', '2023-04-10'),
('110', 'Administrador de Operaciones', '2023-05-25');

-- Veterinarios
INSERT INTO veterinarios (n_documento, especialidad, horario) VALUES
('105', 'Cirugía', 'Lunes a Viernes, 8:00 - 17:00'),
('106', 'Dermatología', 'Martes a Sábado, 9:00 - 18:00'),
('107', 'Oftalmología', 'Lunes a Viernes, 8:00 - 17:00'),
('108', 'Cardiología', 'Miércoles a Domingo, 10:00 - 19:00'),
('109', 'Neurología', 'Jueves a Lunes, 9:00 - 18:00');

-- Servicios
INSERT INTO servicios (codigo, nombre, descripcion, precio) VALUES
('1', 'Vacunación', 'Aplicación de vacunas básicas', 50.00),
('2', 'Consulta General', 'Revisión médica completa', 30.00),
('3', 'Cirugía Menor', 'Procedimientos quirúrgicos de bajo riesgo', 200.00);

-- Citas
INSERT INTO citas (codigo, fecha, hora, id_servicio, n_documento, codigo_mascota) VALUES
('1', '2023-09-10', '10:00:00', '1', '105', '1'),
('2', '2023-09-15', '14:00:00', '2', '105', '2'),
('3', '2023-09-20', '09:30:00', '3', '107', '3');

-- Historiales Médicos
INSERT INTO historiales_medicos (codigo, fecha, descripcion, tratamiento, codigo_mascota) VALUES
('1', '2023-09-01', 'Vacuna antirrábica aplicada', 'Descanso y monitoreo de 24 horas', '1'),
('2', '2023-08-15', 'Desparasitación', 'Administrar medicamento por 5 días', '2'),
('3', '2023-07-22', 'Revisión general', 'Dieta controlada', '3');

-- Productos
INSERT INTO productos (codigo, nombre, descripcion, precio, stock) VALUES
('1', 'Alimento para perros', 'Alimento premium para perros adultos', 25.99, 50),
('2', 'Juguete para gatos', 'Juguete interactivo con plumas', 9.99, 100),
('3', 'Collar antipulgas', 'Collar para eliminar y prevenir pulgas', 15.50, 30);
-- inner join
-- Ver todos los usuarios
SELECT * FROM usuarios;

-- Ver todos los propietarios
SELECT * FROM propietarios;

-- Ver todas las mascotas
SELECT * FROM mascotas;

-- Ver todos los administradores
SELECT * FROM administradores;

-- Ver todos los veterinarios
SELECT * FROM veterinarios;

-- Ver todos los servicios
SELECT * FROM servicios;

-- Ver todas las citas
SELECT * FROM citas;

-- Ver todos los historiales médicos
SELECT * FROM historiales_medicos;

-- Ver todos los productos
SELECT * FROM productos;

SELECT 
    u.n_documento, u.nombre AS nombre_usuario, u.apellido, u.ciudad, u.direccion, u.telefono, u.email,
    p.n_documento AS id_propietario,
    m.codigo AS codigo_mascota, m.nombre AS nombre_mascota, m.especie, m.raza, m.edad, m.peso
FROM 
    usuarios u
INNER JOIN 
    propietarios p ON u.n_documento = p.n_documento
INNER JOIN 
    mascotas m ON p.n_documento = m.n_documento;
    
SELECT 
    u.n_documento, u.nombre AS nombre_usuario, u.apellido, u.ciudad, u.direccion, u.telefono, u.email,
    p.n_documento AS id_propietario
FROM 
    usuarios u
INNER JOIN 
    propietarios p ON u.n_documento = p.n_documento;
    
SELECT 
    u.n_documento, u.nombre AS nombre_usuario, u.apellido, u.ciudad, u.direccion, u.telefono, u.email,
    a.n_documento,a.cargo,a.fecha_ingreso AS id_administrador,cargo,fecha_ingreso
FROM 
    usuarios u
INNER JOIN 
    administradores a ON u.n_documento = a.n_documento;
    
SELECT 
    u.n_documento, u.nombre AS nombre_usuario, u.apellido, u.ciudad, u.direccion, u.telefono, u.email,
    v.n_documento,v.especialidad,v.horario AS id_veterinario,especialidad,horario
FROM 
    usuarios u
INNER JOIN 
    veterinarios v ON u.n_documento = v.n_documento;

SELECT 
    u.n_documento, 
    UPPER(u.nombre) AS nombre_usuario, 
    UPPER(u.apellido) AS apellido, 
    UPPER(u.ciudad) AS ciudad, 
    UPPER(u.direccion) AS direccion, 
    u.telefono, 
    LOWER(u.email) AS email,
    p.n_documento AS id_propietario,
    m.codigo AS codigo_mascota, 
    UPPER(m.nombre) AS nombre_mascota, 
    UPPER(m.especie) AS especie, 
    UPPER(m.raza) AS raza, 
    m.edad, 
    m.peso
FROM 
    usuarios u
INNER JOIN 
    propietarios p ON u.n_documento = p.n_documento
INNER JOIN 
    mascotas m ON p.n_documento = m.n_documento
    ;



