from conexion10 import BaseDatos
from colorama import init, Fore, Back, Style
import re

init()

class Servicios:
    def init(
            self,
            codigo: int = None,
            nombre: str= None,
            descripcion: str= None,
            precio: float= None,
            ):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        

    # GET y SET

    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self):
        while True:
            try:
                codigo_servicio = int(input('Escriba el código del servicio: '))
                if (1 <= codigo_servicio <= 1000000000):
                    self.__codigo = codigo_servicio
                    break
                else:
                    print('El número debe estar entre 0 y 100000000')
            except ValueError:
                print('El código debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue
        
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self):
        while True:
            try:
                nombre = input('Tipo de servicio: ')
                if len(nombre)>3:
                    self.__nombre = nombre
                    break
                else:
                    print('Tipo incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self):
        while True:
            try:
                descripcion = input('descripcion del servicio (Baño, Corte de uñas , Desparasitacion...): ')
                if 2 <= len(descripcion) <= 100:
                    self.__descripcion = descripcion
                    break
                else:
                    print('Datos incorrectos. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def get_precio(self):
        return self.__precio

    def set_precio(self):
        while True:
            try:
                precio = float(input("Ingrese el precio en COP (entre 0 y 50,000,000): "))
                if 0 <= precio <= 50000000:
                    self.__precio = precio
                    print(f"Precio establecido correctamente: {self.__precio} COP")
                    break
                else:
                    print("Ingrese un precio válido dentro del rango.")
            
            except ValueError:
                print("Entrada no válida. Ingrese un número.")
            
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                break    


    def capturar_datos(self):
        self.set_codigo()
        self.set_nombre()
        self.set_descripcion()
        self.set_precio()

    def registrar_servicio(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('InsertarServicio', [
                    self.__codigo,
                    self.__nombre,
                    self.__descripcion,
                    self.__precio,
                ])
                conexion.commit()
                print('Servicio registrado correctamente...')
            except Exception as e:
                print(f'Error al registrar servicio: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
    
    def mostrar_todas_los_servicios(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('BuscarServicios')  # Asumiendo que tienes un procedimiento para mostrar todas las mascotas
                print('Listado de todas los servicios completados.')

                cita_encontrada = False
                for result in cursor_servicio.stored_results():
                    filas = result.fetchall()
                    if filas:
                        cita_encontrada = True
                        for datos in filas:
                            print('Resultado:')
                            print('****************************************************************************************************')
                            print("\033[;36m" +
                                f"| {'Codigo':<15}: {datos[0]:<20} | {'Nombre':<15}: {datos[1]:<30}\n" +
                                f"| {'Descripción':<15}: {datos[2]:<50}\n" +
                                f"| {'Precio':<15}: {datos[3]:<20}\n" +
                                '\033[0;m')
                            print('****************************************************************************************************')


                if not cita_encontrada:
                    print("No se encontró el servicio proporcionado.")
            except Exception as e:
                print(f'Error al buscar servicio: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    
    def buscar_servicio_por_codigo(self, codigo_servicio=None):
        if codigo_servicio is None:
            self.set_codigo()
            codigo_servicio = self.__codigo
        
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('BuscarServicioPorCodigo', [codigo_servicio])
                print('Búsqueda de servicio completada.')
                
                for result in cursor_servicio.stored_results():
                    fila = result.fetchone()
                    while fila is not None:
                        print('Resultado:')
                        print('****************************************************************************************************')
                        print("\033[;36m" +
                            f"| {'Codigo':<15}: {fila[0]:<20} | {'Nombre':<15}: {fila[1]:<30}\n" +
                            f"| {'Descripción':<15}: {fila[2]:<50}\n" +
                            f"| {'Precio':<15}: {fila[3]:<20}\n" +
                            '\033[0;m')
                        print('****************************************************************************************************')

                        fila = result.fetchone()  
                        
            except Exception as e:
                print(f'Error al buscar el servicio: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    

    def buscar_servicio_nombre(self, nombre_servicio):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                # Llamar al procedimiento con el nombre del servicio
                cursor_servicio.callproc('BuscarServicioPorNombre', [nombre_servicio])  
                print('Búsqueda del servicio completada.')

                servicio_encontrado = False
                for result in cursor_servicio.stored_results():
                    filas = result.fetchall()
                    if filas:
                        servicio_encontrado = True
                        for datos in filas:
                            print('Resultado:')
                            print('****************************************************************************************************')
                            print("\033[;36m" +
                                f"| {'Codigo':<15}: {datos[0]:<20} | {'Nombre':<15}: {datos[1]:<30}\n" +
                                f"| {'Descripción':<15}: {datos[2]:<50}\n" +
                                f"| {'Precio':<15}: {datos[3]:<20}\n" +
                                '\033[0;m')
                            print('****************************************************************************************************')
                if not servicio_encontrado:
                    print("No se encontró el servicio proporcionado.")
            except Exception as e:
                print(f'Error al buscar servicio: {e}')
            finally:
                BaseDatos.desconectar()
        return None



    def eliminar_servicio(self, codigo_servicio):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('EliminarServicio', [codigo_servicio])
                conexion.commit()
                print('Servicio borrado correctamente...')
            except Exception as e:
                print(f'Error al eliminar el servicio: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()