import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crud_administradores.administrador import Administrador
from crud_administradores.menuadmi import MenuAdministrador
MenuAdministrador.menu_administrador()