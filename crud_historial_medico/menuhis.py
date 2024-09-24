import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crud_historial_medico.historialmedico import HistorialMedico
import os
class MenuHistorialMedico:
    @staticmethod
    def menu_historial_medico():
        while True:
            print('*************** MENU HISTORIAL MÉDICO ********************')
            print('         1- Registrar nuevo historial médico')
            print('         2- Consultar un historial médico por codigo')
            print('         3- Consultar historiales')
            print('         4- Activar o Inactivar Historial médico')
            print('         5- Actualizar un historial médico por codigo')
            print('         6- Eliminar un historial médico')
            print('         7- Salir del sistema')
            print('*************** MENU HISTORIAL MÉDICO ********************')
            opcion = input('Seleccione una opción: ')
            os.system("pause")
            os.system("cls")
            if opcion == '7':
                print('Gracias por usar nuestra app..')
                os.system("pause")
                os.system("cls")
                break
                
            elif opcion == '1':
                
                print('         1. Registrar Historial Médico -->')
                print('****************************************************************')
                historial1 = HistorialMedico()
                historial1.guardar_historial_medico()
                os.system("pause")
                os.system("cls")
            
            elif opcion == '2':
                print('         2. Menú Consultar Historial Médico Por Código -->')
                print('****************************************************************')
                codigo_mascota = input('Ingrese el código del historial medico: ')
                historial1 = HistorialMedico()
                historial1.buscar_historial_id(codigo_mascota)
                os.system("pause")
                os.system("cls")
            

            elif opcion == '3':
                print('         3. Menú Consultar Todos los Historiales Médicos -->')
                print('****************************************************************')
                historial1 = HistorialMedico()
                historial1.buscar_historiales()
                os.system("pause")
                os.system("cls")
            
            elif opcion == '4':
                print('         4. Menú Activar o Desactivar Historiales Médicos -->')
                print('****************************************************************')
                historial1 = HistorialMedico()
                historial1.actualizar_estado_historial()
                os.system("pause")
                os.system("cls")

            elif opcion == '5':
                print('         5. Menú Actualizar Por Código -->')
                print('****************************************************************')
                codigo = input('Ingrese el código del historial: ')
                historial1 = HistorialMedico()
                historial1.actualizar_historial(codigo)
                os.system("pause")
                os.system("cls")    
            
            elif opcion == '6':
                print('         6.Menú Eliminar Por Código-->') 
                print('****************************************************************')
                id = input('Ingrese el código del historial: ')
                historial1 = HistorialMedico()
                historial1.eliminar_historial(id)
                os.system("pause")
                os.system("cls")
            else:
                print('Opción no válida. Intente de nuevo')

if __name__ == "__main__":
        MenuHistorialMedico.menu_historial_medico()