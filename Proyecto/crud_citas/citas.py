import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos.conexion10 import BaseDatos
import datetime

class Citas:

    def __init__(self,
                codigo: int = None,
                fecha: datetime.datetime = None,
                hora: datetime.datetime= None,
                id_servicio: int = None,
                id_veterinario: int = None,
                codigo_mascota: int = None,
                estado: str = None):
        """
        Inicializa un objeto Citas con los atributos proporcionados.
        :param codigo: Código de la cita.
        :param fecha: Fecha de la cita.
        :param hora: Hora de la cita.
        :param id_servicio: ID del servicio asociado a la cita.
        :param id_veterinario: ID del veterinario que atiende la cita.
        :param codigo_mascota: Código de la mascota para la cual se realiza la cita.
        :param estado: Estado de la cita (PENDIENTE, CONFIRMADA, CANCELADA, REALIZADA, NO ASISTIDA).
        """
        self.__codigo = codigo
        self.__fecha = fecha
        self.__hora = hora
        self.__id_servicio = id_servicio
        self.__id_veterinario = id_veterinario
        self.__codigo_mascota = codigo_mascota
        self.__estado = estado

    def get_codigo(self):
        """
        Retorna el código de la cita.
        """
        return self.__codigo

    def get_fecha(self):
        """
        Retorna la fecha de la cita.
        """
        return self.__fecha

    def get_hora(self):
        """
        Retorna la hora de la cita.
        """
        return self.__hora

    def get_id_servicio(self):
        """
        Retorna el ID del servicio de la cita.
        """
        return self.__id_servicio
    
    def get_id_veterinario(self):
        """
        Retorna el ID del veterinario de la cita.
        """
        return self.__id_veterinario

    def get_codigo_mascota(self):
        """
        Retorna el código de la mascota de la cita.
        """
        return self.__codigo_mascota
    
    def get_estado(self):
        """
        Retorna el estado de la cita.
        """
        return self.__estado

    def set_estado(self):
        """
        Solicita al usuario que ingrese el estado de la cita y valida la entrada.
        """
        while True:
            try:
                estado = input('Escriba el estado de la cita (PENDIENTE, CONFIRMADA, CANCELADA, REALIZADA, NO ASISTIDA): ').lower()
                if estado in ['pendiente', 'confirmada', 'cancelada', 'realizada', 'no asistida']:
                    self.__estado = estado
                    break
                else:
                    print('El estado debe ser PENDIENTE, CONFIRMADA, CANCELADA, REALIZADA o NO ASISTIDA.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')

    def set_fecha(self):
        """
        Solicita al usuario que ingrese la fecha de la cita y valida la entrada.
        """
        while True:
            try:
                fecha = input('Escriba la fecha de la cita (YYYY-MM-DD): ')
                fecha_historial = datetime.datetime.strptime(fecha, "%Y-%m-%d")
                self.__fecha = fecha_historial
                break
            except ValueError:
                print('Formato de fecha inválido. Intente nuevamente.')

    def set_hora(self):
        """
        Solicita al usuario que ingrese la hora de la cita y valida la entrada.
        """
        while True:
            try:
                hora = input('Escriba la hora de la cita (HH:MM:SS): ')
                hora_historial = datetime.datetime.strptime(hora, "%H:%M:%S").time()
                self.__hora = hora_historial
                break
            except ValueError:
                print('Formato de hora inválido. Intente nuevamente.')
    
    def set_id_servicio(self):
        """
        Solicita al usuario que ingrese el ID del servicio y valida la entrada.
        """
        while True:
            try:
                id_servicio = int(input('Escriba el id del servicio: '))
                if 0 <= id_servicio <= 1000000000:
                    self.__id_servicio = id_servicio
                    break
                else:
                    print('El número debe estar entre 0 y 1000000000')
            except ValueError:
                print('El id debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')

    def set_id_veterinario(self):
        """
        Solicita al usuario que ingrese el ID del veterinario y valida la entrada.
        """
        while True:
            try:
                id_veterinario = int(input('Escriba el id del veterinario: '))
                if 0 <= id_veterinario <= 1000000000:
                    self.__id_veterinario = id_veterinario
                    break
                else:
                    print('El número debe estar entre 0 y 1000000000')
            except ValueError:
                print('El id debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')

    def set_codigo_mascota(self):
        """
        Solicita al usuario que ingrese el código de la mascota y valida la entrada.
        """
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

    def capturar_datos(self):
        """
        Captura todos los datos necesarios para la cita a través de las funciones de entrada.
        """
        self.set_fecha()
        self.set_hora()
        self.set_id_servicio()
        self.set_id_veterinario()
        self.set_codigo_mascota()
        self.set_estado()

    def guardar_cita(self):
        """
        Captura los datos de la cita y guarda la información en la base de datos.
        """
        self.capturar_datos()
        
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('InsertarCita', [
                    self.get_fecha(),
                    self.get_hora(),
                    self.get_id_servicio(),
                    self.get_id_veterinario(),
                    self.get_codigo_mascota(),
                    self.get_estado()
                ])
                conexion.commit()
                print('Cita registrada correctamente...')
                print('\n Datos de la cita registrada:')
                print('------------------------------------------')
                print(f'Fecha: {self.get_fecha()}')
                print(f'Hora: {self.get_hora()}')
                print(f'Id servicio:{self.get_id_servicio()}')
                print(f'Id veterinario:{self.get_id_veterinario()}')
                print(f'Codigo mascota:{self.get_codigo_mascota()}')
                print(f'Estado: {self.get_estado()}')
            except Exception as e:
                print(f'Error al registrar la cita: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()

    def buscar_cita_fecha(self, fecha=None):
        """
        Busca citas por fecha. Si no se proporciona una fecha, solicita al usuario que la ingrese.
        :param fecha: Fecha para buscar la cita. Si es None, se solicita al usuario que ingrese una fecha.
        """
        if fecha is None:
            self.set_fecha()
            fecha = self.__fecha
            if isinstance(fecha, datetime.datetime):
                fecha = fecha.strftime("%Y-%m-%d")  # Formatear si es un objeto datetime

        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('BuscarCitaPorFecha', [fecha])
                print('Búsqueda de cita completada.')
                cita_encontrada = False

                for result in cursor_cita.stored_results():
                    filas = result.fetchall()
                    if filas:
                        cita_encontrada = True
                        for datos in filas:
                            # Asegúrate de que la fecha y hora sean del tipo correcto
                            fecha_cita = datos[1] if isinstance(datos[1], datetime.date) else str(datos[1])
                            hora_cita = datos[2] if isinstance(datos[2], datetime.time) else str(datos[2])
                            
                            print('Resultado:')
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                f"| Codigo             :{datos[0]:<20}   | Fecha           :{fecha_cita} \n" +
                                f"| Hora               :{hora_cita:<20}   | Id_servicio     :{datos[3]}  \n" +
                                f"| Id_veterinario     :{datos[4]:<20}   | Código mascota  :{datos[5]:<20}\n" +
                                f"| Estado             :{datos[6]:<20}   |\033[0m" +  # Resetear el color al final de la línea
                                '\033[0;m')
                            print('**********************************************************************************************')

                if not cita_encontrada:
                    print("No se encontraron citas para la fecha proporcionada.")
            except Exception as e:
                print(f'Error al buscar cita: {e}')
            finally:
                BaseDatos.desconectar()
        return None
    
    def buscar_cita_id(self, codigo=None):
        """
        Busca una cita por código. Si no se proporciona un código, solicita al usuario que lo ingrese.
        :param codigo: Código de la cita a buscar. Si es None, se solicita al usuario que ingrese el código.
        """
        if codigo is None:
            self.get_codigo()
            codigo = self.__codigo
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('BuscarCitaPorId', [codigo])
                print('Búsqueda de cita completada.')
                cita_encontrada = False
                for result in cursor_cita.stored_results():
                    fila = result.fetchone()
                    if fila:
                        cita_encontrada = True
                        while fila is not None:
                                # Asegúrate de que la fecha y hora sean del tipo correcto
                                fecha_cita = fila[1] if isinstance(fila[1], datetime.date) else str(fila[1])
                                hora_cita = fila[2] if isinstance(fila[2], datetime.time) else str(fila[2])
                                print('Resultado:')
                                print('**********************************************************************************************')
                                print("\033[;36m" +
                                    f"| Codigo             :{fila[0]:<20}   | Fecha           :{fecha_cita} \n" +
                                    f"| Hora               :{hora_cita:<20}   | Id_servicio    :{fila[3]}  \n" +
                                    f"| Id_veterinario     :{fila[4]:<20}   | Código mascota  :{fila[5]:<20}\n" +
                                    f"| Estado             :{fila[6]:<20}   |\033[0m" +  # Resetear el color al final de la línea
                                    '\033[0;m')
                                return fila
                if not cita_encontrada:
                    print("No se encontraron citas para el código proporcionado.")
            except Exception as e:
                print(f'Error al buscar cita: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    def buscar_citas(self):
        """
        Busca y muestra todas las citas almacenadas en la base de datos.
        """
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_citas = conexion.cursor()
                cursor_citas.callproc('BuscarCitas')  # Asumiendo que tienes un procedimiento para mostrar todas las citas
                print('Listado de todas las citas completado.')
                cita_encontrada = False
                for result in cursor_citas.stored_results():
                    fila = result.fetchall()
                    if fila:
                        cita_encontrada = True
                        for datos in fila:
                            # Asegúrate de que la fecha y hora sean del tipo correcto
                            fecha_cita = datos[1] if isinstance(datos[1], datetime.date) else str(datos[1])
                            hora_cita = datos[2] if isinstance(datos[2], datetime.time) else str(datos[2])
                            print('Resultado:')
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                f"| Codigo             :{datos[0]:<20}   | Fecha           :{fecha_cita} \n" +
                                f"| Hora               :{hora_cita:<20}   | Id_servicio    :{datos[3]}  \n" +
                                f"| Id_veterinario     :{datos[4]:<20}   | Código mascota  :{datos[5]:<20}\n" +
                                f"| Estado             :{datos[6]:<20}   |\033[0m" +  # Resetear el color al final de la línea
                                '\033[0;m')
                            print('**********************************************************************************************')

                if not cita_encontrada:
                    print("No se encontraron las citas proporcionadas.")
            except Exception as e:
                print(f'Error al buscar cita: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    def actualizar_cita(self, codigo):
        """
        Actualiza la información de una cita existente.
        :param codigo: Código de la cita a actualizar.
        """
        cita_encontrada = self.buscar_cita_id(codigo)
        if cita_encontrada:
            print('Escriba los nuevos datos de la cita:')
            print('------------------------------------------')
            self.set_fecha()
            self.set_hora()
            self.set_id_servicio()
            self.set_id_veterinario()
            self.set_codigo_mascota()  
            self.set_estado()
            
            nuevo_fecha = self.get_fecha()
            nuevo_hora = self.get_hora() 
            nuevo_id_servicio = self.get_id_servicio()
            nuevo_id_veterinario = self.get_id_veterinario()
            nuevo_codigo_mascota = self.get_codigo_mascota()
            nueva_estado = self.get_estado()
            
            print('\n Datos de la cita actualizados:')
            print('------------------------------------------')
            print(f'Codigo cita: {codigo}')
            print(f'Nueva fecha: {nuevo_fecha}')
            print(f'Nueva hora: {nuevo_hora}')
            print(f'Nuevo Id servicio:{nuevo_id_servicio}')
            print(f'Nuevo Id veterinario:{nuevo_id_veterinario}')
            print(f'Nuevo Codigo mascota:{nuevo_codigo_mascota}')
            print(f'Nuevo estado: {nueva_estado}')

            conexion = BaseDatos.conectar()
            if conexion:
                try:
                    cursor_cita = conexion.cursor()
                    cursor_cita.callproc('ActualizarCitas', [
                        codigo,
                        nuevo_fecha,
                        nuevo_hora,
                        nuevo_id_servicio,
                        nuevo_id_veterinario,
                        nuevo_codigo_mascota,
                        nueva_estado
                    ])
                    conexion.commit()
                    cursor_cita.close()
                    print('Cita actualizada')
                except Exception as error:
                    print(f'Error al actualizar la cita: {error}. Intente de nuevo')
                finally:
                    BaseDatos.desconectar()
        else:
            print('Cita no encontrada. Intente otra vez')

    def eliminar_cita(self, codigo):
        """
        Elimina una cita existente en la base de datos.
        :param codigo: Código de la cita a eliminar.
        """
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                cursor_historial.callproc('EliminarCitaPorCodigo', [codigo])
                conexion.commit()
                print('Cita borrada correctamente...')
            except Exception as e:
                print(f'Error al eliminar la cita: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()

