from conexion10 import BaseDatos
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

    def get_codigo(self):
        return self.__codigo_mascota

    def set_codigo(self):
        while True:
            try:
                codigo_historial = int(input('Escriba el id del historial medico: '))
                if 1 <= codigo_historial <= 1000000000:
                    self.__codigo = codigo_historial
                    break
                else:
                    print('El número debe estar entre 1 y 1000000000')
            except ValueError:
                print('El código debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue

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
        self.set_codigo()
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
                    self.__codigo,
                    self.__fecha.strftime("%Y-%m-%d"),
                    self.__descripcion,
                    self.__tratamiento,
                    self.__codigo_mascota
                ])
                conexion.commit()
                print('Historial medico registrado correctamente...')
            except Exception as e:
                print(f'Error al registrar el historial medico: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()

    def buscar_historial_mascota(self, codigo_mascota=None):
        if codigo_mascota is None:
            self.set_codigo_mascota()
            codigo_historial = self.__codigo_mascota

        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                cursor_historial.callproc('BuscarHistorial', [codigo_mascota])
                print('Búsqueda de historial completado.')
                for result in cursor_historial.stored_results():
                    fila = result.fetchone()
                    while fila is not None:
                        print('Resultado:') # Si encontró  datos los imprime
                        print('**********************************************************************************************')
                        print("\033[;36m" +
                                f"| Id              :{fila[0] :<20}  | Fecha            :{fila[1]} \n" +
                                f"| Descripcion     :{fila[2]:<20}  | Tratamiento      :{fila[3]}  \n" +
                                f"| Codigo_mascota  :{fila[4]:<20}   "
                                '\033[0;m')
                        print('**********************************************************************************************')
                        return fila
                    fila = result.fetchall()
            except Exception as e:
                print(f'Error al buscar historial: {e}')
            finally:
                BaseDatos.desconectar()
        return None
    
    def actualizar_historial(self,  codigo_mascota):
        historial_encontrado = self.buscar_historial_mascota(codigo_mascota)
        if historial_encontrado:
            print('Escriba los nuevos datos de la mascota:')
            self.set_fecha()
            self.set_descripcion()
            self.set_tratamiento()
            
            nuevo_fecha = self.get_fecha()
            nueva_descripcion= self.get_descripcion()
            nueva_tratamiento= self.get_tratamiento()
            
            print(f'Código mascota: {codigo_mascota}')
            print(f'Nuevo fecha: {nuevo_fecha }')
            print(f'Nueva descripción: {nueva_descripcion}')
            print(f'Nueva tratamiento: {nueva_tratamiento}')

            conexion = BaseDatos.conectar()
            if conexion:
                try:
                    cursor_historial = conexion.cursor()
                    cursor_historial.callproc('ActualizarHistorial', [
                        nuevo_fecha,
                        nueva_descripcion,
                        nueva_tratamiento ,
                        codigo_mascota,
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
