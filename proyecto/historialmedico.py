from conexion10 import BaseDatos
import datetime

class HistorialMedico:

    def __init__(self,
                 id: int = None,
                 fecha: datetime.datetime = None,
                 descripcion: str = None,
                 tratamiento: str = None,
                 codigo: int = None):
        self.__id = id
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tratamiento = tratamiento
        self.__codigo = codigo

    def get_id(self):
        return self.__id

    def get_fecha(self):
        return self.__fecha

    def get_descripcion(self):
        return self.__descripcion

    def get_tratamiento(self):
        return self.__tratamiento

    def get_codigo(self):
        return self.__codigo

    def set_id(self):
        while True:
            try:
                id_historial = int(input('Escriba el id del historial medico: '))
                if 1 <= id_historial <= 1000000000:
                    self.__id = id_historial
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

    def set_codigo(self):
        while True:
            try:
                codigo_mascota = int(input('Escriba el código de la mascota: '))
                if 0 <= codigo_mascota <= 1000000000:
                    self.__codigo = codigo_mascota
                    break
                else:
                    print('El número debe estar entre 0 y 1000000000')
            except ValueError:
                print('El código debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue

    def capturar_datos(self):
        self.set_id()
        self.set_fecha()
        self.set_descripcion()
        self.set_tratamiento()
        self.set_codigo()

    def guardar_historial_medico(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('CrearHistorial', [
                    self.__id,
                    self.__fecha.strftime("%Y-%m-%d"),
                    self.__descripcion,
                    self.__tratamiento,
                    self.__codigo
                ])
                conexion.commit()
                print('Historial medico registrado correctamente...')
            except Exception as e:
                print(f'Error al registrar el historial medico: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
