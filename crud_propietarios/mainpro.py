import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crud_propietarios.propietario import Propietario
from crud_propietarios.menupro import MenuPropietario
MenuPropietario.menu_propietario()