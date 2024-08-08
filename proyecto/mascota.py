#from historial_medico import HistorialMedico
from conexion10 import BaseDatos
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
            usuario: int = None,
            historial_medico= None
            ):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__usuario = usuario
        self.__historial_medico = historial_medico if historial_medico is not None else []

    # GET y SET

    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self):
        while True:
            try:
                codigo_mascota = int(input('Escriba el código de la mascota: '))
                if (1 <= codigo_mascota <= 1000000000):
                    self.__codigo = codigo_mascota
                    break
                else:
                    print('El número debe estar entre 0 y 100000000')
            except ValueError:
                print('El código debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue
 
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self):
        while True:
            try:
                nombre = input('Nombre de la mascota: ')
                if len(nombre)>3:
                    self.__nombre = nombre
                    break
                else:
                    print('Nombre incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue

    def get_especie(self):
        return self.__especie

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

    def get_raza(self):
        return self.__raza

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

    def get_edad(self):
        return self.__edad

    def set_edad(self):
        while True:
            try:
                edad = float(input('Edad de la mascota (años): '))
                if 0 <= edad <= 80.0:
                    self.__edad = edad
                    break
                else:
                    print('Edad no válida')
            except ValueError:
                print('Edad acepta solo números.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue                

    def get_peso(self):
        return self.__peso

    def set_peso(self):
        while True:
            try:
                peso = float(input('Peso en kg: '))
                if (0.1 <= peso <= 1000.0):
                    self.__peso = peso
                    break
                else:
                    print('Peso no válido')
            except ValueError:
                print('El peso acepta solo números')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue                 

    def get_usuario(self):
        return self.__usuario

    def set_usuario(self):
        while True:
            try:
                usuario = int(input('Id usuario: '))
                if (0 <= usuario <= 1000000000):
                    self.__usuario = usuario
                    break
                else:
                    print('Usuario no válido')
            except ValueError:
                print('Solo se admiten números')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue    

    def get_historial(self):
        return self.__historial
    
    def agregar_historial_medico(self, entrada: str):
        self.__historial_medico.append(entrada)

    def capturar_datos(self):
        self.set_codigo()
        self.set_nombre()
        self.set_especie()
        self.set_raza()
        self.set_edad()
        self.set_peso()
        self.set_usuario()

    def registrar_mascota(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('CrearMascota', [
                    self.__codigo,
                    self.__nombre,
                    self.__especie,
                    self.__raza,
                    self.__edad,
                    self.__peso,
                    self.__usuario
                ])
                conexion.commit()
                print('Mascota registrada correctamente...')
            except Exception as e:
                print(f'Error al registrar la mascota: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
    
    def buscar_mascota(self, codigo_mascota=None):
        if codigo_mascota is None:
            self.set_codigo()
            codigo_mascota = self.__codigo

        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('BuscarMascota', [codigo_mascota])
                print('Búsqueda de mascota completada.')
                for result in cursor_mascota.stored_results():
                    fila = result.fetchone()
                    while fila is not None:
                        print('Resultado:') # Si encontró  datos los imprime
                        print('************************************************************************************************')
                        print("\033[;36m"+f"Codigo:{fila[0]}, Nombre:{fila[1]}, Especie:{fila[2]}, Raza:{fila[3]}, Edad:{fila[4]}, Peso:{fila[5]}, Id_usuario:{fila[6]}"+'\033[0;m')
                        print('*************************************************************************************************')
                        return fila
                    fila = result.fetchone()
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                BaseDatos.desconectar()
        return None

    def actualizar_mascota(self, codigo_mascota):
        mascota_encontrada = self.buscar_mascota(codigo_mascota)
        if mascota_encontrada:
            print('Escriba los nuevos datos de la mascota:')
            self.set_nombre()
            self.set_especie()
            self.set_raza()
            self.set_edad()
            self.set_peso()
            
            nuevo_nombre = self.get_nombre()
            nueva_especie = self.get_especie()
            nueva_raza = self.get_raza()
            nueva_edad = self.get_edad()
            nuevo_peso = self.get_peso()
            
            print(f'Código: {codigo_mascota}')
            print(f'Nuevo nombre: {nuevo_nombre}')
            print(f'Nueva especie: {nueva_especie}')
            print(f'Nueva raza: {nueva_raza}')
            print(f'Nueva edad: {nueva_edad}')
            print(f'Nuevo peso: {nuevo_peso}')

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
                        nuevo_peso
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
