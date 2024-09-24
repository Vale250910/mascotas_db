import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crud_propietarios.propietario import Propietario
import os

class MenuPropietario:
    @staticmethod
    def menu_propietario():
        while True:
            print('*************** MENU PROPIETARIOS ********************')
            print('    1- Registrar nuevo propietario')
            print('    2- Consultar propietarios')
            print('    3- Consultar propietario por N. Documento')
            print('    4- Consultar propietario por nombre')
            print('    5- Activar  o Inactivar propietario')
            print('    6- Actualizar un propietario')
            print('    7- Eliminar un propietario')
            print('    8- Salir del sistema')
            print('*************** MENU PROPIETARIOS ********************')
            opcion = input('Seleccione una opción: ')
            os.system("pause")
            os.system("cls")
            if opcion == '8':
                print('Gracias por usar nuestra app..')
                os.system("pause")
                os.system("cls")
                break
                
            elif opcion == '1':
                print('     1. Registrar Propietario -->')
                print('****************************************************************')
                propietario1 = Propietario()  
                propietario1.registrar_propietarios()
                
                os.system("pause")
                os.system("cls")
            
            elif opcion == '2':
                
                print('    2. Mostrar Todos Los Propietarios -->')
                print('****************************************************************')
                propietario1 = Propietario()
                propietario1.consultar_propietarios()
                
                os.system("pause")
                os.system("cls")
            
            elif opcion == '3':
                
                print('    3. Consultar Propietario Por N. Documento -->')
                print('****************************************************************')
                n_documento= input("Escriba el numero de documento a buscar: ")
                propietario1 = Propietario()
                propietario1.buscar_propietario_id(n_documento)
                
                os.system("pause")
                os.system("cls")
            
            elif opcion == '4':
                
                print('   4. Consultar Propietario Por Nombre  -->')
                print('****************************************************************')
                nombre= input("Nombre del propietario a buscar: ")
                propietario1 = Propietario()
                propietario1.buscar_propietario_nombre(nombre)
                
                os.system("pause")
                os.system("cls")
            
            elif opcion == '5':
                
                print('   5. Activar  o Inactivar Propietario  -->')
                print('****************************************************************')
                propietario1 = Propietario()
                propietario1.actualizar_estado_propietario()
                os.system("pause")
                os.system("cls")
            
            elif opcion == '6':
                
                print('   6. Actualizar Propietario  -->')
                print('****************************************************************')
                n_documento = input('Ingrese el numero de documento a actualizar: ')
                propietario1 = Propietario()
                propietario1.actualizar_propietario(n_documento)
                os.system("pause")
                os.system("cls")
            
            elif opcion == '7':
                
                print('    7. Eliminar Propietario  -->')
                print('****************************************************************')
                n_documento= input('Ingrese el numero de documento a eliminar: ')
                propietario1 = Propietario()
                propietario1.eliminar_propietario(n_documento)
                
                os.system("pause")
                os.system("cls")
if __name__ == "__main__":
    MenuPropietario.menu_propietario() 