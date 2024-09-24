import sys
import os
import datetime
from base_datos.conexion10 import BaseDatos

# Clase para manejar el historial médico de las mascotas
class HistorialMedico:

    def __init__(self,
<<<<<<< HEAD
                codigo: str = None,
                fecha: datetime.datetime = None,
                descripcion: str = None,
                tratamiento: str = None,
                codigo_mascota: str = None,
                estado_acceso:str = None):
=======
                codigo: int = None,
                fecha: datetime.datetime = None,
                descripcion: str = None,
                tratamiento: str = None,
                codigo_mascota: int = None):
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        # Inicialización de atributos del historial médico
        self.__codigo = codigo
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tratamiento = tratamiento
        self.__codigo_mascota = codigo_mascota
<<<<<<< HEAD
        self.__estado_acceso = estado_acceso
=======
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6

    # Métodos getters
    def get_codigo(self):
        return self.__codigo

    def get_fecha(self):
        return self.__fecha

    def get_descripcion(self):
        return self.__descripcion

    def get_tratamiento(self):
        return self.__tratamiento

    def get_codigo_mascota(self):
        return self.__codigo_mascota
<<<<<<< HEAD
    
    def get_estado_acceso(self):
        return self.__estado_acceso

    # Métodos setters con validación
    def set_codigo(self):
        while True:
            try:
                codigo = input('Ingrese el codigo de el historial: ').strip()
                if 1<= len(codigo) <= 10000000:
                    self.__codigo = codigo
                    break
                else:
                    print('El codigo debe ser una cadena de 1 a 10000000 dígitos.')
            except KeyboardInterrupt:
                print('\nEl usuario ha cancelado la entrada de datos.')
                return None 
            
=======

    # Métodos setters con validación
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    def set_fecha(self):
        while True:
            try:
                fecha = input('Escriba la fecha del historial medico (YYYY-MM-DD): ')
                # Validación del formato de la fecha
                fecha_historial = datetime.datetime.strptime(fecha, "%Y-%m-%d")
                self.__fecha = fecha_historial
                break
            except ValueError:
                print('Formato de fecha inválido. Intente nuevamente.')

    def set_descripcion(self):
        while True:
            descripcion = input('Escriba la descripción del historial medico: ')
            # Validación de longitud de la descripción
            if 1 <= len(descripcion) <= 1000000000:
                self.__descripcion = descripcion
                break
            else:
                print('La descripción debe tener menos de 1000000000 caracteres.')

    def set_tratamiento(self):
        while True:
            tratamiento = input('Escriba el tratamiento del historial medico: ')
            # Validación de longitud del tratamiento
            if 1 <= len(tratamiento) <= 1000000000:
                self.__tratamiento = tratamiento
                break
            else:
                print('El tratamiento debe tener menos de 1000000000 caracteres.')

    def set_codigo_mascota(self):
<<<<<<< HEAD
            while True:
                try:
                    codigo_mascota = input('Ingrese el codigo de la mascota: ').strip()
                    if 1<= len(codigo_mascota) <= 10000000:
                        self.__codigo_mascota = codigo_mascota
                        break
                    else:
                        print('El codigo debe ser una cadena de 1 a 10000000 dígitos.')
                except KeyboardInterrupt:
                    print('\nEl usuario ha cancelado la entrada de datos.')
                    return None 
    
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

    # Captura de datos del historial médico
    def capturar_datos(self):
        self.set_codigo()
