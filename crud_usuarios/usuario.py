import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import bcrypt
from base_datos.conexion10 import BaseDatos

class Usuario:
    def __init__(self,
                tipo_documento:str = None,
                n_documento:str=None, 
                nombre:str = None,
                apellido:str = None,
                ciudad:str = None,
                direccion:str = None,
                telefono:str = None,
                es_propietario:bool = None,
                es_veterinario:bool = None,
                es_administrador:bool = None,
                email:str = None, 
                contraseña:str = None,
                estado_acceso:str = None,):
        # Inicializa los atributos del usuario
        self.__tipo_documento = tipo_documento
        self.__n_documento = n_documento
        self.__nombre = nombre
        self.__apellido = apellido
        self.__ciudad = ciudad
        self.__direccion = direccion
        self.__telefono = telefono
        self.__es_propietario = es_propietario
        self.__es_veterinario = es_veterinario
        self.__es_administrador = es_administrador
        self.__email = email
        self.__contraseña = contraseña
        self.__estado_acceso = estado_acceso
        
    # Métodos GET y SET para cada atributo
    def get_tipo_documento(self):
        return self.__tipo_documento
    
    def set_tipo_documento(self):
        while True:
            try:
                tipo_documento = input('Ingrese el tipo de documento (C.C/T.I/C.E): ').upper().strip()

                if len(tipo_documento) != 3:
                    print('El tipo de documento debe tener exactamente 2 caracteres.')
                    continue
                if tipo_documento in ['C.C', 'T.I', 'C.E']:
                    self.__tipo_documento = tipo_documento
                    break
                else:
                    print('Tipo de documento inválido. Por favor, ingrese C.C, T.I o C.E.')
            except KeyboardInterrupt:
                print('\nEl usuario ha cancelado la entrada de datos.')
                break

    def get_n_documento(self):
        return self.__n_documento

    def set_n_documento(self):
        while True:
            try:
                n_documento = input('Ingrese el numero de identificación: ').strip()
                if n_documento.isdigit() and 1 <= len(n_documento) <= 1000000000:
                    self.__n_documento = n_documento
                    break
                else:
                    print('El número de documento debe ser una cadena de 1 a 1000000000 dígitos.')
            except KeyboardInterrupt:
                print('\nEl usuario ha cancelado la entrada de datos.')
                return None 
            
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self):
        while True:
            try:
                # Solicita el nombre del usuario y valida su longitud
                nombre = input('Ingrese el nombre : ')
                if len(nombre) > 1:
                    self.__nombre = nombre
                    break
                else:
                    print('Nombre incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
    
    def get_apellido(self):
        return self.__apellido

    def set_apellido(self):
        while True:
            try:
                # Solicita el apellido del usuario y valida su longitud
                apellido = input('Ingrese el apellido: ')
                if len(apellido) > 1:
                    self.__apellido = apellido
                    break
                else:
                    print('Apellido incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def get_ciudad(self):
        return self.__ciudad

    def set_ciudad(self):
        while True:
            try:
                # Solicita la ciudad del usuario y valida su longitud
                ciudad = input('Ingrese la ciudad: ')
                if len(ciudad) > 1:
                    self.__ciudad = ciudad
                    break
                else:
                    print('Ciudad incorrecta. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
        
    def get_direccion(self):
        return self.__direccion

    def set_direccion(self):
        while True:
            try:
                # Solicita la dirección del usuario y valida su longitud
                direccion = input('Ingrese la dirección: ')
                if len(direccion) > 1:
                    self.__direccion = direccion
                    break
                else:
                    print('Dirección incorrecta. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue  

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self):
        while True:
            try:
                telefono = input('Ingrese el telefono: ').strip()
                if telefono.isdigit() and 7<= len(telefono) <= 20:
                    self.__telefono = telefono
                    break
                else:
                    print('El telefono debe ser una cadena de 1 a 20 dígitos.')
            except KeyboardInterrupt:
                print('\nEl usuario ha cancelado la entrada de datos.')
                return None 

    def get_es_propietario(self):
        return self.__es_propietario

    def set_es_propietario(self):
        while True:
            # Solicita si el usuario es propietario y valida la respuesta
            respuesta = input("¿Es propietario? (si/no): ").strip().lower()
            if respuesta == "si" or respuesta == "sí":
                self.__es_propietario = 1  # Representa "sí" como 1
                break 
            elif respuesta == "no":
                self.__es_propietario = 0  # Representa "no" como 0
                break
            else:
                print("Respuesta inválida. Por favor, ingrese 'sí' o 'no'.")
        return self.__es_propietario
    
    def get_es_veterinario(self):
        return self.__es_veterinario

    def set_es_veterinario(self):
        while True:
            # Solicita si el usuario es veterinario y valida la respuesta
            respuesta = input("¿Es veterinario? (sí/no): ").strip().lower()
            if respuesta == "si" or respuesta == "sí":
                self.__es_veterinario = 1  # Representa "sí" como 1
                break
            elif respuesta == "no":
                self.__es_veterinario = 0  # Representa "no" como 0
                break
            else:
                print("Respuesta inválida. Por favor, ingrese 'sí' o 'no'.")
        return self.__es_veterinario
    
    def get_es_administrador(self):
        return self.__es_administrador

    def set_es_administrador(self):
        while True:
            # Solicita si el usuario es administrador y valida la respuesta
            respuesta = input("¿Es administrador? (sí/no): ").strip().lower()
            if respuesta == "si" or respuesta == "sí":
                self.__es_administrador = 1  # Representa "sí" como 1
                break
            elif respuesta == "no":
                self.__es_administrador = 0  # Representa "no" como 0
                break
            else:
                print("Respuesta inválida. Por favor, ingrese 'sí' o 'no'.")
        return self.__es_administrador

    def get_email(self):
        return self.__email

    def set_email(self):
        while True:
            # Solicita el correo electrónico del usuario y valida su formato y longitud
            email = input('Ingrese el correo electrónico (5-100 caracteres): ')
            if not isinstance(email, str):
                raise TypeError("El correo electrónico debe ser una cadena")
            if len(email) < 5:
                raise ValueError("El correo electrónico debe tener al menos 5 caracteres")
            if len(email) > 100:
                raise ValueError("El correo electrónico debe tener como máximo 100 caracteres")
            if "@" not in email:
                raise ValueError("El correo electrónico debe contener un arroba (@)")
            if "." not in email:
                raise ValueError("El correo electrónico debe contener un punto (.)")
            self.__email = email
            break
        return email

    def get_contraseña(self):
        return self.__contraseña

    def set_contraseña(self):
        while True:
            # Solicita la contraseña del usuario y valida su longitud
            contraseña = input("Ingrese la contraseña (5-20 caracteres): ")
            if 5 <= len(contraseña) <= 20:
                # Genera un salt seguro
                salt = bcrypt.gensalt()

                # Realiza un cifrado seguro con bcrypt y el salt generado
                contraseña_cifrada = bcrypt.hashpw(contraseña.encode('utf-8'), salt)
                # Asigna la contraseña cifrada a la variable privada
                self.__contraseña = contraseña_cifrada
                print("Contraseña establecida correctamente.")
                break
            else:
                print("La contraseña debe tener entre 5 y 20 caracteres.")

    def verificar_contraseña(self, contraseña_ingresada):
        # Verifica la contraseña ingresada contra la contraseña cifrada almacenada
        return bcrypt.checkpw(contraseña_ingresada.encode('utf-8'), self.__contraseña)
    
    def get_estado_acceso(self):
        return self.__estado_acceso
    
    def set_estado_acceso(self):
        while True:
            try:
                estado_acceso = input('Ingrese el estado de acceso (ACTIVO o INACTIVO): ').upper().strip()
                # Validar longitud y contenido
                if estado_acceso not in ['ACTIVO','INACTIVO']:
                    print('Estado inválido. Por favor, ingrese ACTIVO o INACTIVO.')
                    continue
                
                self.__estado_acceso = estado_acceso
                break
                
            except KeyboardInterrupt:
                print('\nEl usuario ha cancelado la entrada de datos.')
                break


    
    def capturar_datos(self):
        # Captura y establece todos los datos del usuario
        self.set_tipo_documento()
        self.set_n_documento()
        self.set_nombre()
        self.set_apellido()
        self.set_ciudad()
        self.set_direccion()
        self.set_telefono()
        self.set_es_propietario()
        self.set_es_veterinario()
        self.set_es_administrador()
        self.set_email()
        self.set_contraseña()
        self.set_estado_acceso()        
