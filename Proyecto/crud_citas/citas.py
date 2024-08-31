import sys
import os
import datetime
from base_datos.conexion10 import BaseDatos  # Importar la clase de conexión a la base de datos

# Clase para manejar las citas en el sistema
class Citas:

    # Constructor de la clase
    def __init__(self,
                 codigo: int = None,
                 fecha: datetime.datetime = None,
                 hora: datetime.datetime = None,
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

    # Métodos getter para obtener los atributos de la cita
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

    def get_codigo_mascota(self):
        return self.__codigo_mascota
    
    def get_estado(self):
        return self.__estado

    # Métodos setter para ingresar y validar los atributos de la cita
    def set_estado(self):
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
    
    def set_id_servicio(self):
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

    # Método para capturar todos los datos de la cita
    def capturar_datos(self):
        self.set_fecha()
        self.set_hora()
        self.set_id_servicio()
        self.set_id_veterinario()
        self.set_codigo_mascota()
        self.set_estado()

    # Método para guardar la cita en la base de datos
    def guardar_cita(self):
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
                print(f'Id servicio: {self.get_id_servicio()}')
                print(f'Id veterinario: {self.get_id_veterinario()}')
                print(f'Codigo mascota: {self.get_codigo_mascota()}')
                print(f'Estado: {self.get_estado()}')
            except Exception as e:
                print(f'Error al registrar la cita: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()

    # Método para buscar citas por fecha
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
    
    # Método para buscar citas por código
    def buscar_cita_id(self, codigo=None):
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
                            print('**********************************************************************************************')
                            return fila
                if not cita_encontrada:
                    print("No se encontraron citas para el código proporcionado.")
            except Exception as e:
                print(f'Error al buscar cita: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    # Método para buscar todas las citas
    def buscar_citas(self):
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
                    print("No se encontraron citas.")
            except Exception as e:
                print(f'Error al buscar citas: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    # Método para actualizar una cita existente
    def actualizar_cita(self, codigo):
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
            print(f'Nuevo Id servicio: {nuevo_id_servicio}')
            print(f'Nuevo Id veterinario: {nuevo_id_veterinario}')
            print(f'Nuevo Codigo mascota: {nuevo_codigo_mascota}')
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

    # Método para eliminar una cita
    def eliminar_cita(self, codigo):
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

