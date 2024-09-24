import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos.conexion10 import BaseDatos
from crud_usuarios.usuario import Usuario

# La clase Propietario hereda de la clase Usuario
class Propietario(Usuario):
    def __init__(self, barrio: str = None, **kwargs):
        # Llama al constructor de la clase base Usuario
        super().__init__(**kwargs)
        self.__barrio = barrio  # Atributo privado para almacenar el barrio del propietario

    # Método getter para obtener el valor del atributo barrio
    def get_barrio(self):
        return self.__barrio

    # Método setter para asignar un valor al atributo barrio con validación
    def set_barrio(self):
        while True:
            try:
                barrio = input('Barrio del propietario: ')
                if len(barrio) > 3:  # Validación: el barrio debe tener más de 3 caracteres
                    self.__barrio = barrio
                    break
                else:
                    print('Barrio incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    # Método para capturar los datos del propietario, incluyendo los datos heredados y el barrio
    def capturar_datos(self):
        super().capturar_datos()  # Llama al método capturar_datos de la clase base Usuario
        self.set_barrio()  # Captura el barrio del propietario

    # Método para registrar un propietario en la base de datos
    def registrar_propietarios(self):
        self.capturar_datos()  # Captura todos los datos necesarios
        conexion = BaseDatos.conectar()  # Conecta a la base de datos
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                # Llama al procedimiento almacenado InsertarPropietario
                cursor_mascota.callproc('InsertarPropietario', [
                    self.get_tipo_documento(),  # Usar métodos getter para atributos privados
                    self.get_n_documento(),  # Usar métodos getter para atributos privados
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
                    self.get_estado_acceso(),
                    self.get_barrio(),
                    
                ])
                
                # Confirmar cambios en la base de datos
                conexion.commit()
                print('Propietario registrado correctamente...')
                
                # Imprimir los datos registrados
                print('\nDatos del propietario registrados:')
                print('------------------------------------------')
                print(f'Tipo Documento: {self.get_tipo_documento()}')
                print(f'N. Documento: {self.get_n_documento()}')
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
                print(f'Estado: {self.get_estado_acceso()}')
                print(f'Barrio: {self.get_barrio()}')
                
                
            except Exception as e:
                # En caso de error, se realiza un rollback para revertir la transacción
                print(f'Error al registrar el propietario: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()  # Desconecta de la base de datos

    # Método para consultar todos los propietarios en la base de datos
    def consultar_propietarios(self):
        conexion = BaseDatos.conectar()  # Conecta a la base de datos
        if conexion:
            try:
                cursor_propietario = conexion.cursor()
                # Llama al procedimiento almacenado MostrarTodosPropietarios
                cursor_propietario.callproc('MostrarTodosPropietarios')
                print('Listado de todos los propietarios completado.')
                
                propietario_encontrado = False
                # Itera sobre los resultados devueltos por el procedimiento almacenado
                for result in cursor_propietario.stored_results():
                    filas = result.fetchall()
                    if filas:
                        propietario_encontrado = True
                        for datos in filas:
                            # Imprime los detalles de cada propietario encontrado
                            print('Resultado:')
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                f"| Tipo Documento  : {datos[0]:<20} \n"+
                                f"| N. Documento    : {datos[1]:<20}  | Nombre           : {datos[2]}  \n" +
                                f"| Apellido        : {datos[3]:<20}  | Ciudad           : {datos[4]}  \n" +
                                f"| Dirección       : {datos[5]:<20}  | Teléfono         : {datos[6]}  \n" +
                                f"| Es propietario  : {datos[7]:<20}  | Es veterinario   : {datos[8]}  \n" +
                                f"| Es administrador: {datos[9]:<20}  | Email            : {datos[10]} \n" +
                                f"| Estado Acceso   : {datos[12]:<20}  | Barrio           : {datos[13]} \n" +
                                '\033[0;m')
                            print('**********************************************************************************************')
                    else:
                        print('No se encontraron resultados.')
                if not propietario_encontrado:
                    print("No se encontró el propietario proporcionado no existe o esta inactivo.")
            except Exception as e:
                print(f'Error al buscar el propietario: {e}')
            finally:
                BaseDatos.desconectar()  # Desconecta de la base de datos
        return None

    # Método para buscar un propietario por su ID
    def buscar_propietario_id(self, n_documento=None):
        if n_documento is None:
            self.set_n_documento()  # Si no se proporciona ID, se solicita
            n_documento = self.get_n_documento()
        conexion = BaseDatos.conectar()  # Conecta a la base de datos
        if conexion:
            try:
                cursor_propietario = conexion.cursor()
                # Llama al procedimiento almacenado ObtenerPropietarioPorID
                cursor_propietario.callproc('ObtenerPropietarioPorID', [n_documento])
                print('Búsqueda de propietario completada.')
                propietario_encontrado = False
                # Itera sobre los resultados devueltos por el procedimiento almacenado
                for result in cursor_propietario.stored_results():
                    fila = result.fetchone()
                    if fila:
                        propietario_encontrado = True
                        while fila is not None:
                            # Imprime los detalles del propietario encontrado
                            print('Resultado:')
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                    f"| Tipo Documento  : {fila[0]:<20} \n"+
                                    f"| N. Documento    : {fila[1]:<20}  | Nombre           : {fila[2]}  \n" +
                                    f"| Apellido        : {fila[3]:<20}  | Ciudad           : {fila[4]}  \n" +
                                    f"| Dirección       : {fila[5]:<20}  | Teléfono         : {fila[6]}  \n" +
                                    f"| Es propietario  : {fila[7]:<20}  | Es veterinario   : {fila[8]}  \n" +
                                    f"| Es administrador: {fila[9]:<20}  | Email            : {fila[10]} \n" +
                                    f"| Estado Acceso   : {fila[12]:<20}  | Barrio           : {fila[13]} \n" +
                                    '\033[0;m')
                            print('**********************************************************************************************')
                            return fila
                if not propietario_encontrado:
                    print("No se encontraron propietarios con el código proporcionado no existe o esta inactivo.")      
            except Exception as e:
                print(f'Error al buscar propietario: {e}')
            finally:
                BaseDatos.desconectar()  # Desconecta de la base de datos
            return None
    
    # Método para buscar un propietario por su nombre
    def buscar_propietario_nombre(self, nombre=None):
        if nombre is None:
            self.set_nombre()  # Si no se proporciona el nombre, se solicita
            nombre = self.get_nombre()
        conexion = BaseDatos.conectar()  # Conecta a la base de datos
        if conexion:
            try:
                cursor_propietario = conexion.cursor()
                # Llama al procedimiento almacenado ObtenerPropietarioPorNombre
                cursor_propietario.callproc('ObtenerPropietarioPorNombre', [nombre])
                print('Búsqueda de propietario completada.')
                propietario_encontrado = False
                # Itera sobre los resultados devueltos por el procedimiento almacenado
                for result in cursor_propietario.stored_results():
                    filas = result.fetchall()
                    if filas:
                        propietario_encontrado = True
                        for datos in filas:
                            # Imprime los detalles de cada propietario encontrado
                            print('Resultado:')
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                f"| Tipo Documento  : {datos[0]:<20} \n"+
                                f"| N. Documento    : {datos[1]:<20}  | Nombre           : {datos[2]}  \n" +
                                f"| Apellido        : {datos[3]:<20}  | Ciudad           : {datos[4]}  \n" +
                                f"| Dirección       : {datos[5]:<20}  | Teléfono         : {datos[6]}  \n" +
                                f"| Es propietario  : {datos[7]:<20}  | Es veterinario   : {datos[8]}  \n" +
                                f"| Es administrador: {datos[9]:<20}  | Email            : {datos[10]} \n" +
                                f"| Estado Acceso   : {datos[12]:<20}  | Barrio           : {datos[13]} \n" +
                                '\033[0;m')
                            print('**********************************************************************************************')
                    else:
                        print('No se encontraron resultados.')
                if not propietario_encontrado:
                    print("No se encontró el propietario proporcionado no existe o esta inactivo.") 
            except Exception as e:
                print(f'Error al buscar propietario: {e}')
            finally:
                BaseDatos.desconectar()  # Desconecta de la base de datos
        return None
    def actualizar_estado_propietario(self, n_documento=None, nuevo_estado_acceso=None):
        if n_documento is None:
            self.set_n_documento()  
            n_documento = self.get_n_documento()
            
        if nuevo_estado_acceso is None:
            self.set_estado_acceso()
            nuevo_estado_acceso = self.get_estado_acceso()  
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_propietario = conexion.cursor()  
                cursor_propietario.callproc('ActualizarEstadoUsuario', (n_documento, nuevo_estado_acceso))
                for result in cursor_propietario.stored_results():
                    filas = result.fetchall()
                    if filas:
                        for fila in filas:
                            print('**********************************************************************************************')
                            print(f'Documento: {fila[0]}, Nombre: {fila[1]}, Apellido: {fila[2]}, Estado: {fila[3]}')
                            print('**********************************************************************************************')
                    else:
                        print(f'No se encontraron resultados para el documento {n_documento}.')
                conexion.commit()
                print(f'Estado de acceso actualizado a {nuevo_estado_acceso} para el propietario con documento {n_documento}.')
            except Exception as e:
                print(f'Error al actualizar el estado: {e}')
            finally:
                BaseDatos.desconectar()  
        else:
            print('No se pudo establecer la conexión con la base de datos.')


    def actualizar_propietario(self, n_documento):
    # Buscar el propietario en la base de datos usando el ID del usuario
        propietario_encontrado = self.buscar_propietario_id(n_documento)
        
        if propietario_encontrado:
            # Solicitar y establecer nuevos datos del propietario
            print('Escriba los nuevos datos del propietario:')
            print('------------------------------------------')
            self.set_tipo_documento()
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
            self.set_barrio()
            
            
            # Obtener los nuevos datos del propietario
            nuevo_tipo_documento = self.get_tipo_documento()
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
            nuevo_barrio = self.get_barrio()
            
            # Mostrar los nuevos datos del propietario
            print('\n Datos de el propietario actualizados:')
            print('------------------------------------------')
            print(f'Tipo de documento:{nuevo_tipo_documento}')
            print(f'N. Documento: {n_documento}')
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
            print(f'Nuevo barrio: {nuevo_barrio}')

            # Conectar a la base de datos
            conexion = BaseDatos.conectar()
            if conexion:
                try:
                    # Llamar al procedimiento almacenado para actualizar el propietario
                    cursor_propietario = conexion.cursor()
                    cursor_propietario.callproc('ActualizarPropietario', [
                        nuevo_tipo_documento,
                        n_documento,
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
                        nuevo_barrio
                    ])
                    # Confirmar los cambios
                    conexion.commit()
                    cursor_propietario.close()
                    print('Propietario actualizado')
                except Exception as error:
                    # Manejo de errores en caso de fallos
                    print(f'Error al actualizar el propietario: {error}. Intente de nuevo')
                finally:
                    # Desconectar de la base de datos
                    BaseDatos.desconectar()
        else:
            # Mensaje en caso de no encontrar el propietario
            print('Propietario no encontrado. Asegúrese de que el código ingresado sea correcto o que el propietario esté activo. Intente nuevamente.')

    def eliminar_propietario(self, n_documento):
        # Conectar a la base de datos
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                # Llamar al procedimiento almacenado para eliminar el propietario
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('EliminarUsuario', [n_documento])
                # Confirmar los cambios
                conexion.commit()
                print('Propietario borrado correctamente...')
            except Exception as e:
                # Manejo de errores en caso de fallos
                print(f'Error al eliminar propietario: {e}')
                conexion.rollback()
            finally:
                # Desconectar de la base de datos
                BaseDatos.desconectar()
