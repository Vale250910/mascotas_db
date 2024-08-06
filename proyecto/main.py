from os import system
from mascota import Mascota

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

        if opcion == '5':
            print('Gracias por usar nuestra app..')
            break
        
        elif opcion == '1':
            print('1. Registrar Mascota')
            # Crear un objeto mascota
            mascota1 = Mascota()
            mascota1.registrar_mascota()
        
        elif opcion == '2':
            print('Menú Consultar')
            mascota1 = Mascota()
            mascota1.buscar_mascota()
        elif opcion == '3':
            print('Menú Actualizar ')
            mascota1 = Mascota()
            mascota1.actualizar_mascota()
        elif opcion == '4':
            print('Menú Eliminar  ')
            mascota1 = Mascota()
            mascota1.eliminar_mascota()
        else:
            print('Opción no válida. Intente de nuevo')

if __name__ == "__main__":
    main()