=======
        while True:
            try:
                codigo_mascota = int(input('Escriba el código de la mascota: '))
                # Validación del rango del código de la mascota
                if 0 <= codigo_mascota <= 1000000000:
                    self.__codigo_mascota = codigo_mascota
                    break
                else:
                    print('El número debe estar entre 0 y 1000000000')
            except ValueError:
                print('El código debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue

    # Captura de datos del historial médico
    def capturar_datos(self):
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        self.set_fecha()
        self.set_descripcion()
        self.set_tratamiento()
        self.set_codigo_mascota()
<<<<<<< HEAD
        self.set_estado_acceso()
=======
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6

    # Guardar el historial médico en la base de datos
    def guardar_historial_medico(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                # Llamada al procedimiento almacenado para crear el historial
                cursor_historial.callproc('CrearHistorial', [
<<<<<<< HEAD
                    self.get_codigo(),
                    self.get_fecha(),
                    self.get_descripcion(),
                    self.get_tratamiento(),
                    self.get_codigo_mascota(),
                    self.get_estado_acceso()  # El estado de acceso se envía como un parámetro de entrada al procedimiento almacenado, no como una columna en la tabla.
=======
                    self.get_fecha(),
                    self.get_descripcion(),
                    self.get_tratamiento(),
                    self.get_codigo_mascota()
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                ])
                conexion.commit()
                print('Historial médico registrado correctamente...')
                print('\n Datos del historial médico registrados:')
                print('------------------------------------------')
<<<<<<< HEAD
                print(f'Codigo Historial:{self.get_codigo()}')
=======
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                print(f'Fecha: {self.get_fecha()}')
                print(f'Descripción: {self.get_descripcion()}')
                print(f'Tratamiento: {self.get_tratamiento()}')
                print(f'Código mascota: {self.get_codigo_mascota()}')
<<<<<<< HEAD
                print(f'Estado de acceso: {self.get_estado_acceso()}')
=======
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
            except Exception as e:
                print(f'Error al registrar el historial médico: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()

    # Buscar un historial médico por ID
    def buscar_historial_id(self, codigo=None):
        if codigo is None:
            self.get_codigo()
            codigo_historial = self.__codigo
        else:
            codigo_historial = codigo

        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                # Llamada al procedimiento almacenado para buscar el historial por ID
                cursor_historial.callproc('BuscarHistorialId', [codigo_historial])
                print('Búsqueda de historial completada.')
                historial_encontrado = False
                for result in cursor_historial.stored_results():
                    fila = result.fetchone()
                    if fila:
                        historial_encontrado = True
                        print('Resultado:')
<<<<<<< HEAD
                        fecha_historial = fila[1] if isinstance(fila[1], datetime.date) else str(fila[1])
                        print('**********************************************************************************************')
                        print("\033[;36m" +
                            f"| Codigo          :{fila[0]:<20}  | Fecha            :{fecha_historial} \n" +
                            f"| Descripcion     :{fila[2]:<20}                                       \n" +
                            f"| Tratamiento     :{fila[3]:<20}                                       \n" +
                            f"| Codigo mascota  :{fila[4]:<20}  | Estado Acceso    : {fila[5]} \n" +
=======
                        print('**********************************************************************************************')
                        print("\033[;36m" +
                            f"| Id              :{fila[0]:<20}  | Fecha            :{fila[1]} \n" +
                            f"| Descripcion     :{fila[2]:<20}  | Tratamiento      :{fila[3]}  \n" +
                            f"| Codigo_mascota  :{fila[4]:<20}   "
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                            '\033[0;m')
                        print('**********************************************************************************************')
                        return fila  # Retorna el historial encontrado

                if not historial_encontrado:
<<<<<<< HEAD
                    print('El código de historial médico proporcionado no existe o esta inactivo.')
=======
                    print('El código de historial médico proporcionado no existe.')
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                return historial_encontrado

            except Exception as e:
                print(f'Error al buscar historial médico: {e}')
                return None
            finally:
                BaseDatos.desconectar()
        
        return False  # Retorna False si no se pudo establecer conexión
<<<<<<< HEAD
    def actualizar_estado_historial(self, codigo=None, nuevo_estado_acceso=None):
        if codigo is None:
            self.set_codigo()  
            codigo = self.get_codigo()
            
        if nuevo_estado_acceso is None:
            self.set_estado_acceso()
            nuevo_estado_acceso = self.get_estado_acceso()  
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()  
                cursor_historial.callproc('ActualizarEstadoHistoriales', (codigo, nuevo_estado_acceso))
                for result in cursor_historial.stored_results():
                    filas = result.fetchall()
                    if filas:
                        for fila in filas:
                            print('**********************************************************************************************')
                            print(f'Codigo: {fila[0]},  Estado: {fila[1]}')
                            print('**********************************************************************************************')
                    else:
                        print(f'No se encontraron resultados para el documento {codigo}.')
                conexion.commit()
                print(f'Estado de acceso actualizado a {nuevo_estado_acceso} para el historial con codigo {codigo}.')
            except Exception as e:
                print(f'Error al actualizar el estado: {e}')
            finally:
                BaseDatos.desconectar()  
        else:
            print('No se pudo establecer la conexión con la base de datos.')
=======

>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    # Buscar todos los historiales médicos
    def buscar_historiales(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                # Llamada al procedimiento almacenado para buscar todos los historiales
                cursor_historial.callproc('BuscarHistoriales')
                print('Listado de todas los historiales médicos completado.')
                historial_encontrado = False
                for result in cursor_historial.stored_results():
                    fila = result.fetchall()
                    if fila:
                        historial_encontrado = True
                        for datos in fila:
                            print('Resultado:')
                            print('**********************************************************************************************')
                            print("\033[;36m" +
<<<<<<< HEAD
                                f"| Codigo          :{datos[0]:<20}  | Fecha             :{datos[1]} \n" +
                                f"| Descripcion     :{datos[2]:<20}                                 \n" + 
                                f"| Tratamiento     :{datos[3]:<20}                                 \n" +
                                f"| Codigo mascota  :{datos[4]:<20}   | Estado Acceso     :{datos[5]} \n" +
=======
                                f"| Id              :{datos[0]:<20}  | Fecha            :{datos[1]} \n" +
                                f"| Descripcion     :{datos[2]:<20}  | Tratamiento      :{datos[3]}  \n" +
                                f"| Codigo_mascota  :{datos[4]:<20}   "
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                                '\033[0;m')
                            print('**********************************************************************************************')

                if not historial_encontrado:
<<<<<<< HEAD
                    print('No se encontraron historiales médicos proporcionados no existe o esta inactivo.')
=======
                    print('No se encontraron historiales médicos.')
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
            except Exception as e:
                print(f'Error al buscar historiales médicos: {e}')
            finally:
                BaseDatos.desconectar()
        return None
    
<<<<<<< HEAD
    
=======
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
    # Actualizar un historial médico por ID
    def actualizar_historial(self, codigo):
        historial_encontrado = self.buscar_historial_id(codigo)
        if historial_encontrado:
            print('Escriba los nuevos datos del historial médico:')
            print('------------------------------------------------')
            self.set_fecha()
            self.set_descripcion()
            self.set_tratamiento()
            self.set_codigo_mascota()

            nuevo_fecha = self.get_fecha()
            nueva_descripcion = self.get_descripcion()
            nueva_tratamiento = self.get_tratamiento()
<<<<<<< HEAD
            nuevo_codigo_mascota = self.get_codigo_mascota()
=======
            codigo_mascota = self.get_codigo_mascota()
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6

            print('\n Datos del historial médico actualizados:')
            print('------------------------------------------')
            print(f'Código historial médico: {codigo}')
            print(f'Nueva fecha: {nuevo_fecha}')
            print(f'Nueva descripción: {nueva_descripcion}')
            print(f'Nuevo tratamiento: {nueva_tratamiento}')
<<<<<<< HEAD
            print(f'Código mascota: {nuevo_codigo_mascota}')
=======
            print(f'Código mascota: {codigo_mascota}')
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
            conexion = BaseDatos.conectar()
            if conexion:
                try:
                    cursor_historial = conexion.cursor()
                    # Llamada al procedimiento almacenado para actualizar el historial
                    cursor_historial.callproc('ActualizarHistoriales', [
                        codigo,
                        nuevo_fecha,
                        nueva_descripcion,
                        nueva_tratamiento,
<<<<<<< HEAD
                        nuevo_codigo_mascota
=======
                        codigo_mascota
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                    ])
                    conexion.commit()
                    cursor_historial.close()
                    print('Historial actualizado')
                except Exception as error:
                    print(f'Error al actualizar el historial: {error}. Intente de nuevo')
                finally:
                    BaseDatos.desconectar()
        else:
<<<<<<< HEAD
            print('Historial no encontrado. Asegúrese de que el código ingresado sea correcto o que el historial esté activo. Intente nuevamente.')
=======
            print('Historial no encontrado. Intente otra vez')
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6

    # Eliminar un historial médico por ID
    def eliminar_historial(self, codigo):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                # Llamada al procedimiento almacenado para eliminar el historial
<<<<<<< HEAD
                cursor_historial.callproc('EliminarHistorialPorCodigo', [codigo])
=======
                cursor_historial.callproc('EliminarHistorial', [codigo])
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                conexion.commit()
                print('Historial borrado correctamente...')
            except Exception as e:
                print(f'Error al eliminar el historial: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
