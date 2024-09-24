import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crud_veterinarios.veterinario import Veterinario
import os
class MenuVeterinario:
    @staticmethod
    def menu_veterinario():
        while True:
            print('*************** MENU VETERINARIOS ********************')
            print('    1- Registrar nuevo veterinario')
            print('    2- Consultar veterinarios')
            print('    3- Consultar veterinario por Numero de Documento')
            print('    4- Consultar veterinario por nombre')
            print('    5- Activar o Inactivar veterinario')
            print('    6- Actualizar un veterinario')
            print('    7- Eliminar un veterinario')
            print('    8- Salir del sistema')
            print('*************** MENU VETERINARIOS ********************')
            opcion = input('Seleccione una opción: ')
            os.system("pause")
            os.system("cls")
            if opcion == '8':
                print('Gracias por usar nuestra app..')
                os.system("pause")
                os.system("cls")
                break
                
            elif opcion == '1':
                
                print('     1. Registrar Veterinario -->')
                print('****************************************************************')
                veterinario1 = Veterinario()  
                veterinario1.registrar_veterinarios()
                
                os.system("pause")
                os.system("cls")
            
            elif opcion == '2':
                
                print('    2. Mostrar Todos Los Veterinarios -->')
                print('****************************************************************')
                veterinario1 = Veterinario() 
                veterinario1.consultar_veterinarios()
                
                os.system("pause")
                os.system("cls")
            
            elif opcion == '3':
                
                print('    3. Consultar Veterinario Por ID -->')
                print('****************************************************************')
                n_documento= input("Escriba el numero documento del veterinario a buscar: ")
                veterinario1 = Veterinario() 
                veterinario1.buscar_veterinario_id(n_documento)
                
                os.system("pause")
                os.system("cls")
            
            elif opcion == '4':
                
                print('   4. Consultar Veterinario Por Nombre -->')
                print('****************************************************************')
                nombre= input("Nombre del administrador a buscar: ")
                veterinario1 = Veterinario() 
                veterinario1.buscar_veterinario_nombre(nombre)
                
                os.system("pause")
                os.system("cls")
            
            elif opcion == '5':

                print('   5. Activar  o Inactivar Veterinario  -->')
                print('****************************************************************')
                n_documento = input('Ingrese el numero documento del veterinario a activar o inactivar: ')
                veterinario1 = Veterinario() 
                veterinario1.actualizar_estado_administrador(n_documento)
                os.system("pause")
                os.system("cls")
            
            elif opcion == '6':
                
                print('   6. Actualizar Veterinario -->')
                print('****************************************************************')
                n_documento = input('Ingrese el numero documento del veterinario a actualizar: ')
                veterinario1 = Veterinario() 
                veterinario1.actualizar_veterinario(n_documento)
                os.system("pause")
                os.system("cls")
            
            elif opcion == '7':
                
                print('    7. Eliminar Veterinario -->')
                print('****************************************************************')
                n_documento= input('Ingrese el id del veterinario a eliminar: ')
                veterinario1 = Veterinario() 
                veterinario1.eliminar_veterinario(n_documento)
                
                os.system("pause")
                os.system("cls")
if __name__ == "__main__":
    MenuVeterinario.menu_veterinario()