from historialmedico import HistorialMedico
import os
class MenuHistorialMedico:
    @staticmethod
    def menu_historial_medico():
        while True:
            print('*************** MENU HISTORIAL MEDICO ********************')
            print('         1- Registrar nuevo historial')
            print('         2- Consultar un historial por mascota')
            print('         3- Actualizar un historial por mascota')
            print('         4- Eliminar un historial')
            print('         5- Salir del sistema')
            print('*************** MENU HISTORIAL MEDICO ********************')
            opcion = input('Seleccione una opción: ')
            os.system("pause")
            os.system("cls")
            if opcion == '5':
                print('Gracias por usar nuestra app..')
                os.system("pause")
                os.system("cls")
                break
                
            elif opcion == '1':
                
                print('         1. Registrar Historial Medico -->')
                print('****************************************************************')
                historial1 = HistorialMedico()
                historial1.guardar_historial_medico()
                os.system("pause")
                os.system("cls")
            
            elif opcion == '2':
                print('         2. Menú Consultar -->')
                print('****************************************************************')
                codigo_mascota = int(input('Ingrese el código de la mascota: '))
                historial1 = HistorialMedico()
                historial1.buscar_historial_mascota(codigo_mascota)
                os.system("pause")
                os.system("cls")
            
            
            elif opcion == '3':
                print('         3. Menú Actualizar -->')
                print('****************************************************************')
                id = int(input('Ingrese el código de la mascota: '))
                historial1 = HistorialMedico()
                historial1.actualizar_historial(id)
                os.system("pause")
                os.system("cls")    
            
            elif opcion == '4':
                print('         4.Menú Eliminar -->') 
                print('****************************************************************')
                id = int(input('Ingrese el código de la mascota: '))
                historial1 = HistorialMedico()
                historial1.eliminar_historial(id)
                os.system("pause")
                os.system("cls")
            else:
                print('Opción no válida. Intente de nuevo')

if __name__ == "__main__":
        MenuHistorialMedico.menu_historial_medico()