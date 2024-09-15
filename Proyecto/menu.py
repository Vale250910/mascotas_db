# Importar los menús de las diferentes clases
from crud_administradores.menuadmi import MenuAdministrador
from crud_citas.menucit import MenuCitas
from crud_historial_medico.menuhis import MenuHistorialMedico
from crud_mascotas.menumas import MenuMascota
from crud_producto.menuprod import MenuProductos
from crud_propietarios.menupro import MenuPropietario
from crud_veterinarios.menuvet import MenuVeterinario
from crud_servicios.menuser import MenuServicios
import os
# Clase para el menú principal

class MenuPrincipal:
    @staticmethod
    def menu_principal():
        try:
            while True:
                print("\n******************** MENU PRINCIPAL ****************")
                print("         1. Administradores")
                print("         2. Propietarios")
                print("         3. Veterinarios")
                print("         4. Citas")
                print("         5. Historial Médico")
                print("         6. Mascotas")
                print("         7. Productos") 
                print("         8. Servicios")
                print("         9. Salir")
                print("\n******************** MENU PRINCIPAL ****************")
                
                opcion = input("Seleccione una opción: ")
                os.system("pause")
                os.system("cls")
                
                if opcion == "1":
                    admin = MenuAdministrador()
                    admin.menu_administrador()
                    os.system("pause")
                    os.system("cls")
                    
                elif opcion == "2":
                    propietarios = MenuPropietario()
                    propietarios.menu_propietario()
                    os.system("pause")
                    os.system("cls")
                    
                elif opcion == "3":
                    vet = MenuVeterinario()
                    vet.menu_veterinario()
                    os.system("pause")
                    os.system("cls")
                    
                elif opcion == "4":
                    citas = MenuCitas()
                    citas.menu_citas()
                    os.system("pause")
                    os.system("cls")
                    
                elif opcion == "5":
                    his = MenuHistorialMedico()
                    his.menu_historial_medico()
                    os.system("pause")
                    os.system("cls")
                    
                elif opcion == "6":
                    mas = MenuMascota()
                    mas.menu_mascotas()
                    os.system("pause")
                    os.system("cls")
                    
                elif opcion == "7":
                    prod = MenuProductos()
                    prod.menu_productos()
                
                elif opcion == "8":
                    serv = MenuServicios()
                    serv.menu_servicio()
                        
                elif opcion == "9":
                    print("Gracias por usar el sistema. ¡Hasta luego!")
                    break
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")
        except KeyboardInterrupt:
            print('El usuario ha cancelado la ejecución, por favor continue')
        except Exception as error:
            print(f'Ha ocurrido error no codificado {error}')
        finally:
            print('Intente de nuevo')

if __name__ == "__main__":
    MenuPrincipal.menu_principal()