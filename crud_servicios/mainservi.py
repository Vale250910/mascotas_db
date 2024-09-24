
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crud_servicios.servicios import Servicios
from crud_servicios.menuser import MenuServicios
MenuServicios.menu_servicio()