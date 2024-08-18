from servicios import Servicios
import os
class MenuServicios:
    @staticmethod
    def menu_servicio():
        while True:
            print('*************** MENU SERVICIOS ********************')
            print('         1- Registrar nuevo servicios ')
            print('         2- Consultar servicios  ')
            print('         3- Consultar servicios por codigo ')
            print('         4- Consultar servicios por nombre ')
            print('         5- Eliminar servicios ')
            print('         6- Salir')
            print('*************** MENU SERVICIOS ********************')
            opcion = input('Seleccione una opción: ')
            os.system("pause")
            os.system("cls")
            if opcion == '6':
                print('Gracias por usar nuestra app..')
                os.system("pause")
                os.system("cls")
                break
                
            elif opcion == '1':
                
                print('         1. Registrar Servicios -->')
                print('****************************************************************')
                servicio1 = Servicios()
                servicio1.registrar_servicio()
                os.system("pause")
                os.system("cls")
            
            elif opcion == '2':
                print('         2. Consultar Servicios -->')
                print('****************************************************************')
                servicio1 = Servicios()
                servicio1.mostrar_todas_los_servicios()
                os.system("pause")
                os.system("cls")
            
            elif opcion == '3':
                print('         3. Consultar Servicios Por Codigo Mascota -->')
                print('****************************************************************')
                codigo= input("Escriba el id del propietario a buscar: ")
                servicio1 = Servicios()
                servicio1.buscar_servicio_por_codigo(codigo)
                os.system("pause")
                os.system("cls")
            
            elif opcion == '4':
                
                print('         4. Buscar Servicios Por Nombre -->')
                print('****************************************************************')
                nombre= input("Ingrese el nombre que desea buscar: ")
                servicio1 = Servicios()
                servicio1.buscar_servicio_nombre(nombre)
                os.system("pause")
                os.system("cls")
            
            elif opcion == '5':
                
                print('         5. Eliminar Servicios -->')
                print('****************************************************************')
                codigo= input("Escriba el id del propietario a buscar: ")
                servicio1 = Servicios()
                servicio1.eliminar_servicio(codigo)
                os.system("pause")
                os.system("cls")
            

if __name__ == "__main__":
    MenuServicios.menu_servicio()  