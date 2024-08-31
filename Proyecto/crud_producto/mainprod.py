import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crud_producto.producto import Productos
from crud_producto.menuprod import MenuProductos
MenuProductos.menu_productos()