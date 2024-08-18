from conexion10 import BaseDatos
from usuario import Usuario
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
                fecha = input('Escriba la fecha del historial medico (YYYY-MM-DD): ')
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
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('InsertarAdministrador', [
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
            except Exception as e:
                print(f'Error al registrar el administrador: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
                
    def consultar_administradores(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_propietario = conexion.cursor()
                cursor_propietario.callproc('MostrarTodosAdministradores')  # Asumiendo que tienes un procedimiento para mostrar todas las mascotas
                print('Listado de todas los administradores completado.')

                for result in cursor_propietario.stored_results():
                    fila = result.fetchone()
                    if fila is not None:
                        print('Resultado:')
                        while fila is not None:
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                            f"| Id propietario    : {fila[0]:<20}   | Nombre           : {fila[1]:<20}  \n" +
                            f"| Apellido          : {fila[2]:<20}   | Ciudad           : {fila[3]:<20}  \n" +
                            f"| Dirección         : {fila[4]:<20}   | Teléfono         : {fila[5]:<20}  \n" +
                            f"| Es propietario    : {fila[6]:<20}   | Es veterinario   : {fila[7]:<20}  \n" +
                            f"| Es administrador  : {fila[8]:<20}   | Email            : {fila[9]:<20}  \n" +
                            f"| Contraseña        : {fila[10]:<20}   | Cargo           : {fila[11]:<20}\n"+
                            f"| Fecha ingreso     : {fila[12]}"
                            '\033[0;m')
                            print('**********************************************************************************************')
                            fila = result.fetchone()
                    else:
                        print('No se encontraron resultados.')
            except Exception as e:
                print(f'Error al mostrar los administradores: {e}')
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
                cursor_propietario = conexion.cursor()
                cursor_propietario.callproc('ObtenerAdministradorPorID', [id_usuario])
                print('Búsqueda de administrador completada.')
                for result in cursor_propietario.stored_results():
                    fila = result.fetchone()
                    while fila is not None:
                        print('Resultado:')
                        print('**********************************************************************************************')
                        print("\033[;36m" +
                        f"| Id propietario    : {fila[0]:<20}   | Nombre           : {fila[1]:<20}  \n" +
                        f"| Apellido          : {fila[2]:<20}   | Ciudad           : {fila[3]:<20}  \n" +
                        f"| Dirección         : {fila[4]:<20}   | Teléfono         : {fila[5]:<20}  \n" +
                        f"| Es propietario    : {fila[6]:<20}   | Es veterinario   : {fila[7]:<20}  \n" +
                        f"| Es administrador  : {fila[8]:<20}   | Email            : {fila[9]:<20}  \n" +
                        f"| Contraseña        : {fila[10]:<20}   | Cargo           : {fila[11]:<20}\n"+
                        f"| Fecha ingreso     : {fila[12]}"
                        '\033[0;m')
                        print('**********************************************************************************************')
                        return fila
                        fila = result.fetchall()
            except Exception as e:
                print(f'Error al buscar administrador: {e}')
            finally:
                BaseDatos.desconectar()
            return None
    
    def buscar_administrador_nombre(self, nombre=None):
        if nombre is None:
            self.set_nombre()
            nombre = self.get_nombre()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_propietario = conexion.cursor()
                cursor_propietario.callproc('ObtenerAdministradorPorNombre', [nombre])
                print('Búsqueda de administrador completada.')
                for result in cursor_propietario.stored_results():
                    fila = result.fetchone()
                    while fila is not None:
                        print('Resultado:')
                        print('**********************************************************************************************')
                        print("\033[;36m" +
                        f"| Id propietario    : {fila[0]:<20}   | Nombre           : {fila[1]:<20}  \n" +
                        f"| Apellido          : {fila[2]:<20}   | Ciudad           : {fila[3]:<20}  \n" +
                        f"| Dirección         : {fila[4]:<20}   | Teléfono         : {fila[5]:<20}  \n" +
                        f"| Es propietario    : {fila[6]:<20}   | Es veterinario   : {fila[7]:<20}  \n" +
                        f"| Es administrador  : {fila[8]:<20}   | Email            : {fila[9]:<20}  \n" +
                        f"| Contraseña        : {fila[10]:<20}   | Cargo           : {fila[11]:<20}\n"+
                        f"| Fecha ingreso     : {fila[12]}"
                        '\033[0;m')
                        print('**********************************************************************************************')
                        return fila
                    fila = result.fetchall()
            except Exception as e:
                print(f'Error al buscar administrador: {e}')
            finally:
                BaseDatos.desconectar()
            return None
            
    def actualizar_administrador(self,id_usuario):
        propietario_encontrado = self.buscar_administrador_id(id_usuario)
        if propietario_encontrado:
            print('Escriba los nuevos datos del administrador:')
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
                    cursor_propietario = conexion.cursor()
                    cursor_propietario.callproc('ActualizarAdministrador', [
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
                    cursor_propietario.close()
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
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('EliminarAdministrador', [id_usuario])
                conexion.commit()
                print('Administrador borrado correctamente...')
            except Exception as e:
                print(f'Error al eliminar administrador: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar() 