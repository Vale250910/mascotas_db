import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos.conexion10 import BaseDatos


class Productos:
    def __init__(self,
                codigo: str = None,
                nombre: str = None,
                descripcion: str = None,
                precio: float = None,
                stock: int = None,
                estado_acceso:str = None,):
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
        self.__estado_acceso = estado_acceso

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
    
    def get_estado_acceso(self):
        """
        Retorna el estado de acceso del producto.
        """
        return self.__estado_acceso

    # Métodos SET
    def set_codigo(self):
        """
        Solicita al usuario que ingrese el código del producto y valida la entrada.
        """
        while True:
            try:
                codigo = input('Ingrese el código del producto: ').strip()
                if 1 <= len(codigo) <= 10000000:
                    self.__codigo = codigo
                    break
                else:
                    print('Código incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def set_nombre(self):
        """
        Solicita al usuario que ingrese el nombre del producto y valida la entrada.
        """
        while True:
            try:
                nombre = input('Escriba el nombre del producto: ')
                if len(nombre) >1:
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
        """
        Captura todos los datos necesarios para registrar un producto a través de las funciones de entrada.
        """
        self.set_codigo()
        self.set_nombre()
        self.set_descripcion()
        self.set_precio()
        self.set_stock()
        self.set_estado_acceso()

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
                    self.get_codigo(), 
                    self.get_nombre(), 
                    self.get_descripcion(),
                    self.get_precio(),
                    self.get_stock(),
                    self.get_estado_acceso(),
                ])
                conexion.commit()
                print('Producto registrado correctamente...')
                print('\n Datos del producto registrados:')
                print('------------------------------------------')
                print(f'  Código: {self.get_codigo()}')
                print(f'  Nombre: {self.get_nombre()}')
                print(f'  Descripción: {self.get_descripcion()}')
                print(f'  Precio: {self.get_precio()}')
                print(f'  Stock: {self.get_stock()}')
                print(f'  Estado de acceso: {self.get_estado_acceso()}')
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
                                f"| {'Estado de acceso':<15}: {datos[5]:<20}\n" +
                                '\033[0;m')
                            print('****************************************************************************************************')

                if not producto_encontrado:
                    print("No se encontraron productos no existe o esta inactivo.")
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
                            f"| {'Estado de acceso':<15}: {fila[5]:<20}\n" +
                            '\033[0;m')
                        print('****************************************************************************************************')
                        break

                if not producto_encontrado:
                    print('El código de producto proporcionado no existe o esta inactivo.')
                
                return producto_encontrado  # Retorna True si se encontró un producto, False si no
            
            except Exception as e:
                print(f'Error al buscar el producto: {e}')
                return False
            finally:
                BaseDatos.desconectar()
    
        return False 

    def buscar_producto_nombre(self, nombre):
        """
        Busca un producto en la base de datos por su nombre.
        :param nombre_producto: Nombre del producto a buscar.
        """
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursorproducto = conexion.cursor()
                cursorproducto.callproc('BuscarProductosPorNombre', [nombre])
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
                                f"| {'Estado de acceso':<15}: {datos[5]:<20}\n" +
                                '\033[0;m')
                            print('****************************************************************************************************')
                if not producto_encontrado:
                    print("No se encontró el producto proporcionado no existe o esta inactivo.")
            except Exception as e:
                print(f'Error al buscar producto: {e}')
            finally:
                BaseDatos.desconectar()
        return None
    
    def actualizar_estado_producto(self, codigo=None, nuevo_estado_acceso=None):
        if codigo is None:
            self.set_codigo()  
            codigo = self.get_codigo()
            
        if nuevo_estado_acceso is None:
            self.set_estado_acceso()
            nuevo_estado_acceso = self.get_estado_acceso()  
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()  
                cursor_mascota.callproc('ActualizarEstadoProductos', (codigo, nuevo_estado_acceso))
                for result in cursor_mascota.stored_results():
                    filas = result.fetchall()
                    if filas:
                        for fila in filas:
                            print('**********************************************************************************************')
                            print(f'Codigo: {fila[0]},  Nombre: {fila[1]} Estado: {fila[2]}')
                            print('**********************************************************************************************')
                    else:
                        print(f'No se encontraron resultados para el documento {codigo}.')
                conexion.commit()
                print(f'Estado de acceso actualizado a {nuevo_estado_acceso} para el producto con codigo {codigo}.')
            except Exception as e:
                print(f'Error al actualizar el estado: {e}')
            finally:
                BaseDatos.desconectar()  
        else:
            print('No se pudo establecer la conexión con la base de datos.')

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
           print('Producto no encontrado. Asegúrese de que el código ingresado sea correcto o que el producto esté activo. Intente nuevamente.')


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
