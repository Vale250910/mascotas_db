from conexion10 import BaseDatos
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
        self.__codigo = codigo
        self.__fecha = fecha
        self.__hora = hora
        self.__id_servicio = id_servicio
        self.__id_veterinario = id_veterinario
        self.__codigo_mascota = codigo_mascota
        self.__estado = estado

    def get_codigo(self):
        return self.__codigo

    def get_fecha(self):
        return self.__fecha

    def get_hora(self):
        return self.__hora

    def get_id_servicio(self):
        return self.__id_servicio
    
    def get_id_veterinario(self):
        return self.__id_veterinario

    def get_codigo_mascota(self):  # Corregido el nombre del método
        return self.__codigo_mascota
    
    def get_estado(self):
        return self.__estado

    def set_estado(self):
        while True:
            try:
                estado = input('Escriba el estado de la cita (PENDIENTE, CONFIRMADA, CANCELADA, REALIZADA, NO ASISTIDA): ').lower()
                if estado in ['pendiente', 'confirmada', 'cancelada', 'realizada', 'no asistida']:  # Corregido el espacio extra
                    self.__estado = estado
                    break
                else:
                    print('El estado debe ser PENDIENTE, CONFIRMADA, CANCELADA, REALIZADA o NO ASISTIDA.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')

    def set_codigo(self):
        while True:
            try:
                codigo_historial = int(input('Escriba el codigo de la cita: '))
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
                fecha = input('Escriba la fecha de la cita (YYYY-MM-DD): ')
                fecha_historial = datetime.datetime.strptime(fecha, "%Y-%m-%d")
                self.__fecha = fecha_historial
                break
            except ValueError:
                print('Formato de fecha inválido. Intente nuevamente.')

    def set_hora(self):
        while True:
            try:
                hora = input('Escriba la hora de la cita (HH:MM:SS): ')
                hora_historial = datetime.datetime.strptime(hora, "%H:%M:%S").time()
                self.__hora = hora_historial
                break
            except ValueError:
                print('Formato de hora inválido. Intente nuevamente.')
    
    def set_id_servicios(self):
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
            continue

    def set_id_veterinario(self):
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
            continue
    
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
        self.set_hora()
        self.set_id_servicios()
        self.set_id_veterinario()
        self.set_codigo_mascota()
        self.set_estado()

    def guardar_cita(self):
        self.capturar_datos()
        
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('InsertarCita', [
                    self.__codigo,
                    self.__fecha.strftime("%Y-%m-%d"),
                    self.__hora.strftime("%H:%M:%S"),
                    self.__id_servicio,
                    self.__id_veterinario,
                    self.__codigo_mascota,
                    self.__estado
                ])
                conexion.commit()
                print('Cita registrada correctamente...')
            except Exception as e:
                print(f'Error al registrar la cita: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()

    def buscar_cita_fecha(self, fecha=None):
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
    
    def buscar_cita_mascota(self, codigo_mascota=None):
        if codigo_mascota is None:
            self.set_codigo_mascota()
            codigo_mascota = self.__codigo_mascota
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('BuscarCitaPorMascota', [codigo_mascota])
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
                                f"| Hora               :{hora_cita:<20}   | Id_servicio    :{datos[3]}  \n" +
                                f"| Id_veterinario     :{datos[4]:<20}   | Código mascota  :{datos[5]:<20}\n" +
                                f"| Estado             :{datos[6]:<20}   |\033[0m" +  # Resetear el color al final de la línea
                                '\033[0;m')
                            print('**********************************************************************************************')

                if not cita_encontrada:
                    print("No se encontraron citas para el codigo de mascota proporcionado.")
            except Exception as e:
                print(f'Error al buscar cita: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    def buscar_citas(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('BuscarCitas')  # Asumiendo que tienes un procedimiento para mostrar todas las mascotas
                print('Listado de todas las mascotas completado.')

                for result in cursor_mascota.stored_results():
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
                    print("No se encontraron las citas proporcionada.")
            except Exception as e:
                print(f'Error al buscar cita: {e}')
            finally:
                BaseDatos.desconectar()
        return None



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
