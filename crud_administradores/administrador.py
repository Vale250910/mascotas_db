import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import datetime
from base_datos.conexion10 import BaseDatos  # Importa la clase de conexión a la base de datos
from crud_usuarios.usuario import Usuario  # Importa la clase base Usuario

class Administrador(Usuario):
    def __init__(self, cargo: str = None, fecha_ingreso: datetime.datetime = None, **kwargs):
        super().__init__(**kwargs)
        self.__cargo = cargo  # Atributo privado para almacenar el cargo del administrador
        self.__fecha_ingreso = fecha_ingreso  # Atributo privado para almacenar la fecha de ingreso

    # Método para obtener el cargo del administrador
    def get_cargo(self):
        return self.__cargo

    # Método para establecer el cargo del administrador con validación
    def set_cargo(self):
        while True:
            try:
                cargo = input('Cargo del administrador: ')
                if len(cargo) > 3:  # Validación para asegurar que el cargo tenga más de 3 caracteres
                    self.__cargo = cargo
                    break
                else:
                    print('Cargo incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    # Método para obtener la fecha de ingreso del administrador
    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    # Método para establecer la fecha de ingreso del administrador con validación
    def set_fecha_ingreso(self):
        while True:
            try:
                fecha = input('Escriba la fecha de ingreso (YYYY-MM-DD): ')
                fecha_historial = datetime.datetime.strptime(fecha, "%Y-%m-%d")  # Convierte la cadena de fecha en un objeto datetime
                self.__fecha_ingreso = fecha_historial
                break  # Salir del bucle si la fecha es válida
            except ValueError:
                print('Formato de fecha inválido. Intente nuevamente.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    # Método para capturar todos los datos del administrador
    def capturar_datos(self):
        super().capturar_datos()  # Llama al método de captura de datos de la clase base
        self.set_cargo()
        self.set_fecha_ingreso()

    # Método para registrar un nuevo administrador en la base de datos
    def registrar_administradores(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_administrador = conexion.cursor()
                cursor_administrador.callproc('InsertarAdministrador', [
                    self.get_tipo_documento(),
                    self.get_n_documento(),  
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
                    self.get_cargo(),
                    self.get_fecha_ingreso(),
                    
                ])
                conexion.commit()  # Confirma los cambios en la base de datos
                print('Administrador registrado correctamente...')
                
                # Muestra los datos registrados del administrador
                print('\nDatos del administrador registrados:')
                print('------------------------------------------')
                print(f'Tipo Documento:{self.get_tipo_documento()}')
                print(f'Numero Documento: {self.get_n_documento()}')
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
                print(f'Estado Acceso: {self.get_estado_acceso()}')
                print(f'Cargo: {self.get_cargo()}')
                print(f'Fecha de ingreso: {self.get_fecha_ingreso()}')
                
            except Exception as e:
                print(f'Error al registrar el administrador: {e}')
                conexion.rollback()  # Revertir los cambios en caso de error
            finally:
                BaseDatos.desconectar()
                
    # Método para consultar todos los administradores registrados en la base de datos
    def consultar_administradores(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_administrador = conexion.cursor()
                cursor_administrador.callproc('MostrarTodosAdministradores')  # Llama al procedimiento almacenado
                print('Listado de todos los administradores completado.')
                administrador_encontrado = False
                for result in cursor_administrador.stored_results():
                    filas = result.fetchall()
                    if filas:
                        administrador_encontrado = True
                        for datos in filas:
                            print('Resultado:')
                            fecha_ingreso = datos[14] if isinstance(datos[14], datetime.date) else str(datos[14])
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                f"| Tipo Documento     : {datos[0]:<20} \n"+
                                f"| N.Documento       : {datos[1]:<20}   | Nombre           : {datos[2]:<20}  \n" +
                                f"| Apellido          : {datos[3]:<20}   | Ciudad           : {datos[4]:<20}  \n" +
                                f"| Dirección         : {datos[5]:<20}   | Teléfono         : {datos[6]:<20}  \n" +
                                f"| Es propietario    : {datos[7]:<20}   | Es veterinario   : {datos[8]:<20}  \n" +
                                f"| Es administrador  : {datos[9]:<20}   | Email            : {datos[10]:<20}  \n" +
                                f"| Estado Acceso     : {datos[12]:<20}  | Cargo            : {datos[13]:<20}  \n"+
                                f"| Fecha Ingreso     : {fecha_ingreso}"
                                '\033[0;m')
                            print('**********************************************************************************************')
                if not administrador_encontrado:
                    print("No se encontró el administrador proporcionado no existe o esta inactivo.")
            except Exception as e:
                print(f'Error al buscar administrador: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    # Método para buscar un administrador por su ID en la base de datos
    def buscar_administrador_id(self, n_documento=None):
        if n_documento is None:
            self.set_n_documento()  # Captura el ID del usuario si no se proporciona
            n_documento = self.get_n_documento()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_administrador = conexion.cursor()
                cursor_administrador.callproc('ObtenerAdministradorPorID', [n_documento])
                administrador_encontrado = False
                print('Búsqueda de administrador completada.')
                for result in cursor_administrador.stored_results():
                    fila = result.fetchone()
                    if fila:
                        administrador_encontrado = True
                        while fila is not None:
                            print('Resultado:')
                            fecha_ingreso = fila[14] if isinstance(fila[14], datetime.date) else str(fila[14])
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                f"| Tipo Documento    : {fila[0]:<20} \n"+
                                f"| N.Documento       : {fila[1]:<20}   | Nombre           : {fila[2]:<20}  \n" +
                                f"| Apellido          : {fila[3]:<20}   | Ciudad           : {fila[4]:<20}  \n" +
                                f"| Dirección         : {fila[5]:<20}   | Teléfono         : {fila[6]:<20}  \n" +
                                f"| Es propietario    : {fila[7]:<20}   | Es veterinario   : {fila[8]:<20}  \n" +
                                f"| Es administrador  : {fila[9]:<20}   | Email            : {fila[10]:<20}  \n" +
                                f"| Estado Acceso     : {fila[12]:<20}   | Cargo            : {fila[13]:<20}  \n"+
                                f"| Fecha Ingreso     : {fecha_ingreso}"
                            '\033[0;m')
                            print('**********************************************************************************************')
                            return fila
                if not administrador_encontrado:
                    print('El código de administrador proporcionado no existe o esta inactivo.')
            except Exception as e:
                print(f'Error al buscar administrador: {e}')
            finally:
                BaseDatos.desconectar()
            return None
    
    # Método para buscar un administrador por su nombre en la base de datos
    def buscar_administrador_nombre(self, nombre):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_administrador = conexion.cursor()
                cursor_administrador.callproc('ObtenerAdministradorPorNombre', [nombre]) 
                print('Búsqueda del administrador completada.')

                administrador_encontrado = False
                for result in cursor_administrador.stored_results():
                    filas = result.fetchall()
                    if filas:
                        administrador_encontrado = True
                        for datos in filas:
                            print('Resultado:')
                            fecha_ingreso = datos[14] if isinstance(datos[14], datetime.date) else str(datos[14])
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                f"| Tipo Documento     : {datos[0]:<20} \n"+
                                f"| N.Documento       : {datos[1]:<20}   | Nombre           : {datos[2]:<20}  \n" +
                                f"| Apellido          : {datos[3]:<20}   | Ciudad           : {datos[4]:<20}  \n" +
                                f"| Dirección         : {datos[5]:<20}   | Teléfono         : {datos[6]:<20}  \n" +
                                f"| Es propietario    : {datos[7]:<20}   | Es veterinario   : {datos[8]:<20}  \n" +
                                f"| Es administrador  : {datos[9]:<20}   | Email            : {datos[10]:<20}  \n" +
                                f"| Estado Acceso     : {datos[12]:<20}   | Cargo            : {datos[13]:<20}  \n"+
                                f"| Fecha Ingreso     : {fecha_ingreso}\n"+
                                '\033[0;m')
                            print('**********************************************************************************************')
                if not administrador_encontrado:
                    print('El nombre del administrador proporcionado no existe o esta inactivo.')
            except Exception as e:
                print(f'Error al buscar administrador: {e}')
            finally:
                BaseDatos.desconectar()
        return None
    
    def actualizar_estado_administrador(self, n_documento=None, nuevo_estado_acceso=None):
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
                print(f'Estado de acceso actualizado a {nuevo_estado_acceso} para el administrador con documento {n_documento}.')
            except Exception as e:
                print(f'Error al actualizar el estado: {e}')
            finally:
                BaseDatos.desconectar()  
        else:
            print('No se pudo establecer la conexión con la base de datos.')
    
    def actualizar_administrador(self,n_documento):
        administrador_encontrado = self.buscar_administrador_id(n_documento)
        if administrador_encontrado:
            print('Escriba los nuevos datos del administrador:')
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
            self.set_cargo()  
            self.set_fecha_ingreso()
            
            nuevo_tipo_documento= self.get_tipo_documento()
            nuevo_nombre = self.get_nombre()
            nuevo_apellido = self.get_apellido()  # Fixed variable name to 'nuevo_apellido'
            nueva_ciudad = self.get_ciudad()
            nueva_direccion = self.get_direccion()
            nuevo_telefono = self.get_telefono()
            nuevo_es_propietario = self.get_es_propietario()  # Fixed variable name to 'nuevo_es_propietario'
            nuevo_es_veterinario = self.get_es_veterinario()  # Fixed variable name to 'nuevo_es_veterinario'
            nuevo_es_administrador = self.get_es_administrador()  # Fixed variable name to 'nuevo_es_administrador'
            nuevo_email = self.get_email()
            nuevo_contraseña = self.get_contraseña()
            nuevo_cargo = self.get_cargo()
            nuevo_fecha_ingreso = self.get_fecha_ingreso()
            
            print('\n Datos del administrador actualizados:')
            print('------------------------------------------')
            print(f'Nuevo Tipo de Documento:{nuevo_tipo_documento}')
            print(f'Numero de documento: {n_documento}')
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
            print(f'Nueva cargo: {nuevo_cargo}')
            print(f'Nueva fecha ingreso: {nuevo_fecha_ingreso}')

            conexion = BaseDatos.conectar()
            if conexion:
                try:
                    cursor_administrador = conexion.cursor()
                    cursor_administrador.callproc('ActualizarAdministrador', [
                        nuevo_tipo_documento,
                        n_documento,
                        nuevo_nombre,
                        nuevo_apellido,  # Ensure correct variable is passed
                        nueva_ciudad,
                        nueva_direccion,
                        nuevo_telefono,
                        nuevo_es_propietario,  # Ensure correct variable is passed
                        nuevo_es_veterinario,  # Ensure correct variable is passed
                        nuevo_es_administrador,  # Ensure correct variable is passed
                        nuevo_email,
                        nuevo_contraseña,
                        nuevo_cargo,
                        nuevo_fecha_ingreso
                    ])
                    conexion.commit()
                    cursor_administrador.close()
                    print('Administrador actualizado')
                except Exception as error:
                    print(f'Error al actualizar el administrador: {error}. Intente de nuevo')
                finally:
                    BaseDatos.desconectar()
        else:
            print('Administrador no encontrado.Asegúrese de que el código ingresado sea correcto o que el administrador esté activo. Intente nuevamente.')
    
    def eliminar_administrador(self,n_documento):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_administrador = conexion.cursor()
                cursor_administrador.callproc('EliminarUsuario', [n_documento])
                conexion.commit()
                print('Administrador borrado correctamente...')
            except Exception as e:
                print(f'Error al eliminar administrador: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar() 
