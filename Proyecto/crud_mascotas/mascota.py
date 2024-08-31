#from historial_medico import HistorialMedico
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos.conexion10 import BaseDatos
from colorama import init, Fore, Back, Style
import re
init()

class Mascota:
    def __init__(
            self,
            codigo: int = None,
            nombre: str= None,
            especie: str= None,
            raza: str= None,
            edad: float= None,
            peso: float= None,
            id_usuario: int = None,
            historial_medico= None
            ):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__id_usuario = id_usuario
        self.__historial_medico = historial_medico if historial_medico is not None else []

    # GET y SET

    def get_codigo(self):
        return self.__codigo
        
    def get_nombre(self):
        return self.__nombre
    
    def get_especie(self):
        return self.__especie
    
    def get_raza(self):
        return self.__raza
    
    def get_edad(self):
        return self.__edad
    
    def get_peso(self):
        return self.__peso
    
    def get_id_usuario(self):
        return self.__id_usuario 
    
    def get_historial(self):
        return self.__historial

    def set_nombre(self):
        while True:
            try:
                nombre = input('Nombre de la mascota: ')
                if len(nombre)>1:
                    self.__nombre = nombre
                    break
                else:
                    print('Nombre incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
    
    def set_especie(self):
        while True:
            try:
                especie = input('Especie de la mascota (gato, perro...): ')
                if 3 <= len(especie) <= 50:
                    self.__especie = especie
                    break
                else:
                    print('Datos incorrectos. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def set_raza(self):
        while True:
            try:
                raza = input('Raza de la mascota: ')
                if re.match(r'^[A-Za-z\s]{3,30}$', raza):
                    self.__raza = raza
                    break
                else:
                    print('Datos de raza incorrectos. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def set_edad(self):
        while True:
            try:
                pref= input("Preferencias edad a=años, m=meses: ").strip().lower()
                if pref =='a':
                    edad=float(input("Ingrese la edad entre 0 y 70 años: "))
                    edad = float(edad)
                    if edad >= 0 and edad <= 70:
                        self.__edad = edad
                        print(f"Edad establecida correctamente: {self.__edad} años")
                        break
                    else:
                        edad = int(input("Ingrese una edad válida.."))
                if pref =='m':
                    edad=float(input("Ingrese la edad entre 0 y 840 meses: "))
                    edad = float(edad)
                    if edad >= 0 and edad <= 840:
                        self.__edad = edad
                        print(f"Edad establecida correctamente: {self.__edad} meses")
                        break
                    else:
                        edad = int(input("Ingrese una edad válida: "))  
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue 
    
    def set_peso(self):
        while True:
            try:
                peso = float(input('Ingrese el peso de la mascota (en kilogramos): '))
                if 0.1 <= peso <= 100:
                    self.__peso = peso
                    break
                else:
                    print('Peso incorrecto. Intente de nuevo')
            except ValueError:
                print('El peso debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def set_id_usuario(self):
        while True:
            try:
                id_usuario = int(input('Ingrese el numero de identificación del dueño: '))
                if (0 <= id_usuario<= 1000000000):
                    self.__id_usuario = id_usuario
                    break
                else:
                    print('Usuario no válido')
            except ValueError:
                print('Solo se admiten números')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue    
    
    def agregar_historial_medico(self, entrada: str):
        self.__historial_medico.append(entrada)

    def capturar_datos(self):
        self.set_nombre()
        self.set_especie()
        self.set_raza()
        self.set_edad()
        self.set_peso()
        self.set_id_usuario()

    def registrar_mascota(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('CrearMascota', [
                    self.get_nombre(),
                    self.get_especie(),
                    self.get_raza(),
                    self.get_edad(),
                    self.get_peso(),
                    self.get_id_usuario()
                ])
                conexion.commit()
                print('Mascota registrada correctamente...')
                print('\n Datos de la mascota registrados:')
                print('------------------------------------------')
                print(f'  Nombre: {self.get_nombre()}')
                print(f'  Especie: {self.get_especie()}')
                print(f'  Raza: {self.get_raza()}')
                print(f'  Edad: {self.get_edad()}')
                print(f'  Peso: {self.get_peso()}')
                print(f'  Id_usuario: {self.get_id_usuario()}\n')
            except Exception as e:
                print(f'Error al registrar la mascota: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
    
    def mostrar_todas_las_mascotas(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('MostrarTodasLasMascotas')  # Asumiendo que tienes un procedimiento para mostrar todas las mascotas
                print('Listado de todas las mascotas completado.')
                mascota_encontrada = False
                for result in cursor_mascota.stored_results():
                    filas = result.fetchall()
                    if filas:
                        mascota_encontrada = True
                        for datos in filas:
                            print('Resultado:')
                            print('****************************************************************************************************')
                            print("\033[;36m" +
                                f"| Codigo          :{datos[0]:<20}   | Nombre           :{datos[1]}  \n" +
                                f"| Especie         :{datos[2]:<20}   | Raza             :{datos[3]}  \n" +
                                f"| Edad            :{datos[4]:<20}   | Peso             :{datos[5]}  \n" +
                                f"| Id_usuario      :{datos[6]:<20}  "
                                '\033[0;m')
                            print('****************************************************************************************************')
                    else:
                        print('No se encontraron resultados.')
                if not mascota_encontrada:
                    print("No se encontró el servicio proporcionado.")
            except Exception as e:
                print(f'Error al buscar servicio: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    def buscar_mascota_codigo(self, codigo_mascota=None):
        if codigo_mascota is None:
            self.get_codigo()
            codigo_mascota = self.__codigo
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('BuscarMascotaCodigo', [codigo_mascota])
                print('Búsqueda de mascota completada.')
                mascota_encontrada = False
                for result in cursor_mascota.stored_results():
                    fila = result.fetchone()
                    if fila:
                        mascota_encontrada = True
                        while fila is not None:
                            print('Resultado:') # Si encontró  datos los imprime
                            print('**********************************************************************************************')
                            print("\033[;36m" +
                                    f"| Codigo          :{fila[0]:<20}   | Nombre           :{fila[1]}  \n" +
                                    f"| Especie         :{fila[2]:<20}   | Raza             :{fila[3]}  \n" +
                                    f"| Edad            :{fila[4]:<20}   | Peso             :{fila[5]}  \n" +
                                    f"| Id_usuario      :{fila[6]:<20}  "
                                    '\033[0;m')
                            print('**********************************************************************************************')
                            return fila
                        fila = result.fetchall()
                if not mascota_encontrada:
                    print("No se encontraron mascotas para el código proporcionado.")
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                BaseDatos.desconectar()
        return None
    
    def buscar_mascota_nombre(self, nombre_mascota=None):
        if nombre_mascota is None:
            self.set_nombre()
            nombre_mascota = self.__nombre
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('BuscarMascotaNombre', [nombre_mascota])
                print('Búsqueda de mascota completada.')
                mascota_encontrada = False
                for result in cursor_mascota.stored_results():
                    filas = result.fetchall()
                    if filas:
                        mascota_encontrada = True
                        for datos in filas:
                            print('Resultado:')
                            print('****************************************************************************************************')
                            print("\033[;36m" +
                                f"| Codigo          :{datos[0]:<20}   | Nombre           :{datos[1]}  \n" +
                                f"| Especie         :{datos[2]:<20}   | Raza             :{datos[3]}  \n" +
                                f"| Edad            :{datos[4]:<20}   | Peso             :{datos[5]}  \n" +
                                f"| Id_usuario      :{datos[6]:<20}  "
                                '\033[0;m')
                            print('****************************************************************************************************')
                    else:
                        print('No se encontraron resultados.')
                if not mascota_encontrada:
                    print("No se encontró la mascota proporcionada.")
            except Exception as e:
                print(f'Error al buscar mascota: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    def actualizar_mascota(self, codigo_mascota):
        mascota_encontrada = self.buscar_mascota_codigo(codigo_mascota)
        if mascota_encontrada:
            print('\nEscriba los nuevos datos de la mascota:')
            print('------------------------------------------')
            self.set_nombre()
            self.set_especie()
            self.set_raza()
            self.set_edad()
            self.set_peso()
            self.set_id_usuario()
            
            nuevo_nombre = self.get_nombre()
            nueva_especie = self.get_especie()
            nueva_raza = self.get_raza()
            nueva_edad = self.get_edad()
            nuevo_peso = self.get_peso()
            nuevo_id_usuario = self.get_id_usuario()

            print('\n Datos de la mascota actualizados:')
            print('------------------------------------------')
            print(f'  Código: {codigo_mascota}')
            print(f'  Nuevo nombre: {nuevo_nombre}')
            print(f'  Nueva especie: {nueva_especie}')
            print(f'  Nueva raza: {nueva_raza}')
            print(f'  Nueva edad: {nueva_edad}')
            print(f'  Nuevo peso: {nuevo_peso}')
            print(f'  Nuevo id_usuario: {nuevo_id_usuario}\n')

            conexion = BaseDatos.conectar()
            if conexion:
                try:
                    cursor_mascota = conexion.cursor()
                    cursor_mascota.callproc('ActualizarMascota', [
                        codigo_mascota,
                        nuevo_nombre,
                        nueva_especie,
                        nueva_raza,
                        nueva_edad,
                        nuevo_peso,
                        nuevo_id_usuario
                    ])
                    conexion.commit()
                    cursor_mascota.close()
                    print('Mascota actualizada')
                except Exception as error:
                    print(f'Error al actualizar la mascota: {error}. Intente de nuevo')
                finally:
                    BaseDatos.desconectar()
        else:
            print('Mascota no encontrada. Intente otra vez')

    def eliminar_mascota(self, codigo_mascota):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('EliminarMascota', [codigo_mascota])
                conexion.commit()
                print('Mascota borrada correctamente...')
            except Exception as e:
                print(f'Error al eliminar la mascota: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()       
