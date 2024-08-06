import mysql.connector
from mysql.connector import Error
import os

def conectar():
    try:
        conexion =mysql.connector.connect(
            host ='localhost',
            database ='mascotas_db',
            user='root',
            password='12345678',
            port=3306
        )
        if conexion.is_connected():
            print("Conexión existosa")
            return conexion
    except Error as e:
     print(f"Error al conectar a MYSQL{e}")
    return None

def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
    print("Conexión cerrada")

def insertar_usuarios(conexion,id_usuario,nombre,apellido,ciudad,direccion,telefono,es_propietario,es_veterinario,es_administrador,email,contraseña):
    try:
        cursor =conexion.cursor()
        sql ="INSERT INTO usuarios(id_usuario,nombre,apellido,ciudad,direccion,telefono,es_propietario,es_veterinario,es_administrador,email,contraseña) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        datos=(id_usuario,nombre,apellido,ciudad,direccion,telefono,es_propietario,es_veterinario,es_administrador,email,contraseña)
        cursor.execute(sql,datos)
        conexion.commit()
        print("Usuario insertado existosamente")
    except Error as e:
        print(f"Error al insertar Usuario{e}")

def main():
    conexion=conectar()
    if conexion:
        print("*******************Usuario***************************")
        id_usuario= input("Ingrese el id del usuario -->")
        nombre= input("Ingrese el nombre del usuario -->")
        apellido= input("Ingese el apellido del usuario -->")
        ciudad =input("Ingrese la ciudad del usuario-->")
        direccion=input("Ingrese la direccion del usuario-_>")
        telefono=input("Ingrese el telefono de el usuario-->")
        es_propietario= input("Ingrese 1(si) o 0 (no) es propietario -->")
        es_veterinario= input("Ingrese 1(si) o 0 (no) es veterinario -->")
        es_administrador= input("Ingrese 1(si) o 0 (no) es administrador -->")
        email=input("Ingrese el email del usuario -->")
        contraseña=input("Ingrese la contraseña del usuario -->")
        insertar_usuarios(conexion,id_usuario,nombre,apellido,ciudad,direccion,telefono,es_propietario,es_veterinario,es_administrador,email,contraseña)
        cerrar_conexion(conexion)
        print("*******************************************************")
        os.system("pause")
        os.system("cls")
        
if __name__ =="__main__":
    main()