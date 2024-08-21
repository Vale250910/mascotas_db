
CREATE DATABASE castaño_db;
USE castaño_db;
CREATE TABLE computadoras(
codigo INT UNSIGNED PRIMARY KEY NOT NULL,
marca VARCHAR(45),
modelo VARCHAR(45),
procesador VARCHAR(45),
cap_memoria DECIMAL(20,2),
cap_almacenamiento DECIMAL(20,2)
);
CREATE TABLE cuentahabientes(
id_cuentahabiente INT UNSIGNED PRIMARY KEY NOT NULL,
nombre VARCHAR(45)NOT NULL,
apellido1 VARCHAR(45)NOT NULL,
correo VARCHAR(45)NOT NULL UNIQUE,
telefono VARCHAR(45) NOT NULL
);

CREATE TABLE cuentas (
numero_cuenta INT UNSIGNED PRIMARY KEY,
tipo ENUM ('AHORROS','CORRIENTE'),
saldo INT NOT NULL,
id_cuentahabiente INT UNSIGNED NOT NULL,
FOREIGN KEY(id_cuentahabiente)REFERENCES cuentahabientes(id_cuentahabiente)
);
CREATE TABLE movimientos(
codigo_movimiento INT UNSIGNED NOT NULL ,  
numero_cuenta INT UNSIGNED NOT NULL,
fecha DATE,
hora TIME,
tipo_mov ENUM('C','R'),
PRIMARY KEY(codigo_movimiento,numero_cuenta),
FOREIGN KEY (numero_cuenta) REFERENCES cuentas(numero_cuenta)
);

DELIMITER //
CREATE PROCEDURE InsertarCuenta(
IN p_numero_cuenta INT,
IN p_tipo ENUM('AHORROS','CORRIENTE'),
IN p_saldo INT,
IN p_id_cuentahabiente INT
)
BEGIN
	INSERT INTO cuentas(numero_cuenta,tipo,saldo,id_cuentahabiente)
	VALUES (p_numero_cuenta,p_tipo,p_saldo,p_id_cuentahabiente);
END //

CALL InsertarCuenta(101,'AHORROS',  101, 105);
DELIMITER //
CREATE PROCEDURE BuscarCuenta(
IN p_numero_cuenta INT
)
BEGIN
	SELECT*FROM cuentas WHERE numero_cuenta =p_numero_cuenta;
END //
CALL BuscarCuenta(101);