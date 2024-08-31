import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from base_datos.conexion10 import BaseDatos
import datetime

class HistorialMedico:

    def __init__(self,
                codigo: int = None,
                fecha: datetime.datetime = None,
                descripcion: str = None,
                tratamiento: str = None,
                codigo_mascota: int = None):
        self.__codigo = codigo
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tratamiento = tratamiento
        self.__codigo_mascota = codigo_mascota

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


    def set_fecha(self):
        while True:
            try:
                fecha = input('Escriba la fecha del historial medico (YYYY-MM-DD): ')
                fecha_historial = datetime.datetime.strptime(fecha, "%Y-%m-%d")
                self.__fecha = fecha_historial
                break  # Salir del bucle si la fecha es válida
            except ValueError:
                print('Formato de fecha inválido. Intente nuevamente.')

    def set_descripcion(self):
        while True:
            descripcion = input('Escriba la descripción del historial medico: ')
            if 1 <= len(descripcion) <= 1000000000:
                self.__descripcion = descripcion
                break
            else:
                print('La descripción debe tener menos de 1000000000 caracteres.')

    def set_tratamiento(self):
        while True:
            tratamiento = input('Escriba el tratamiento del historial medico: ')
            if 1 <= len(tratamiento) <= 1000000000:
                self.__tratamiento = tratamiento
                break
            else:
                print('El tratamiento debe tener menos de 1000000000 caracteres.')

    def set_codigo_mascota(self):
        while True:
            try:
                codigo_mascota = int(input('Escriba el código de la mascota: '))
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

    def capturar_datos(self):
        self.set_fecha()
        self.set_descripcion()
        self.set_tratamiento()
        self.set_codigo_mascota()

    def guardar_historial_medico(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                cursor_historial.callproc('CrearHistorial', [
                    self.get_fecha(),
                    self.get_descripcion(),
                    self.get_tratamiento(),
                    self.get_codigo_mascota()
                ])
                conexion.commit()
                print('Historial médico registrado correctamente...')
                print('\n Datos del historial  médico registrados:')
                print('------------------------------------------')
                print(f'Fecha: {self.get_fecha() }')
                print(f'Descripción: {self.get_descripcion()}')
                print(f'Tratamiento: {self.get_tratamiento()}')
                print(f'Código mascota: {self.get_codigo_mascota()}')
            except Exception as e:
                print(f'Error al registrar el historial médico: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()

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
                        return fila  # Return the found record

                if not historial_encontrado:
                    print('El código de historial médico proporcionado no existe.')
                return historial_encontrado

            except Exception as e:
                print(f'Error al buscar historial médico: {e}')
                return None
            finally:
                BaseDatos.desconectar()
        
        return False  # Return None if no connection could be established



    def buscar_historiales(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                cursor_historial.callproc('BuscarHistoriales')  # Asumiendo que tienes un procedimiento para mostrar todas las mascotas
                print('Listado de todas los historiales medicos completado.')
                historial_encontrado = False
                for result in cursor_historial.stored_results():
                    fila = result.fetchall()
                    if fila:
                        historial_encontrado = True
                        for datos in fila:
                            
                            print('Resultado:')
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                f"| Id              :{datos[0] :<20}  | Fecha            :{datos[1]} \n" +
                                f"| Descripcion     :{datos[2]:<20}  | Tratamiento      :{datos[3]}  \n" +
                                f"| Codigo_mascota  :{datos[4]:<20}   "
                                '\033[0;m')
                            print('**********************************************************************************************')

                if not historial_encontrado:
                    print('El código de historial médico proporcionado no existe.')
            except Exception as e:
                print(f'Error al buscar historial médico: {e}')
            finally:
                BaseDatos.desconectar()
        return None
    
    def actualizar_historial(self,codigo):
        historial_encontrado = self.buscar_historial_id(codigo)
        if historial_encontrado:
            print('Escriba los nuevos datos del historial médico:')
            print('------------------------------------------------')
            self.set_fecha()
            self.set_descripcion()
            self.set_tratamiento()
            self.set_codigo_mascota()

            
            nuevo_fecha = self.get_fecha()
            nueva_descripcion= self.get_descripcion()
            nueva_tratamiento= self.get_tratamiento()
            codigo_mascota= self.get_codigo_mascota()

            print('\n Datos del historial  médico actualizados:')
            print('------------------------------------------')
            print(f'Código historial médico: {codigo}')
            print(f'Nuevo fecha: {nuevo_fecha }')
            print(f'Nueva descripción: {nueva_descripcion}')
            print(f'Nueva tratamiento: {nueva_tratamiento}')
            print(f'Código mascota: {codigo_mascota}')
            conexion = BaseDatos.conectar()
            if conexion:
                try:
                    cursor_historial = conexion.cursor()
                    cursor_historial.callproc('ActualizarHistoriales', [
                        codigo,
                        nuevo_fecha,
                        nueva_descripcion,
                        nueva_tratamiento ,
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

    def eliminar_historial(self, codigo):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial= conexion.cursor()
                cursor_historial.callproc('EliminarHistorial', [codigo])
                conexion.commit()
                print('Historial borrado correctamente...')
            except Exception as e:
                print(f'Error al eliminar el historial: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar() 
