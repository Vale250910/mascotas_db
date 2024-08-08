from mascota import Mascota
import os
def main():
    while True:
        print('***************MENU MASCOTAS********************')
        print('1- Registrar nueva mascota')
        print('2- Consultar una mascota')
        print('3- Actualizar mascota')
        print('4- Eliminar una mascota')
        print('5- Salir del sistema')
        print('***************MENU MASCOTAS********************')
        opcion = input('Seleccione una opción: ')
        os.system("pause")
        os.system("cls")
        if opcion == '5':
            print('Gracias por usar nuestra app..')
            os.system("pause")
            os.system("cls")
            break
            
        elif opcion == '1':
            
            print('1. Registrar Mascota')
            print('****************************************************************')
            mascota1 = Mascota()
            mascota1.registrar_mascota()
            os.system("pause")
            os.system("cls")
            
        elif opcion == '2':
            
            print('2. Menú Consultar')
            print('****************************************************************')
            codigo = int(input('Ingrese el código de la mascota: '))
            mascota1 = Mascota()
            mascota1.buscar_mascota(codigo)
            os.system("pause")
            os.system("cls")
            
        
        elif opcion == '3':
            
            print('3. Menú Actualizar')
            print('****************************************************************')
            codigo = int(input('Ingrese el código de la mascota: '))
            mascota1 = Mascota()
            mascota1.actualizar_mascota(codigo)
            os.system("pause")
            os.system("cls")
            
        elif opcion == '4':
           
            print('4.Menú Eliminar') 
            print('****************************************************************')
            codigo = int(input('Ingrese el código de la mascota: '))
            mascota1 = Mascota()
            mascota1.eliminar_mascota(codigo)
            os.system("pause")
            os.system("cls")
            
        
        else:
            print('Opción no válida. Intente de nuevo')

if __name__ == "__main__":
    main()
