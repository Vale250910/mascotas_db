import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crud_mascotas.mascota import Mascota
import os
class MenuMascota:
    @staticmethod
    def menu_mascotas():
        while True:
            print('***************MENU MASCOTAS********************')
            print('     1- Registrar nueva mascota')
            print('     2- Mostrar Mascotas (todas)')
            print('     3- Mostrar Mascotas por código')
            print('     4- Mostrar Mascota por nombre')
            print('     5- Actualizar mascota')
            print('     6- Eliminar una mascota')
            print('     7- Salir del sistema')
            print('***************MENU MASCOTAS********************')
            opcion = input('Seleccione una opción: ')
            os.system("pause")
            os.system("cls")
            if opcion == '7':
                print('Gracias por usar nuestra app..')
                os.system("pause")
                os.system("cls")
                break
                
            elif opcion == '1':
                
                print('            1. Registrar Mascota -->')
                print('****************************************************************')
                mascota1 = Mascota()
                mascota1.registrar_mascota()
                os.system("pause")
                os.system("cls")
                
            elif opcion == '2':
                
                print('           2. Mostrar Mascotas (todas) -->')
                print('****************************************************************')
                mascota1 = Mascota()
                mascota1.mostrar_todas_las_mascotas()
                os.system("pause")
                os.system("cls")

            
            elif opcion == '3':
                
                print('          3. Mostrar Mascota por código -->')
                print('****************************************************************')
                codigo_mascota = int(input('Ingrese el código de la mascota: '))
                mascota1 = Mascota()
                mascota1.buscar_mascota_codigo(codigo_mascota)
                os.system("pause")
                os.system("cls")

            elif opcion == '4':
                
                print('          4. Mostrar Mascota por nombre -->')
                print('****************************************************************')
                nombre = input('Ingrese el nombre de la mascota: ')
                mascota1 = Mascota()
                mascota1.buscar_mascota_nombre(nombre)
                os.system("pause")
                os.system("cls")  
            
            elif opcion == '5':
                
                print('            5. Menú Actualizar -->')
                print('****************************************************************')
                codigo_mascota = int(input('Ingrese el código de la mascota: '))
                mascota1 = Mascota()
                mascota1.actualizar_mascota(codigo_mascota)
                os.system("pause")
                os.system("cls")
                
            elif opcion == '6':
                print('           6. Menú Eliminar -->') 
                print('****************************************************************')
                codigo_mascota = int(input('Ingrese el código de la mascota: '))
                mascota1 = Mascota()
                mascota1.eliminar_mascota(codigo_mascota)
                os.system("pause")
                os.system("cls")
                
            
            else:
                print('Opción no válida. Intente de nuevo')

if __name__ == "__main__":
    MenuMascota.menu_mascotas()