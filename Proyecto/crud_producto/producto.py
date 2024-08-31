import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos.conexion10 import BaseDatos
from colorama import init, Fore, Back, Style
init()

class Productos:
    def __init__(self,
                codigo: int = None,
                nombre: str = None,
                descripcion: str = None,
                precio: float = None,
                stock: int = None):
        """
        Inicializa un objeto Producto con los atributos proporcionados.
        :param codigo: Código del producto.
        :param nombre: Nombre del producto.
        :param descripcion: Descripción del producto.
        :param precio: Precio del producto en COP.
        :param stock: Cantidad de stock del producto.
        """
        self.__codigo = codigo
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock

    # Métodos GET
    def get_codigo(self):
        """
        Retorna el código del producto.
        """
        return self.__codigo

    def get_nombre(self):
        """
        Retorna el nombre del producto.
        """
        return self.__nombre

    def get_descripcion(self):
        """
        Retorna la descripción del producto.
        """
        return self.__descripcion

    def get_precio(self):
        """
        Retorna el precio del producto.
        """
        return self.__precio

    def get_stock(self):
        """
        Retorna el stock del producto.
        """
        return self.__stock

    # Métodos SET
    def set_nombre(self):
        """
        Solicita al usuario que ingrese el nombre del producto y valida la entrada.
        """
        while True:
            try:
                nombre = input('Escriba el nombre del producto: ')
                if len(nombre) > 3:
                    self.__nombre = nombre
                    break
                else:
                    print('Nombre incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def set_descripcion(self):
        """
        Solicita al usuario que ingrese la descripción del producto y valida la entrada.
        """
        while True:
            try:
                descripcion = input('Escriba la descripcion del producto: ')
                if 2 <= len(descripcion) <= 100:
                    self.__descripcion = descripcion
                    break
                else:
                    print('Datos incorrectos. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def set_precio(self):
        """
        Solicita al usuario que ingrese el precio del producto y valida la entrada.
        """
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

    def set_stock(self):
        """
        Solicita al usuario que ingrese el stock del producto y valida la entrada.
        """
        while True:
            try:
                stock = int(input('Ingrese el stock de un producto: '))
                if 0 <= stock <= 1000000000:
                    self.__stock = stock
                    break
                else:
                    print('Stock no válido.')
            except ValueError:
                print('Solo se admiten números.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def capturar_datos(self):
        """
        Captura todos los datos necesarios para registrar un producto a través de las funciones de entrada.
        """
        self.set_nombre()
        self.set_descripcion()
        self.set_precio()
        self.set_stock()

    def registrar_producto(self):
        """
        Captura los datos del producto y guarda la información en la base de datos.
        """
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursorproducto = conexion.cursor()
                cursorproducto.callproc('InsertarProducto', [
                    self.get_nombre(), 
                    self.get_descripcion(),
                    self.get_precio(),
                    self.get_stock(),
                ])
                conexion.commit()
                print('Producto registrado correctamente...')
                print('\n Datos del producto registrados:')
                print('------------------------------------------')
                print(f'  Nombre: {self.get_nombre()}')
                print(f'  Descripción: {self.get_descripcion()}')
                print(f'  Precio: {self.get_precio()}')
                print(f'  Stock: {self.get_stock()}')
            except Exception as e:
                print(f'Error al registrar producto: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()

    def mostrar_todas_los_productos(self):
        """
        Muestra todos los productos almacenados en la base de datos.
        """
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursorproducto = conexion.cursor()
                cursorproducto.callproc('BuscarTodosLosProductos')  # Asumiendo que tienes un procedimiento para mostrar todos los productos
                print('Listado de todos los productos completado.')

                producto_encontrado = False
                for result in cursorproducto.stored_results():
                    filas = result.fetchall()
                    if filas:
                        producto_encontrado = True
                        for datos in filas:
                            print('Resultado:')
                            print('****************************************************************************************************')
                            print("\033[;36m" +
                                f"| {'Codigo':<15}: {datos[0]:<20} | {'Nombre':<15}: {datos[1]:<30}\n" +
                                f"| {'Descripción':<15}: {datos[2]:<50}\n" +
                                f"| {'Precio':<15}: {datos[3]:<20} | {'Stock':<15}: {datos[4]:<20}\n" +
                                '\033[0;m')
                            print('****************************************************************************************************')

                if not producto_encontrado:
                    print("No se encontraron productos.")
            except Exception as e:
                print(f'Error al buscar productos: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    def buscar_producto_por_codigo(self, codigo=None):
        """
        Busca un producto en la base de datos por su código.
        :param codigo: Código del producto a buscar. Si no se proporciona, utiliza el código de la instancia.
        :return: True si el producto se encuentra, False si no.
        """
        if codigo is None:
            self.get_codigo()
            codigo = self.__codigo

        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursorproducto = conexion.cursor()
                cursorproducto.callproc('BuscarProductoCodigo', [codigo])
                print('Búsqueda de productos completada.')
                
                producto_encontrado = False
                for result in cursorproducto.stored_results():
                    fila = result.fetchone()
                    if fila:
                        producto_encontrado = True
                        print('Resultado:')
                        print('****************************************************************************************************')
                        print("\033[;36m" +
                            f"| {'Codigo':<15}: {fila[0]:<20} | {'Nombre':<15}: {fila[1]:<30}\n" +
                            f"| {'Descripción':<15}: {fila[2]:<50}\n" +
                            f"| {'Precio':<15}: {fila[3]:<20} | {'Stock':<15}: {fila[4]:<20}\n" +
                            '\033[0;m')
                        print('****************************************************************************************************')
                        break

                if not producto_encontrado:
                    print('El código de producto proporcionado no existe.')
                
                return producto_encontrado  # Retorna True si se encontró un producto, False si no
            
            except Exception as e:
                print(f'Error al buscar el producto: {e}')
                return False
            finally:
                BaseDatos.desconectar()
    
        return False 

    def buscar_producto_nombre(self, nombre_producto):
        """
        Busca un producto en la base de datos por su nombre.
        :param nombre_producto: Nombre del producto a buscar.
        """
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursorproducto = conexion.cursor()
                cursorproducto.callproc('BuscarProductosPorNombre', [nombre_producto])
                print('Búsqueda del producto completada.')

                producto_encontrado = False
                for result in cursorproducto.stored_results():
                    filas = result.fetchall()
                    if filas:
                        producto_encontrado = True
                        for datos in filas:
                            print('Resultado:')
                            print('****************************************************************************************************')
                            print("\033[;36m" +
                                f"| {'Codigo':<15}: {datos[0]:<20} | {'Nombre':<15}: {datos[1]:<30}\n" +
                                f"| {'Descripción':<15}: {datos[2]:<50}\n" +
                                f"| {'Precio':<15}: {datos[3]:<20} | {'Stock':<15}: {datos[4]:<20}\n" +
                                '\033[0;m')
                            print('****************************************************************************************************')
                if not producto_encontrado:
                    print("No se encontró el producto proporcionado.")
            except Exception as e:
                print(f'Error al buscar producto: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    def actualizar_producto(self, codigo):
        """
        Actualiza los datos de un producto existente en la base de datos.
        :param codigo: Código del producto a actualizar.
        """
        producto_encontrado = self.buscar_producto_por_codigo(codigo)
        if producto_encontrado:
            print('\nEscriba los nuevos datos del producto:')
            print('------------------------------------------')
            self.set_nombre()
            self.set_descripcion()
            self.set_precio()
            self.set_stock()
            
            nuevo_nombre = self.get_nombre()
            nueva_descripcion = self.get_descripcion()
            nuevo_precio = self.get_precio()
            nuevo_stock = self.get_stock()

            print('\n Datos del producto actualizados:')
            print('------------------------------------------')
            print(f'  Código: {codigo}')
            print(f'  Nuevo nombre: {nuevo_nombre}')
            print(f'  Nueva descripción: {nueva_descripcion}')
            print(f'  Nuevo precio: {nuevo_precio}')
            print(f'  Nuevo stock: {nuevo_stock}')

            conexion = BaseDatos.conectar()
            if conexion:
                try:
                    cursor_producto = conexion.cursor()
                    cursor_producto.callproc('ActualizarProducto', [
                        codigo,
                        nuevo_nombre,
                        nueva_descripcion,
                        nuevo_precio,
                        nuevo_stock
                    ])
                    conexion.commit()
                    cursor_producto.close()
                    print('Producto actualizado')
                except Exception as error:
                    print(f'Error al actualizar el producto: {error}. Intente de nuevo')
                finally:
                    BaseDatos.desconectar()
        else:
            print('Producto no encontrado. Intente otra vez')

    def eliminar_producto(self, codigo_producto):
        """
        Elimina un producto de la base de datos usando su código.
        :param codigo_producto: Código del producto a eliminar.
        """
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursorproducto = conexion.cursor()
                cursorproducto.callproc('EliminarProductoPorCodigo', [codigo_producto])
                conexion.commit()
                print('Producto borrado correctamente...')
            except Exception as e:
                print(f'Error al eliminar el producto: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
