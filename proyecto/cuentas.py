from conexion10 import BaseDatos
class Cuenta:
    
    def __init__(
            self,
            numero_cuenta: int = None,
            tipo: str= None,
            saldo: int= None,
            id_cuentahabiente: int= None,
           
            ):
        self.__numero_cuenta = numero_cuenta
        self.__tipo = tipo
        self.__saldo = saldo
        self.__id_cuentahabiente = id_cuentahabiente
    
    def get_numero_cuenta(self):
        return self.__numero_cuenta
    
    def get_tipo(self):
        return self.__tipo
    
    def get_saldo(self):
        return self.__saldo
    
    def get_id_cuentahabiente(self):
        return self.__id_cuentahabiente
    
    def set_numero_cuenta(self):
        while True:
            try:
                numero_cuenta = int(input('Escriba el numero de la cuenta : '))
                if 1 <= numero_cuenta <= 1000000000:
                    self.__numero_cuenta = numero_cuenta
                    break
                else:
                    print('El número debe estar entre 1 y 1000000000')
            except ValueError:
                print('El numero de cuenta debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue
    
    def set_tipo(self):
        while True:
            try:
                tipo= input('Escriba el tipo  de la cuenta (AHORROS,CORRIENTE): ').lower()
                if tipo in ['ahorros','corriente']:  # Corregido el espacio extra
                    self.__tipo = tipo
                    break
                else:
                    print('El tipo debe ser AHORROS , CORRIENTE.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')

    def set_saldo(self):
        while True:
            try:
                saldo = int(input('Escriba el saldo de la cuenta : '))
                if 1 <= saldo <= 1000000000:
                    self.__saldo = saldo
                    break
                else:
                    print('El saldo debe estar entre 1 y 1000000000')
            except ValueError:
                print('El saldo debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue
        
    def set_id_cuentahabiente(self):
        while True:
            try:
                id_cuentahabiente = int(input('Escriba el id de la cuenta habiente  : '))
                if 1 <= id_cuentahabiente <= 1000000000:
                    self.__id_cuentahabiente = id_cuentahabiente
                    break
                else:
                    print('La cuenta habiente debe estar entre 1 y 1000000000')
            except ValueError:
                print('La cuentahabiente debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue
    
    def capturar_datos(self):
        self.set_numero_cuenta()
        self.set_tipo()
        self.set_saldo()
        self.set_id_cuentahabiente()
      

    def guardar_cuenta(self):
        self.capturar_datos()
        
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('InsertarCuenta', [
                    self.__numero_cuenta,
                    self.__tipo,
                    self.__saldo,
                    self.__id_cuentahabiente
                   
                ])
                conexion.commit()
                print('Cuenta registrada correctamente...')
            except Exception as e:
                print(f'Error al registrar la cuenta: {e}')
                conexion.rollback()
            finally:
                BaseDatos.desconectar()
    
    def buscar_cuenta_codigo(self, numero_cuenta=None):
        if numero_cuenta is None:
            self.set_numero_cuenta()
            numero_cuenta = self.__numero_cuenta

        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cuenta = conexion.cursor()
                cursor_cuenta.callproc('BuscarCuenta', [numero_cuenta])
                print('Búsqueda de cuenta completada.')
                for result in cursor_cuenta.stored_results():
                    fila = result.fetchone()
                    while fila is not None:
                        print('Resultado:') # Si encontró  datos los imprime
                        print('**********************************************************************************************')
                        print("\033[;36m" +
                                f"| Numero Cuenta        :{fila[0]:<20}   | Tipo                   :{fila[1]}  \n" +
                                f"| Saldo                :{fila[2]:<20}   | Cuenta Habiente        :{fila[3]}  \n" +
                                '\033[0;m')
                        print('**********************************************************************************************')
                        return fila
            except Exception as e:
                print(f'Error al buscar la cuenta: {e}')
            finally:
                BaseDatos.desconectar()
        return None