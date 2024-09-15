import sys
import os
import datetime
from base_datos.conexion10 import BaseDatos

# Clase para manejar el historial médico de las mascotas
class HistorialMedico:

    def __init__(self,
                codigo: int = None,
                fecha: datetime.datetime = None,
                descripcion: str = None,
                tratamiento: str = None,
                codigo_mascota: int = None):
        # Inicialización de atributos del historial médico
        self.__codigo = codigo
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tratamiento = tratamiento
        self.__codigo_mascota = codigo_mascota

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

    # Métodos setters con validación
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
        self.set_fecha()
        self.set_descripcion()
        self.set_tratamiento()
        self.set_codigo_mascota()

    # Guardar el historial médico en la base de datos
    def guardar_historial_medico(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                # Llamada al procedimiento almacenado para crear el historial
                cursor_historial.callproc('CrearHistorial', [
                    self.get_fecha(),
                    self.get_descripcion(),
                    self.get_tratamiento(),
                    self.get_codigo_mascota()
                ])
                conexion.commit()
                print('Historial médico registrado correctamente...')
                print('\n Datos del historial médico registrados:')
                print('------------------------------------------')
                print(f'Fecha: {self.get_fecha()}')
                print(f'Descripción: {self.get_descripcion()}')
                print(f'Tratamiento: {self.get_tratamiento()}')
                print(f'Código mascota: {self.get_codigo_mascota()}')
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
                        print('**********************************************************************************************')
                        print("\033[;36m" +
                            f"| Id              :{fila[0]:<20}  | Fecha            :{fila[1]} \n" +
                            f"| Descripcion     :{fila[2]:<20}  | Tratamiento      :{fila[3]}  \n" +
                            f"| Codigo_mascota  :{fila[4]:<20}   "
                            '\033[0;m')
                        print('**********************************************************************************************')
                        return fila  # Retorna el historial encontrado

                if not historial_encontrado:
                    print('El código de historial médico proporcionado no existe.')
                return historial_encontrado

            except Exception as e:
                print(f'Error al buscar historial médico: {e}')
                return None
            finally:
                BaseDatos.desconectar()
        
        return False  # Retorna False si no se pudo establecer conexión

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
                                f"| Id              :{datos[0]:<20}  | Fecha            :{datos[1]} \n" +
                                f"| Descripcion     :{datos[2]:<20}  | Tratamiento      :{datos[3]}  \n" +
                                f"| Codigo_mascota  :{datos[4]:<20}   "
                                '\033[0;m')
                            print('**********************************************************************************************')

                if not historial_encontrado:
                    print('No se encontraron historiales médicos.')
            except Exception as e:
                print(f'Error al buscar historiales médicos: {e}')
            finally:
                BaseDatos.desconectar()
        return None
    
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
            codigo_mascota = self.get_codigo_mascota()

            print('\n Datos del historial médico actualizados:')
            print('------------------------------------------')
            print(f'Código historial médico: {codigo}')
            print(f'Nueva fecha: {nuevo_fecha}')
            print(f'Nueva descripción: {nueva_descripcion}')
            print(f'Nuevo tratamiento: {nueva_tratamiento}')
            print(f'Código mascota: {codigo_mascota}')
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
                        codigo_mascota
                    ])
                    conexion.commit()
                    cursor_historial.close()
                    print('Historial actualizado')
                except Exception as error:
                    print(f'Error al actualizar el historial: {error}. Intente de nuevo')
                finally:
                    BaseDatos.desconectar()
        else:
            print('Historial no encontrado. Intente otra vez')

    # Eliminar un historial médico por ID
    def eliminar_historial(self, codigo):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                # Llamada al procedimiento almacenado para eliminar el historial
                cursor_historial.callproc('EliminarHistorial', [codigo])
                conexion.commit()
                print('Historial borrado correctamente...')
            except Exception as e:
                print(f'Error al eliminar el historial: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
