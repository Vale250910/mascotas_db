from citas import Citas
import os
class MenuCitas:
    def menu_citas():
        while True:
            print('*************** MENU CITAS MEDICAS ********************')
            print('         1- Registrar nuevo cita ')
            print('         2- Consultar cita por fecha ')
            print('         3- Consultar cita por  codigo mascota ')
            print('         4- Buscar citas ')
            print('         5- Eliminar cita ')
            print('         6- Salir')
            print('*************** MENU CITAS MEDICAS ********************')
            opcion = input('Seleccione una opción: ')
            os.system("pause")
            os.system("cls")
            if opcion == '6':
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
                print('         3. Consultar Cita Por Codigo Mascota -->')
                print('****************************************************************')
                cita1 = Citas()
                cita1.buscar_cita_mascota()
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
                
                print('         5. Eliminar Cita -->')
                print('****************************************************************')
                cita1 = Citas()
                cita1.eliminar_cita()
                os.system("pause")
                os.system("cls")
            

if __name__ == "__main__":
    MenuCitas.menu_citas()