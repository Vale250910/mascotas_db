import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crud_citas.citas import Citas
import os
class MenuCitas:
    @staticmethod
    def menu_citas():
        while True:
            print('*************** MENU CITAS MEDICAS ********************')
            print('         1- Registrar nuevo cita ')
            print('         2- Consultar cita por fecha ')
            print('         3- Consultar cita por codigo ')
            print('         4- Buscar citas ')
            print('         5- Actualizar cita por codigo')
            print('         6- Eliminar cita por codigo')
            print('         7- Salir')
            print('*************** MENU CITAS MEDICAS ********************')
            opcion = input('Seleccione una opción: ')
            os.system("pause")
            os.system("cls")
            if opcion == '7':
                print('Gracias por usar nuestra app..')
                os.system("pause")
                os.system("cls")
                break
                
            elif opcion == '1':
                
                print('         1. Registrar Cita -->')
                print('****************************************************************')
                citas1 = Citas()
                citas1.guardar_cita()
                os.system("pause")
                os.system("cls")
            
            elif opcion == '2':
                print('         2. Consultar Cita Por Fecha -->')
                print('****************************************************************')
                cita1 = Citas()
                cita1.buscar_cita_fecha()
                os.system("pause")
                os.system("cls")
            
            elif opcion == '3':
                print('         3. Consultar Cita Por Codigo  -->')
                print('****************************************************************')
                codigo= int(input('Ingrese el codigo de la cita que desea buscar:'))
                cita1 = Citas()
                cita1.buscar_cita_id(codigo)
                os.system("pause")
                os.system("cls")
            
            elif opcion == '4':
                
                print('         4. Buscar Citas -->')
                print('****************************************************************')
                cita1 = Citas()
                cita1.buscar_citas()
                os.system("pause")
                os.system("cls")
            
            elif opcion == '5':
                print('         5. Actualizar Cita Por Codigo -->')
                print('****************************************************************')
                codigo= int(input('Ingrese el codigo de la cita que desea actualizar:'))
                cita1 = Citas()
                cita1.actualizar_cita(codigo)
                os.system("pause")
                os.system("cls")
            
            elif opcion == '6':
                
                print('         6. Eliminar Cita  Por Codigo -->')
                print('****************************************************************')
                codigo= int(input('Ingrese el codigo de la cita que desea eliminar:'))
                cita1 = Citas()
                cita1.eliminar_cita(codigo)
                os.system("pause")
                os.system("cls")
            

if __name__ == "__main__":
    MenuCitas.menu_citas()