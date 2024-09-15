import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from base_datos.conexion10 import BaseDatos
import re

class Servicios:
    def __init__(
            self,
            codigo: int = None,
            nombre: str = None,
            descripcion: str = None,
            precio: float = None,
            ):
        # Inicializa los atributos del servicio
        self.__codigo = codigo
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio

    # GET y SET

    def get_codigo(self):
        # Devuelve el código del servicio
        return self.__codigo

    def get_nombre(self):
        # Devuelve el nombre del servicio
        return self.__nombre

    def set_nombre(self):
        # Establece el nombre del servicio después de validarlo
        while True:
            try:
                nombre = input('Tipo de servicio: ')
                if len(nombre) > 3:
                    self.__nombre = nombre
                    break
                else:
                    print('Tipo incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def get_descripcion(self):
        # Devuelve la descripción del servicio
        return self.__descripcion

    def set_descripcion(self):
        # Establece la descripción del servicio después de validarla
        while True:
            try:
                descripcion = input('Descripción del servicio: ')
                if 2 <= len(descripcion) <= 100:
                    self.__descripcion = descripcion
                    break
                else:
                    print('Datos incorrectos. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def get_precio(self):
        # Devuelve el precio del servicio
        return self.__precio

    def set_precio(self):
        # Establece el precio del servicio después de validarlo
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
        # Captura y establece todos los datos del servicio
        self.set_nombre()
        self.set_descripcion()
        self.set_precio()

    def registrar_servicio(self):
        # Registra un nuevo servicio en la base de datos
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                # Llama al procedimiento almacenado para insertar un servicio
                cursor_servicio.callproc('InsertarServicio', [
                    self.get_nombre(),
                    self.get_descripcion(),
                    self.get_precio(),
                ])
                conexion.commit()
                print('Servicio registrado correctamente...')
                print('\n Datos del servicio actualizados:')
                print('------------------------------------------')
                print(f'  Nombre: {self.get_nombre()}')
                print(f'  Descripción: {self.get_descripcion()}')
                print(f'  Precio: {self.get_precio()}')
            except Exception as e:
                print(f'Error al registrar servicio: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
    
    def mostrar_todas_los_servicios(self):
        # Muestra todos los servicios registrados en la base de datos
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                # Llama al procedimiento almacenado para obtener todos los servicios
                cursor_servicio.callproc('BuscarServicios')  
                print('Listado de todos los servicios completados.')

                servicio_encontrado = False
                for result in cursor_servicio.stored_results():
                    filas = result.fetchall()
                    if filas:
                        servicio_encontrado = True
                        for datos in filas:
                            print('Resultado:')
                            print('****************************************************************************************************')
                            print("\033[;36m" +
                                f"| {'Código':<15}: {datos[0]:<20} | {'Nombre':<15}: {datos[1]:<30}\n" +
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

    def buscar_servicio_por_codigo(self, codigo=None):
        # Busca un servicio por código en la base de datos
        if codigo is None:
            self.get_codigo()
            codigo = self.__codigo
        
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                # Llama al procedimiento almacenado para buscar un servicio por código
                cursor_servicio.callproc('BuscarServicioPorCodigo', [codigo])
                print('Búsqueda de servicio completada.')

                servicio_encontrado = False
                for result in cursor_servicio.stored_results():
                    fila = result.fetchone()
                    if fila:
                        servicio_encontrado = True
                        print('Resultado:')
                        print('****************************************************************************************************')
                        print("\033[;36m" +
                                f"| {'Código':<15}: {fila[0]:<20} | {'Nombre':<15}: {fila[1]:<30}\n" +
                                f"| {'Descripción':<15}: {fila[2]:<50}\n" +
                                f"| {'Precio':<15}: {fila[3]:<20}\n" +
                                '\033[0;m')
                        print('****************************************************************************************************')
                        break
                if not servicio_encontrado:
                    print("No se encontró el servicio con el código proporcionado.")
                return servicio_encontrado        
            except Exception as e:
                print(f'Error al buscar el servicio: {e}')
            finally:
                BaseDatos.desconectar()
        return False 

    def buscar_servicio_nombre(self, nombre_servicio):
        # Busca un servicio por nombre en la base de datos
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                # Llama al procedimiento almacenado para buscar un servicio por nombre
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
                                f"| {'Código':<15}: {datos[0]:<20} | {'Nombre':<15}: {datos[1]:<30}\n" +
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

    def actualizar_servicio(self, codigo):
        # Actualiza un servicio existente por su código
        producto_encontrado = self.buscar_servicio_por_codigo(codigo)
        if producto_encontrado:
            print('\nEscriba los nuevos datos del producto:')
            print('------------------------------------------')
            self.set_nombre()
            self.set_descripcion()
            self.set_precio()
        
            nuevo_nombre = self.get_nombre()
            nueva_descripcion = self.get_descripcion()
            nuevo_precio = self.get_precio()

            print('\n Datos del producto actualizados:')
            print('------------------------------------------')
            print(f'  Código: {codigo}')
            print(f'  Nuevo nombre: {nuevo_nombre}')
            print(f'  Nueva descripción: {nueva_descripcion}')
            print(f'  Nuevo precio: {nuevo_precio}')
            
            conexion = BaseDatos.conectar()
            if conexion:
                try:
                    cursor_producto = conexion.cursor()
                    # Llama al procedimiento almacenado para actualizar un servicio
                    cursor_producto.callproc('ActualizarServicios', [
                        codigo,
                        nuevo_nombre,
                        nueva_descripcion,
                        nuevo_precio
                    ])
                    conexion.commit()
                    cursor_producto.close()
                    print('Producto actualizado')
                except Exception as error:
                    print(f'Error al actualizar el servicio: {error}. Intente de nuevo')
                finally:
                    BaseDatos.desconectar()
        else:
            print('Servicio no encontrado. Intente otra vez')

    def eliminar_servicio(self, codigo_servicio):
        # Elimina un servicio por su código
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                # Llama al procedimiento almacenado para eliminar un servicio
                cursor_servicio.callproc('EliminarServicio', [codigo_servicio])
                conexion.commit()
                print('Servicio borrado correctamente...')
            except Exception as e:
                print(f'Error al eliminar el servicio: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
