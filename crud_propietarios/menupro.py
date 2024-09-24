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
<<<<<<< HEAD
            print('    3- Consultar propietario por N. Documento')
            print('    4- Consultar propietario por nombre')
            print('    5- Activar  o Inactivar propietario')
            print('    6- Actualizar un propietario')
            print('    7- Eliminar un propietario')
            print('    8- Salir del sistema')
=======
            print('    3- Consultar propietario por ID')
            print('    4- Consultar propietario por nombre')
            print('    5- Actualizar un propietario')
            print('    6- Eliminar un propietario')
            print('    7- Salir del sistema')
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
            print('*************** MENU PROPIETARIOS ********************')
            opcion = input('Seleccione una opción: ')
            os.system("pause")
            os.system("cls")
<<<<<<< HEAD
            if opcion == '8':
=======
            if opcion == '7':
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                print('Gracias por usar nuestra app..')
                os.system("pause")
                os.system("cls")
                break
                
            elif opcion == '1':
<<<<<<< HEAD
=======
                
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
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
                
<<<<<<< HEAD
                print('    3. Consultar Propietario Por N. Documento -->')
                print('****************************************************************')
                n_documento= input("Escriba el numero de documento a buscar: ")
                propietario1 = Propietario()
                propietario1.buscar_propietario_id(n_documento)
=======
                print('    3. Consultar Propietario Por ID  -->')
                print('****************************************************************')
                id_usuario= input("Escriba el id del propietario a buscar: ")
                propietario1 = Propietario()
                propietario1.buscar_propietario_id(id_usuario)
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                
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
                
<<<<<<< HEAD
                print('   5. Activar  o Inactivar Propietario  -->')
                print('****************************************************************')
                propietario1 = Propietario()
                propietario1.actualizar_estado_propietario()
=======
                print('   5. Actualizar Propietario  -->')
                print('****************************************************************')
                id_usuario = int(input('Ingrese el id del propietario a actualizar: '))
                propietario1 = Propietario()
                propietario1.actualizar_propietario(id_usuario)
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                os.system("pause")
                os.system("cls")
            
            elif opcion == '6':
                
<<<<<<< HEAD
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
=======
                print('    6. Eliminar Propietario  -->')
                print('****************************************************************')
                id_usuario= int(input('Ingrese el id del propietario a eliminar: '))
                propietario1 = Propietario()
                propietario1.eliminar_propietario(id_usuario)
>>>>>>> 0256cca8fbd656168a9dcc2f6278819dc6a34ad6
                
                os.system("pause")
                os.system("cls")
if __name__ == "__main__":
    MenuPropietario.menu_propietario() 