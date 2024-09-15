import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crud_administradores.administrador import Administrador
import os
class MenuAdministrador:
    @staticmethod
    def menu_administrador():
        try:
            while True:
                print('*************** MENU ADMINISTRADORES ********************')
                print('    1- Registrar nuevo administrador')
                print('    2- Consultar administradores')
                print('    3- Consultar administrador por ID')
                print('    4- Consultar administrador por nombre')
                print('    5- Actualizar un administrador por ID')
                print('    6- Eliminar un administrador por ID')
                print('    7- Salir del sistema')
                print('*************** MENU ADMINISTRADORES ********************')
                opcion = input('Seleccione una opción: ')
                os.system("pause")
                os.system("cls")
                if opcion == '7':
                    print('Gracias por usar nuestra app..')
                    os.system("pause")
                    os.system("cls")
                    break
                    
                elif opcion == '1':
                    
                    print('     1. Registrar Administrador -->')
                    print('****************************************************************')
                    administrador1 = Administrador()  
                    administrador1.registrar_administradores()
                    
                    os.system("pause")
                    os.system("cls")
                
                elif opcion == '2':
                    
                    print('    2. Mostrar Todos Los Adminitradores -->')
                    print('****************************************************************')
                    administrador1 = Administrador()  
                    administrador1.consultar_administradores()
                    
                    os.system("pause")
                    os.system("cls")
                
                elif opcion == '3':
                    
                    print('    3. Consultar Administrador Por ID  -->')
                    print('****************************************************************')
                    id_usuario= input("Escriba el id del administrador a buscar: ")
                    administrador1 = Administrador()  
                    administrador1.buscar_administrador_id(id_usuario)
                    
                    os.system("pause")
                    os.system("cls")
                
                elif opcion == '4':
                    
                    print('   4. Consultar Administrador Por Nombre -->')
                    print('****************************************************************')
                    nombre= input("Nombre del administrador a buscar: ")
                    administrador1 = Administrador()  
                    administrador1.buscar_administrador_nombre(nombre)
                    
                    os.system("pause")
                    os.system("cls")
                
                elif opcion == '5':
                    
                    print('   5. Actualizar Administrador Por ID -->')
                    print('****************************************************************')
                    id_usuario = int(input('Ingrese el id del administrador a actualizar: '))
                    administrador1 = Administrador()   
                    administrador1.actualizar_administrador(id_usuario)
                    os.system("pause")
                    os.system("cls")
                
                elif opcion == '6':
                    
                    print('    6. Eliminar Administrador Por ID -->')
                    print('****************************************************************')
                    id_usuario= int(input('Ingrese el id del administrador a eliminar: '))
                    administrador1 = Administrador()  
                    administrador1.eliminar_administrador(id_usuario)
                    
                    os.system("pause")
                    os.system("cls")

        except KeyboardInterrupt:
            print('El usuario ha cancelado la ejecución, por favor continue')
        except Exception as error:
            print(f'Ha ocurrido error no codificado {error}')
        finally:
            print('Intente de nuevo')
if __name__ == "__main__":
    MenuAdministrador.menu_administrador() 