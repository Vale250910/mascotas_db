from propietario import Propietario
import os

class MenuPropietario:
    @staticmethod
    def menu_propietario():
        while True:
            print('*************** MENU PROPIETARIOS ********************')
            print('    1- Registrar nuevo propietario')
            print('    2- Consultar propietarios')
            print('    3- Consultar propietario por ID')
            print('    4- Consultar propietario por nombre')
            print('    5- Actualizar un propietario')
            print('    6- Eliminar un propietario')
            print('    7- Salir del sistema')
            print('*************** MENU PROPIETARIOS ********************')
            opcion = input('Seleccione una opción: ')
            os.system("pause")
            os.system("cls")
            if opcion == '7':
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
                
                print('    3. Consultar Propietario Por ID  -->')
                print('****************************************************************')
                id_usuario= input("Escriba el id del propietario a buscar: ")
                propietario1 = Propietario()
                propietario1.buscar_propietario_id(id_usuario)
                
                os.system("pause")
                os.system("cls")
            
            elif opcion == '4':
                
                print('   4. Consultar Propietario Por Nombre  -->')
                print('****************************************************************')
                propietario1 = Propietario()
                propietario1.buscar_propietario_nombre()
                
                os.system("pause")
                os.system("cls")
            
            elif opcion == '5':
                
                print('   5. Actualizar Propietario  -->')
                print('****************************************************************')
                id_usuario = int(input('Ingrese el id del propietario a actualizar: '))
                propietario1 = Propietario()
                propietario1.actualizar_propietario(id_usuario)
                os.system("pause")
                os.system("cls")
            
            elif opcion == '6':
                
                print('    6. Eliminar Propietario  -->')
                print('****************************************************************')
                id_usuario= int(input('Ingrese el id del propietario a eliminar: '))
                propietario1 = Propietario()
                propietario1.eliminar_propietario(id_usuario)
                
                os.system("pause")
                os.system("cls")
if __name__ == "__main__":
    MenuPropietario.menu_propietario() 