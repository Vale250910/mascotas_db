import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos.conexion10 import BaseDatos
from crud_usuarios.usuario import Usuario
import datetime

class Administrador(Usuario):
    def __init__(self, cargo: str = None,fecha_ingreso: datetime.datetime = None, **kwargs):
        super().__init__(**kwargs)
        self.__cargo = cargo
        self.__fecha_ingreso = fecha_ingreso

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self):
        while True:
            try:
                cargo = input('Cargo  del administrador: ')
                if len(cargo) > 3:
                    self.__cargo= cargo
                    break
                else:
                    print('Cargo incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
    
    def get_fecha_ingreso(self):
        return self.__fecha_ingreso
    
    def set_fecha_ingreso(self):
        while True:
            try:
                fecha = input('Escriba la fecha de ingreso (YYYY-MM-DD): ')
                fecha_historial = datetime.datetime.strptime(fecha, "%Y-%m-%d")
                self.__fecha_ingreso = fecha_historial
                break  # Salir del bucle si la fecha es válida
            except ValueError:
                print('Formato de fecha inválido. Intente nuevamente.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def capturar_datos(self):
        super().capturar_datos()  
        self.set_cargo()
        self.set_fecha_ingreso()
        

    def registrar_administradores(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_administrador = conexion.cursor()
                cursor_administrador.callproc('InsertarAdministrador', [
                    self.get_id_usuario(),  # Use getter methods for private attributes
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
                    self.get_cargo(),
                    self.get_fecha_ingreso()
                ])
                conexion.commit()
                print('Administrador registrado correctamente...')
                
                print('\nDatos del administrador registrados:')
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
                print(f'Cargo: {self.get_cargo()}')
                print(f'Fecha de ingreso: {self.get_fecha_ingreso()}')
                
            except Exception as e:
                print(f'Error al registrar el administrador: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
                
    def consultar_administradores(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_administrador = conexion.cursor()
                cursor_administrador.callproc('MostrarTodosAdministradores')  # Asumiendo que tienes un procedimiento para mostrar todas las mascotas
                print('Listado de todas los administradores completado.')
                administrador_encontrado = False
                for result in cursor_administrador.stored_results():
                    filas = result.fetchall()
                    if filas:
                        administrador_encontrado = True
                        for datos in filas:
                            print('Resultado:')
                            fecha_ingreso = datos[11] if isinstance(datos[11], datetime.date) else str(datos[11])
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                f"| Id propietario    : {datos[0]:<20}   | Nombre           : {datos[1]:<20}  \n" +
                                f"| Apellido          : {datos[2]:<20}   | Ciudad           : {datos[3]:<20}  \n" +
                                f"| Dirección         : {datos[4]:<20}   | Teléfono         : {datos[5]:<20}  \n" +
                                f"| Es propietario    : {datos[6]:<20}   | Es veterinario   : {datos[7]:<20}  \n" +
                                f"| Es administrador  : {datos[8]:<20}   | Email            : {datos[9]:<20}  \n" +
                                f"| Cargo           : {datos[10]:<20}     | Fecha ingreso   : {fecha_ingreso}  \n"+
                                '\033[0;m')
                            print('**********************************************************************************************')
                if not administrador_encontrado:
                    print("No se encontró el administrador proporcionado.")
            except Exception as e:
                print(f'Error al buscar administrador: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    def buscar_administrador_id(self, id_usuario=None):
        if id_usuario is None:
            self.set_id_usuario()
            id_usuario = self.get_id_usuario()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_administrador = conexion.cursor()
                cursor_administrador.callproc('ObtenerAdministradorPorID', [id_usuario])
                
                administrador_encontrado = False
                print('Búsqueda de administrador completada.')
                for result in cursor_administrador.stored_results():
                    fila = result.fetchone()
                    if fila:
                        administrador_encontrado = True
                        while fila is not None:
                            print('Resultado:')
                            fecha_ingreso = fila[11] if isinstance(fila[11], datetime.date) else str(fila[11])
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                            f"| Id propietario    : {fila[0]:<20}   | Nombre           : {fila[1]:<20}  \n" +
                            f"| Apellido          : {fila[2]:<20}   | Ciudad           : {fila[3]:<20}  \n" +
                            f"| Dirección         : {fila[4]:<20}   | Teléfono         : {fila[5]:<20}  \n" +
                            f"| Es propietario    : {fila[6]:<20}   | Es veterinario   : {fila[7]:<20}  \n" +
                            f"| Es administrador  : {fila[8]:<20}   | Email            : {fila[9]:<20}  \n" +
                            f"| Cargo             : {fila[10]:<20}   | Fecha ingreso    : {fecha_ingreso}\n"+
                            f""
                            '\033[0;m')
                            print('**********************************************************************************************')
                            return fila
                if not  administrador_encontrado:
                    print('El código de administrador proporcionado no existe.')
            except Exception as e:
                print(f'Error al buscar administrador: {e}')
            finally:
                BaseDatos.desconectar()
            return None
    
    def buscar_administrador_nombre(self, nombre):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_administrador = conexion.cursor()
                cursor_administrador.callproc('ObtenerAdministradorPorNombre', [nombre]) 
                print('Búsqueda del administrador completado.')

                administrador_encontrado = False
                for result in cursor_administrador.stored_results():
                    filas = result.fetchall()
                    if filas:
                        administrador_encontrado = True
                        for datos in filas:
                            print('Resultado:')
                            fecha_ingreso = datos[11] if isinstance(datos[11], datetime.date) else str(datos[11])
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                f"| Id propietario    : {datos[0]:<20}   | Nombre           : {datos[1]:<20}  \n" +
                                f"| Apellido          : {datos[2]:<20}   | Ciudad           : {datos[3]:<20}  \n" +
                                f"| Dirección         : {datos[4]:<20}   | Teléfono         : {datos[5]:<20}  \n" +
                                f"| Es propietario    : {datos[6]:<20}   | Es veterinario   : {datos[7]:<20}  \n" +
                                f"| Es administrador  : {datos[8]:<20}   | Email            : {datos[9]:<20}  \n" +
                                f"| Cargo           : {datos[10]:<20}     | Fecha ingreso   : {fecha_ingreso}  \n"+
                                '\033[0;m')
                            print('**********************************************************************************************')
                if not administrador_encontrado:
                    print("No se encontró el administrador proporcionado.")
            except Exception as e:
                print(f'Error al buscar administrador: {e}')
            finally:
                BaseDatos.desconectar()
        return None
    
    def actualizar_administrador(self,id_usuario):
        administrador_encontrado = self.buscar_administrador_id(id_usuario)
        if administrador_encontrado:
            print('Escriba los nuevos datos del administrador:')
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
            self.set_cargo()  
            self.set_fecha_ingreso()
            
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
            print(f'Nueva cargo: {nuevo_cargo}')
            print(f'Nueva fecha ingreso: {nuevo_fecha_ingreso}')

            conexion = BaseDatos.conectar()
            if conexion:
                try:
                    cursor_administrador = conexion.cursor()
                    cursor_administrador.callproc('ActualizarAdministrador', [
                        id_usuario,
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
            print('Administrador no encontrado. Intente otra vez')
    
    def eliminar_administrador(self, id_usuario):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_administrador = conexion.cursor()
                cursor_administrador.callproc('EliminarAdministrador', [id_usuario])
                conexion.commit()
                print('Administrador borrado correctamente...')
            except Exception as e:
                print(f'Error al eliminar administrador: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar() 