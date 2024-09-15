import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos.conexion10 import BaseDatos
from crud_usuarios.usuario import Usuario

class Veterinario(Usuario):
    def __init__(self, especialidad: str = None, horario: str = None, **kwargs):
        """
        Constructor de la clase Veterinario que hereda de Usuario.
        Inicializa los atributos adicionales: especialidad y horario.
        """
        super().__init__(**kwargs)  # Llama al constructor de la clase base Usuario
        self.__especialidad = especialidad
        self.__horario = horario

    def get_especialidad(self):
        """Retorna la especialidad del veterinario."""
        return self.__especialidad

    def set_especialidad(self):
        """
        Solicita al usuario que ingrese la especialidad del veterinario y valida la entrada.
        La especialidad debe tener más de 3 caracteres.
        """
        while True:
            try:
                especialidad = input('Especialidad del veterinario: ')
                if len(especialidad) > 3:
                    self.__especialidad = especialidad
                    break
                else:
                    print('Especialidad incorrecta. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos')
                continue

    def get_horario(self):
        """Retorna el horario del veterinario."""
        return self.__horario
    
    def set_horario(self):
        """
        Solicita al usuario que ingrese el horario del veterinario y valida la entrada.
        El horario debe tener más de 3 caracteres.
        """
        while True:
            try:
                horario = input('Horario del veterinario: ')
                if len(horario) > 3:
                    self.__horario = horario
                    break
                else:
                    print('Horario incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos')
                continue

    def capturar_datos(self):
        """Captura los datos del veterinario, incluyendo los datos heredados de Usuario."""
        super().capturar_datos()  # Captura los datos del usuario base
        self.set_especialidad()
        self.set_horario()

    def registrar_veterinarios(self):
        """
        Registra un veterinario en la base de datos.
        Llama al procedimiento almacenado 'InsertarVeterinario' y maneja posibles errores.
        """
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_veterinario = conexion.cursor()
                cursor_veterinario.callproc('InsertarVeterinario', [
                    self.get_id_usuario(),
                    self.get_nombre(),
                    self.get_apellido(),
                    self.get_ciudad(),
                    self.get_direccion(),
                    self.get_telefono(),
                    self.get_es_propietario(),
                    self.get_es_veterinario(),
                    self.get_es_administrador(),
                    self.get_email(),
                    self.get_contraseña(),
                    self.get_especialidad(),
                    self.get_horario()
                ])
                conexion.commit()
                print('Veterinario registrado correctamente...')
                
                print('\nDatos del veterinario registrados:')
                print('------------------------------------------')
                print(f'Id propietario: {self.get_id_usuario()}')
                print(f'Nombre: {self.get_nombre()}')
                print(f'Apellido: {self.get_apellido()}')
                print(f'Ciudad: {self.get_ciudad()}')
                print(f'Dirección: {self.get_direccion()}')
                print(f'Teléfono: {self.get_telefono()}')
                print(f'Es propietario: {self.get_es_propietario()}')
                print(f'Es veterinario: {self.get_es_veterinario()}') 
                print(f'Es administrador: {self.get_es_administrador()}')
                print(f'Email: {self.get_email()}')
                print(f'Contraseña: {self.get_contraseña()}')
                print(f'Especialidad: {self.get_especialidad()}')
                print(f'Horario: {self.get_horario()}')
            except Exception as e:
                print(f'Error al registrar el veterinario: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
                
    def consultar_veterinarios(self):
        """
        Consulta y muestra todos los veterinarios registrados en la base de datos.
        Llama al procedimiento almacenado 'MostrarTodosVeterinarios' y maneja posibles errores.
        """
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_veterinario = conexion.cursor()
                cursor_veterinario.callproc('MostrarTodosVeterinarios')
                print('Listado de todas los veterinarios completado.')
                veterinario_encontrado = False
                for result in cursor_veterinario.stored_results():
                    filas = result.fetchall()
                    if filas:
                        veterinario_encontrado = True
                        for datos in filas:
                            print('Resultado:')
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                            f"| Id propietario    : {datos[0]:<20}   | Nombre           : {datos[1]:<20}  \n" +
                            f"| Apellido          : {datos[2]:<20}   | Ciudad           : {datos[3]:<20}  \n" +
                            f"| Dirección         : {datos[4]:<20}   | Teléfono         : {datos[5]:<20}  \n" +
                            f"| Es propietario    : {datos[6]:<20}   | Es veterinario   : {datos[7]:<20}  \n" +
                            f"| Es administrador  : {datos[8]:<20}   | Email            : {datos[9]:<20}  \n" +
                            f"| Especialidad      : {datos[11]:<20}\n"+
                            f"| Horario           : {datos[12]:<20}"
                            '\033[0;m')
                            print('**********************************************************************************************')
                    else:
                        print('No se encontraron resultados.')
                if not veterinario_encontrado:
                    print("No se encontró el veterinario proporcionado.")
                    return veterinario_encontrado
            except Exception as e:
                print(f'Error al buscar veterinario: {e}')
            finally:
                BaseDatos.desconectar()
        return False

    def buscar_veterinario_id(self, id_usuario=None):
        """
        Busca un veterinario por ID en la base de datos.
        Si no se proporciona un ID, solicita uno al usuario.
        Llama al procedimiento almacenado 'ObtenerVeterinarioPorID' y maneja posibles errores.
        """
        if id_usuario is None:
            self.set_id_usuario()
            id_usuario = self.get_id_usuario()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_veterinario = conexion.cursor()
                cursor_veterinario.callproc('ObtenerVeterinarioPorID', [id_usuario])
                
                veterinario_encontrado = False
                print('Búsqueda de veterinario completada.')
                for result in cursor_veterinario.stored_results():
                    fila = result.fetchone()
                    if fila:
                        veterinario_encontrado = True
                        while fila is not None:
                            print('Resultado:')
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                            f"| Id propietario    : {fila[0]:<20}   | Nombre           : {fila[1]:<20}  \n" +
                            f"| Apellido          : {fila[2]:<20}   | Ciudad           : {fila[3]:<20}  \n" +
                            f"| Dirección         : {fila[4]:<20}   | Teléfono         : {fila[5]:<20}  \n" +
                            f"| Es propietario    : {fila[6]:<20}   | Es veterinario   : {fila[7]:<20}  \n" +
                            f"| Es administrador  : {fila[8]:<20}   | Email            : {fila[9]:<20}  \n" +
                            f"| Especialidad      : {fila[11]:<20}\n"+
                            f"| Horario           : {fila[12]:<20}"
                            '\033[0;m')
                            print('**********************************************************************************************')
                            return fila
                if not veterinario_encontrado:
                    print('El código de veterinario proporcionado no existe.')
            except Exception as e:
                print(f'Error al buscar veterinario: {e}')
            finally:
                BaseDatos.desconectar()
            return None
    
    def buscar_veterinario_nombre(self, nombre=None):
        """
        Busca veterinarios por nombre en la base de datos.
        Si no se proporciona un nombre, solicita uno al usuario.
        Llama al procedimiento almacenado 'ObtenerVeterinarioPorNombre' y maneja posibles errores.
        """
        if nombre is None:
            self.set_nombre()
            nombre = self.get_nombre()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_veterinario = conexion.cursor()
                cursor_veterinario.callproc('ObtenerVeterinarioPorNombre', [nombre])
                print('Búsqueda de veterinario completada.')
                veterinario_encontrado = False
                for result in cursor_veterinario.stored_results():
                    filas = result.fetchall()
                    if filas:
                        veterinario_encontrado = True
                        for datos in filas:
                            print('Resultado:')
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                            f"| Id propietario    : {datos[0]:<20}   | Nombre           : {datos[1]:<20}  \n" +
                            f"| Apellido          : {datos[2]:<20}   | Ciudad           : {datos[3]:<20}  \n" +
                            f"| Dirección         : {datos[4]:<20}   | Teléfono         : {datos[5]:<20}  \n" +
                            f"| Es propietario    : {datos[6]:<20}   | Es veterinario   : {datos[7]:<20}  \n" +
                            f"| Es administrador  : {datos[8]:<20}   | Email            : {datos[9]:<20}  \n" +
                            f"| Especialidad      : {datos[11]:<20}\n"+
                            f"| Horario           : {datos[12]:<20}"
                            '\033[0;m')
                            print('**********************************************************************************************')
                    else:
                        print('No se encontraron resultados.')
                if not veterinario_encontrado:
                    print("No se encontró el veterinario proporcionado.")
            except Exception as e:
                print(f'Error al buscar veterinario: {e}')
            finally:
                BaseDatos.desconectar()
        return None
            
    def actualizar_veterinario(self, id_usuario):
        """
        Actualiza los datos de un veterinario en la base de datos.
        Primero verifica si el veterinario existe, luego solicita los nuevos datos y actualiza la información.
        Llama al procedimiento almacenado 'ActualizarVeterinario' y maneja posibles errores.
        """
        propietario_encontrado = self.buscar_veterinario_id(id_usuario)
        if propietario_encontrado:
            print('Escriba los nuevos datos del veterinario:')
            print('------------------------------------------')
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
            self.set_especialidad()  
            self.set_horario()
            
            nuevo_nombre = self.get_nombre()
            nuevo_apellido = self.get_apellido()
            nueva_ciudad = self.get_ciudad()
            nueva_direccion = self.get_direccion()
            nuevo_telefono = self.get_telefono()
            nuevo_es_propietario = self.get_es_propietario()
            nuevo_es_veterinario = self.get_es_veterinario()
            nuevo_es_administrador = self.get_es_administrador()
            nuevo_email = self.get_email()
            nuevo_contraseña = self.get_contraseña()
            nuevo_especialidad = self.get_especialidad()
            nuevo_horario = self.get_horario()
            
            print('\nDatos del veterinario actualizados:')
            print('------------------------------------------')
            print(f'Id propietario: {id_usuario}')
            print(f'Nuevo nombre: {nuevo_nombre}')
            print(f'Nuevo apellido: {nuevo_apellido}')
            print(f'Nueva ciudad: {nueva_ciudad}')
            print(f'Nueva dirección: {nueva_direccion}')
            print(f'Nuevo teléfono: {nuevo_telefono}')
            print(f'Nuevo es propietario: {nuevo_es_propietario}')
            print(f'Nuevo es veterinario: {nuevo_es_veterinario}') 
            print(f'Nuevo es administrador: {nuevo_es_administrador}')
            print(f'Nuevo email: {nuevo_email}')
            print(f'Nueva contraseña: {nuevo_contraseña}')
            print(f'Nueva especialidad: {nuevo_especialidad}')
            print(f'Nuevo horario: {nuevo_horario}')

            conexion = BaseDatos.conectar()
            if conexion:
                try:
                    cursor_propietario = conexion.cursor()
                    cursor_propietario.callproc('ActualizarVeterinario', [
                        id_usuario,
                        nuevo_nombre,
                        nuevo_apellido,
                        nueva_ciudad,
                        nueva_direccion,
                        nuevo_telefono,
                        nuevo_es_propietario,
                        nuevo_es_veterinario,
                        nuevo_es_administrador,
                        nuevo_email,
                        nuevo_contraseña,
                        nuevo_especialidad,
                        nuevo_horario
                    ])
                    conexion.commit()
                    cursor_propietario.close()
                    print('Veterinario actualizado')
                except Exception as error:
                    print(f'Error al actualizar el veterinario: {error}. Intente de nuevo')
                finally:
                    BaseDatos.desconectar()
        else:
            print('Veterinario no encontrado. Intente otra vez')
    
    def eliminar_veterinario(self, id_usuario):
        """
        Elimina un veterinario de la base de datos.
        Llama al procedimiento almacenado 'EliminarVeterinario' y maneja posibles errores.
        """
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('EliminarVeterinario', [id_usuario])
                conexion.commit()
                print('Veterinario borrado correctamente...')
            except Exception as e:
                print(f'Error al eliminar Veterinario: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()

    