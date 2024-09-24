import sys
import os
import re
<<<<<<< HEAD
from base_datos.conexion10 import BaseDatos

# Inicializa Colorama para los colores en la terminal

class Mascota:
    def __init__(self,
                codigo: str = None,
=======
from colorama import init
from base_datos.conexion10 import BaseDatos

# Inicializa Colorama para los colores en la terminal
init()

class Mascota:
    def __init__(self,
                codigo: int = None,
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                nombre: str = None,
                especie: str = None,
                raza: str = None,
                edad: float = None,
                peso: float = None,
<<<<<<< HEAD
                n_documento: str = None,
                estado_acceso: str = None,):

=======
                id_usuario: int = None,
                historial_medico=None):
        """
        Inicializa un objeto Mascota con los atributos proporcionados.
        :param codigo: Código de la mascota.
        :param nombre: Nombre de la mascota.
        :param especie: Especie de la mascota (e.g., perro, gato).
        :param raza: Raza de la mascota.
        :param edad: Edad de la mascota (en años o meses).
        :param peso: Peso de la mascota en kilogramos.
        :param id_usuario: ID del propietario de la mascota.
        :param historial_medico: Lista de historiales médicos de la mascota.
        """
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        self.__codigo = codigo
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
<<<<<<< HEAD
        self.__n_documento = n_documento
        self.__estado_acceso = estado_acceso
        

    # Métodos GET
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
    
    def get_n_documento(self):
        return self.__n_documento
    
    def get_estado_acceso(self):
        return self.__estado_acceso

    # Métodos SET
    def set_codigo(self):
        while True:
            try:
                codigo = input('Ingrese el codigo de la mascota: ').strip()
                if 1<= len(codigo) <= 10000000:
                    self.__codigo = codigo
                    break
                else:
                    print('El codigo debe ser una cadena de 1 a 10000000 dígitos.')
            except KeyboardInterrupt:
                print('\nEl usuario ha cancelado la entrada de datos.')
                return None 
            
    def set_nombre(self):

