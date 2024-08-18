from conexion10 import BaseDatos
from usuario import Usuario

class Propietario(Usuario):
    def __init__(self, barrio: str = None, **kwargs):
        super().__init__(**kwargs)
        self.__barrio = barrio

    def get_barrio(self):
        return self.__barrio

    def set_barrio(self):
        while True:
            try:
                barrio = input('Barrio del propietario: ')
                if len(barrio) > 3:
                    self.__barrio = barrio
                    break
                else:
                    print('Barrio incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def capturar_datos(self):
        super().capturar_datos()  
        self.set_barrio()

    def registrar_propietarios(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('InsertarPropietario', [
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
                    self.get_barrio()
                ])
                conexion.commit()
                print('Propietario registrado correctamente...')
            except Exception as e:
                print(f'Error al registrar el propietario: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
                
    def consultar_propietarios(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_propietario = conexion.cursor()
                cursor_propietario.callproc('MostrarTodosPropietarios')  # Asumiendo que tienes un procedimiento para mostrar todas las mascotas
                print('Listado de todas los propietarios completado.')
                
                propietario_encontrado = False
                for result in cursor_propietario.stored_results():
                    filas = result.fetchall()
                    if filas:
                        propietario_encontrado = True
                        for datos in filas:
                            print('Resultado:')
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                f"| Id propietario  : {datos[0]:<20}  | Nombre           : {datos[1]}  \n" +
                                f"| Apellido        : {datos[2]:<20}  | Ciudad           : {datos[3]}  \n" +
                                f"| Dirección       : {datos[4]:<20}  | Teléfono         : {datos[5]}  \n" +
                                f"| Es propietario  : {datos[6]:<20}  | Es veterinario   : {datos[7]}  \n" +
                                f"| Es administrador: {datos[8]:<20}  | Email            : {datos[9]}  \n" +
                                f"| Contraseña      : {datos[10]:<20}  | Barrio           : {datos[11]} "
                                '\033[0;m')
                            print('**********************************************************************************************')
                    else:
                        print('No se encontraron resultados.')
                if not propietario_encontrado:
                    print("No se encontró el propietario proporcionado.")
            except Exception as e:
                print(f'Error al buscar el propietario: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    def buscar_propietario_id(self, id_usuario=None):
        if id_usuario is None:
            self.set_id_usuario()
            id_usuario = self.get_id_usuario()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_propietario = conexion.cursor()
                cursor_propietario.callproc('ObtenerPropietarioPorID', [id_usuario])
                print('Búsqueda de propietario completada.')
                for result in cursor_propietario.stored_results():
                    f = result.fetchone()
                    while f is not None:
                        print('Resultado:')
                        print('**********************************************************************************************')
                        print("\033[;36m" +
                                f"| Id propietario  : {f[0]:<20}  | Nombre           : {f[1]}  \n" +
                                f"| Apellido        : {f[2]:<20}  | Ciudad           : {f[3]}  \n" +
                                f"| Dirección       : {f[4]:<20}  | Teléfono         : {f[5]}  \n" +
                                f"| Es propietario  : {f[6]:<20}  | Es veterinario   : {f[7]}  \n" +
                                f"| Es administrador: {f[8]:<20}  | Email            : {f[9]}  \n" +
                                f"| Contraseña      : {f[10]:<20}  | Barrio           : {f[11]} "
                                '\033[0;m')
                        print('**********************************************************************************************')
                        return f
                    f = result.fetchall()
            except Exception as e:
                print(f'Error al buscar propietario: {e}')
            finally:
                BaseDatos.desconectar()
            return None
    
    def buscar_propietario_nombre(self, nombre=None):
        if nombre is None:
            self.set_nombre()
            nombre = self.get_nombre()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_propietario = conexion.cursor()
                cursor_propietario.callproc('ObtenerPropietarioPorNombre', [nombre])
                print('Búsqueda de propietario completada.')
                propietario_encontrado = False
                for result in cursor_propietario.stored_results():
                    filas = result.fetchall()
                    if filas:
                        propietario_encontrado = True
                        for datos in filas:
                            print('Resultado:')
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                f"| Id propietario  : {datos[0]:<20}  | Nombre           : {datos[1]}  \n" +
                                f"| Apellido        : {datos[2]:<20}  | Ciudad           : {datos[3]}  \n" +
                                f"| Dirección       : {datos[4]:<20}  | Teléfono         : {datos[5]}  \n" +
                                f"| Es propietario  : {datos[6]:<20}  | Es veterinario   : {datos[7]}  \n" +
                                f"| Es administrador: {datos[8]:<20}  | Email            : {datos[9]}  \n" +
                                f"| Contraseña      : {datos[10]:<20}  | Barrio           : {datos[11]} "
                                '\033[0;m')
                            print('**********************************************************************************************')
                    else:
                        print('No se encontraron resultados.')
                if not propietario_encontrado:
                    print("No se encontró el propietario proporcionado.")
            except Exception as e:
                print(f'Error al buscar el propietario: {e}')
            finally:
                BaseDatos.desconectar()
        return None
            
    def actualizar_propietario(self,id_usuario):
        propietario_encontrado = self.buscar_propietario_id(id_usuario)
        if propietario_encontrado:
            print('Escriba los nuevos datos del propietario:')
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
            nuevo_barrio = self.get_barrio()
            
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
            print(f'Nuevo barrio: {nuevo_barrio}')

            conexion = BaseDatos.conectar()
            if conexion:
                try:
                    cursor_propietario = conexion.cursor()
                    cursor_propietario.callproc('ActualizarPropietario', [
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
                        nuevo_barrio
                    ])
                    conexion.commit()
                    cursor_propietario.close()
                    print('Propietario actualizado')
                except Exception as error:
                    print(f'Error al actualizar el propietario: {error}. Intente de nuevo')
                finally:
                    BaseDatos.desconectar()
        else:
            print('Propietario no encontrado. Intente otra vez')
    
    def eliminar_propietario(self, id_usuario):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('EliminarPropietario', [id_usuario])
                conexion.commit()
                print('Propietario borrado correctamente...')
            except Exception as e:
                print(f'Error al eliminar propietario: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()       

    