from historialmedico import HistorialMedico
import os
def main():
    while True:
        print('***************MENU MASCOTAS********************')
        print('1- Registrar nuevo historial')
        print('2- Consultar un historial')
        print('3- Actualizar un historial')
        print('4- Consultar cuantas mascotas tiene la tabla')
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
            
            print('1. Registrar Historial Medico')
            print('****************************************************************')
            historial1 = HistorialMedico()
            historial1.guardar_historial_medico()
            os.system("pause")
            os.system("cls")
if __name__ == "__main__":
    main()