=======
        self.__id_usuario = id_usuario
        self.__historial_medico = historial_medico if historial_medico is not None else []

    # Métodos GET
    def get_codigo(self):
        """
        Retorna el código de la mascota.
        """
        return self.__codigo

    def get_nombre(self):
        """
        Retorna el nombre de la mascota.
        """
        return self.__nombre
    
    def get_especie(self):
        """
        Retorna la especie de la mascota.
        """
        return self.__especie
    
    def get_raza(self):
        """
        Retorna la raza de la mascota.
        """
        return self.__raza
    
    def get_edad(self):
        """
        Retorna la edad de la mascota.
        """
        return self.__edad
    
    def get_peso(self):
        """
        Retorna el peso de la mascota.
        """
        return self.__peso
    
    def get_id_usuario(self):
        """
        Retorna el ID del propietario de la mascota.
        """
        return self.__id_usuario 
    
    def get_historial(self):
        """
        Retorna el historial médico de la mascota.
        """
        return self.__historial_medico

    # Métodos SET
    def set_nombre(self):
        """
        Solicita al usuario que ingrese el nombre de la mascota y valida la entrada.
        """
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        while True:
            try:
                nombre = input('Nombre de la mascota: ')
                if len(nombre) > 1:
                    self.__nombre = nombre
                    break
                else:
                    print('Nombre incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
    
    def set_especie(self):
<<<<<<< HEAD
=======
        """
        Solicita al usuario que ingrese la especie de la mascota y valida la entrada.
        """
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
=======
        """
        Solicita al usuario que ingrese la raza de la mascota y valida la entrada.
        """
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
=======
        """
        Solicita al usuario que ingrese la edad de la mascota y valida la entrada. La edad puede ser en años o meses.
        """
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        while True:
            try:
                pref = input("Preferencias edad a=años, m=meses: ").strip().lower()
                if pref == 'a':
                    edad = float(input("Ingrese la edad entre 0 y 70 años: "))
                    if 0 <= edad <= 70:
                        self.__edad = edad
                        print(f"Edad establecida correctamente: {self.__edad} años")
                        break
                    else:
                        print("Ingrese una edad válida.")
                elif pref == 'm':
                    edad = float(input("Ingrese la edad entre 0 y 840 meses: "))
                    if 0 <= edad <= 840:
                        self.__edad = edad
                        print(f"Edad establecida correctamente: {self.__edad} meses")
                        break
                    else:
                        print("Ingrese una edad válida.")
                else:
                    print("Preferencia no válida. Intente de nuevo.")
            except ValueError:
                print('La edad debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue 
    
    def set_peso(self):
<<<<<<< HEAD
=======
        """
        Solicita al usuario que ingrese el peso de la mascota y valida la entrada.
        """
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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

<<<<<<< HEAD
    def set_n_documento(self):
        while True:
            try:
                n_documento = input('Ingrese el numero de identificación: ').strip()
                if n_documento.isdigit() and 1 <= len(n_documento) <= 1000000000:
                    self.__n_documento = n_documento
                    break
                else:
                    print('El número de documento debe ser una cadena de 1 a 1000000000 dígitos.')
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

    def capturar_datos(self):
        self.set_codigo()
=======
    def set_id_usuario(self):
        """
        Solicita al usuario que ingrese el ID del propietario y valida la entrada.
        """
        while True:
            try:
                id_usuario = int(input('Ingrese el número de identificación del dueño: '))
                if 0 <= id_usuario <= 1000000000:
                    self.__id_usuario = id_usuario
                    break
                else:
                    print('Usuario no válido')
            except ValueError:
                print('Solo se admiten números.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue    

    def agregar_historial_medico(self, entrada: str):
        """
        Agrega un nuevo historial médico a la lista de historiales médicos de la mascota.

        :param entrada: Información del historial médico.
        """
        self.__historial_medico.append(entrada)

    def capturar_datos(self):
        """
        Captura todos los datos necesarios para registrar una mascota a través de las funciones de entrada.
        """
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        self.set_nombre()
        self.set_especie()
        self.set_raza()
        self.set_edad()
        self.set_peso()
<<<<<<< HEAD
        self.set_n_documento()
        self.set_estado_acceso()

    def registrar_mascota(self):
=======
        self.set_id_usuario()

    def registrar_mascota(self):
        """
        Captura los datos de la mascota y guarda la información en la base de datos.
        """
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('CrearMascota', [
<<<<<<< HEAD
                    self.get_codigo(),  # Este código se genera automáticamente en la base de datos
=======
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                    self.get_nombre(),
                    self.get_especie(),
                    self.get_raza(),
                    self.get_edad(),
                    self.get_peso(),
<<<<<<< HEAD
                    self.get_n_documento(),
                    self.get_estado_acceso()  # Estado de acceso se almacena como un parámetro de entrada al procedimiento almacenado en la base de datos. No es necesario hacer nada en Python para ello.
=======
                    self.get_id_usuario()
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                ])
                conexion.commit()
                print('Mascota registrada correctamente...')
                print('\n Datos de la mascota registrados:')
                print('------------------------------------------')
<<<<<<< HEAD
                print(f'  Codigo: {self.get_codigo()}')
=======
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                print(f'  Nombre: {self.get_nombre()}')
                print(f'  Especie: {self.get_especie()}')
                print(f'  Raza: {self.get_raza()}')
                print(f'  Edad: {self.get_edad()}')
                print(f'  Peso: {self.get_peso()}')
<<<<<<< HEAD
                print(f'  Numero documento: {self.get_n_documento()}')
                print(f'  Estado acceso: {self.get_estado_acceso()}')
=======
                print(f'  Id_usuario: {self.get_id_usuario()}\n')
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
            except Exception as e:
                print(f'Error al registrar la mascota: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
    
    def mostrar_todas_las_mascotas(self):
<<<<<<< HEAD
=======
        """
        Muestra todas las mascotas almacenadas en la base de datos.
        """
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
                                f"| Codigo           :{datos[0]:<20}   | Nombre           :{datos[1]}  \n" +
                                f"| Especie          :{datos[2]:<20}   | Raza             :{datos[3]}  \n" +
                                f"| Edad             :{datos[4]:<20}   | Peso             :{datos[5]}  \n" +
                                f"| Numero Documento :{datos[6]:<20}   | Estado Acceso    :{datos[7]} \n" +
                                '\033[0;m')
                            print('***************************************************************************************************')
                    else:
                        print('No se encontraron resultados.')
                if not mascota_encontrada:
                    print("No se encontró el servicio proporcionado no existe o esta inactivo.")
=======
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
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
            except Exception as e:
                print(f'Error al buscar servicio: {e}')
            finally:
                BaseDatos.desconectar()
        return None

<<<<<<< HEAD
    def buscar_mascota_codigo(self,codigo=None):
        if codigo is None:
            self.get_codigo()
            codigo = self.__codigo
=======
    def buscar_mascota_codigo(self, codigo_mascota=None):
        """
        Busca una mascota en la base de datos por su código.
        :param codigo_mascota: Código de la mascota a buscar. Si no se proporciona, usa el código de la instancia.
        :return: Datos de la mascota si se encuentra; de lo contrario, None.
        """
        if codigo_mascota is None:
            self.get_codigo()
            codigo_mascota = self.__codigo
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
<<<<<<< HEAD
                cursor_mascota.callproc('BuscarMascotaCodigo', [codigo])
=======
                cursor_mascota.callproc('BuscarMascotaCodigo', [codigo_mascota])
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                print('Búsqueda de mascota completada.')
                mascota_encontrada = False
                for result in cursor_mascota.stored_results():
                    fila = result.fetchone()
                    if fila:
                        mascota_encontrada = True
                        print('Resultado:')
                        print('**********************************************************************************************')
                        print("\033[;36m" +
<<<<<<< HEAD
                                f"| Codigo           :{fila[0]:<20}   | Nombre           :{fila[1]}  \n" +
                                f"| Especie          :{fila[2]:<20}   | Raza             :{fila[3]}  \n" +
                                f"| Edad             :{fila[4]:<20}   | Peso             :{fila[5]}  \n" +
                                f"| Numero documento :{fila[6]:<20}   | Estado acceso    :{fila[7]} \n" +
=======
                                f"| Codigo          :{fila[0]:<20}   | Nombre           :{fila[1]}  \n" +
                                f"| Especie         :{fila[2]:<20}   | Raza             :{fila[3]}  \n" +
                                f"| Edad            :{fila[4]:<20}   | Peso             :{fila[5]}  \n" +
                                f"| Id_usuario      :{fila[6]:<20}  "
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                                '\033[0;m')
                        print('**********************************************************************************************')
                        return fila
                    fila = result.fetchall()
                if not mascota_encontrada:
<<<<<<< HEAD
                    print("No se encontraron mascotas para el código proporcionado no existe o esta inactivo.")
=======
                    print("No se encontraron mascotas para el código proporcionado.")
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                BaseDatos.desconectar()
        return None
    
    def buscar_mascota_nombre(self, nombre_mascota=None):
<<<<<<< HEAD
=======
        """
        Busca una mascota en la base de datos por su nombre.
        :param nombre_mascota: Nombre de la mascota a buscar. Si no se proporciona, solicita el nombre.
        :return: Datos de la mascota si se encuentra; de lo contrario, None.
        """
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
<<<<<<< HEAD
                                f"| Codigo           :{datos[0]:<20}   | Nombre           :{datos[1]}  \n" +
                                f"| Especie          :{datos[2]:<20}   | Raza             :{datos[3]}  \n" +
                                f"| Edad             :{datos[4]:<20}   | Peso             :{datos[5]}  \n" +
                                f"| Numero Documento :{datos[6]:<20}   | Estado Acceso    :{datos[7]} \n" +
                                '\033[0;m')
                            print('****************************************************************************************************')
                    else:
                        print('No se encontraron resultados no existe o esta inactivo."')
=======
                                f"| Codigo          :{datos[0]:<20}   | Nombre           :{datos[1]}  \n" +
                                f"| Especie         :{datos[2]:<20}   | Raza             :{datos[3]}  \n" +
                                f"| Edad            :{datos[4]:<20}   | Peso             :{datos[5]}  \n" +
                                f"| Id_usuario      :{datos[6]:<20}  "
                                '\033[0;m')
                            print('****************************************************************************************************')
                    else:
                        print('No se encontraron resultados.')
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                if not mascota_encontrada:
                    print("No se encontró la mascota proporcionada.")
            except Exception as e:
                print(f'Error al buscar mascota: {e}')
            finally:
                BaseDatos.desconectar()
        return None
<<<<<<< HEAD
    
    def actualizar_estado_mascota(self, codigo=None, nuevo_estado_acceso=None):
        if codigo is None:
            self.set_codigo()  
            codigo = self.get_codigo()
            
        if nuevo_estado_acceso is None:
            self.set_estado_acceso()
            nuevo_estado_acceso = self.get_estado_acceso()  
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()  
                cursor_mascota.callproc('ActualizarEstadoMascotas', (codigo, nuevo_estado_acceso))
                for result in cursor_mascota.stored_results():
                    filas = result.fetchall()
                    if filas:
                        for fila in filas:
                            print('**********************************************************************************************')
                            print(f'Codigo: {fila[0]},  Nombre: {fila[1]} Estado: {fila[2]}')
                            print('**********************************************************************************************')
                    else:
                        print(f'No se encontraron resultados para el documento {codigo}.')
                conexion.commit()
                print(f'Estado de acceso actualizado a {nuevo_estado_acceso} para la mascota con codigo {codigo}.')
            except Exception as e:
                print(f'Error al actualizar el estado: {e}')
            finally:
                BaseDatos.desconectar()  
        else:
            print('No se pudo establecer la conexión con la base de datos.')

    def actualizar_mascota(self, codigo_mascota):
=======

    def actualizar_mascota(self, codigo_mascota):
        """
        Actualiza los datos de una mascota existente en la base de datos.
        :param codigo_mascota: Código de la mascota a actualizar.
        """
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
        mascota_encontrada = self.buscar_mascota_codigo(codigo_mascota)
        if mascota_encontrada:
            print('\nEscriba los nuevos datos de la mascota:')
            print('------------------------------------------')
            self.set_nombre()
            self.set_especie()
            self.set_raza()
            self.set_edad()
            self.set_peso()
<<<<<<< HEAD
            self.set_n_documento()
=======
            self.set_id_usuario()
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
            
            nuevo_nombre = self.get_nombre()
            nueva_especie = self.get_especie()
            nueva_raza = self.get_raza()
            nueva_edad = self.get_edad()
            nuevo_peso = self.get_peso()
<<<<<<< HEAD
            nuevo_n_documeto = self.get_n_documento()
=======
            nuevo_id_usuario = self.get_id_usuario()
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6

            print('\n Datos de la mascota actualizados:')
            print('------------------------------------------')
            print(f'  Código: {codigo_mascota}')
            print(f'  Nuevo nombre: {nuevo_nombre}')
            print(f'  Nueva especie: {nueva_especie}')
            print(f'  Nueva raza: {nueva_raza}')
            print(f'  Nueva edad: {nueva_edad}')
            print(f'  Nuevo peso: {nuevo_peso}')
<<<<<<< HEAD
            print(f'  Nuevo numero documeto: {nuevo_n_documeto}\n')
=======
            print(f'  Nuevo id_usuario: {nuevo_id_usuario}\n')
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6

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
<<<<<<< HEAD
                        nuevo_n_documeto
=======
                        nuevo_id_usuario
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                    ])
                    conexion.commit()
                    cursor_mascota.close()
                    print('Mascota actualizada')
                except Exception as error:
                    print(f'Error al actualizar la mascota: {error}. Intente de nuevo')
                finally:
                    BaseDatos.desconectar()
        else:
<<<<<<< HEAD
            print('Mascota no encontrada. Asegúrese de que el código ingresado sea correcto o que la mascota esté activa. Intente nuevamente.')

    def eliminar_mascota(self, codigo_mascota):
=======
            print('Mascota no encontrada. Intente otra vez')

    def eliminar_mascota(self, codigo_mascota):
        """
        Elimina una mascota de la base de datos usando su código.
        :param codigo_mascota: Código de la mascota a eliminar.
        """
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
