import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crud_producto.producto import Productos
import os
class MenuProductos:
    @staticmethod
    def menu_productos():
        while True:
            print('*************** MENU Productos ********************')
            print('         1- Registrar nuevo productos ')
            print('         2- Consultar productos ')
            print('         3- Consultar productos por codigo ')
            print('         4- Consultar productos por nombre ')
            print('         5- Activar O Inactivar productos ')
            print('         6- Actualizar productos ')
            print('         7- Eliminar productos ')
            print('         8- Salir')
            print('*************** MENU Productos ********************')
            opcion = input('Seleccione una opción: ')
            os.system("pause")
            os.system("cls")
            if opcion == '8':
                print('Gracias por usar nuestra app..')
                os.system("pause")
                os.system("cls")
                break
                
            elif opcion == '1':
                
                print('         1. Registrar Productos -->')
                print('****************************************************************')
                productos1 = Productos()
                productos1.registrar_producto()
                os.system("pause")
                os.system("cls")
            
            elif opcion == '2':
                print('         2. Consultar Productos -->')
                print('****************************************************************')
                productos1 = Productos()
                productos1.mostrar_todas_los_productos()
                os.system("pause")
                os.system("cls")
            
            elif opcion == '3':
                print('         3. Consultar Productos Por Codigo -->')
                print('****************************************************************')
                codigo= input("Escriba el codigo del producto: ")
                productos1 = Productos()
                productos1.buscar_producto_por_codigo(codigo)
                os.system("pause")
                os.system("cls")
            
            elif opcion == '4':
                
                print('         4. Buscar Productos Por Nombre -->')
                print('****************************************************************')
                nombre= input("Ingrese el nombre del producto que desea buscar: ")
                productos1 = Productos()
                productos1.buscar_producto_nombre(nombre)
                os.system("pause")
                os.system("cls")
            
            elif opcion == '5':

                print('         5. Activar O Inactivar Productos -->')
                print('****************************************************************')
                codigo= input('Ingrese el codigo del producto: ')
                productos1 = Productos()
                productos1.actualizar_estado_producto(codigo)
                os.system("pause")
                os.system("cls")
            
            elif opcion == '6':
                
                print('         6. Actualizar Productos -->')
                print('****************************************************************')
                codigo= input('Ingrese el codigo del producto a actualizar: ')
                productos1 = Productos()
                productos1.actualizar_producto(codigo)
                os.system("pause")
                os.system("cls")
                
            elif opcion == '7':
                
                print('         7. Eliminar Productos -->')
                print('****************************************************************')
                codigo= input("Escriba el codigo del producto: ")
                productos1 = Productos()
                productos1.eliminar_producto(codigo)
                os.system("pause")
                os.system("cls")
            

if __name__ == "__main__":
    MenuProductos.menu_productos()  