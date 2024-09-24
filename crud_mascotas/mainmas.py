import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crud_mascotas.mascota import Mascota
from crud_mascotas.menumas import MenuMascota
MenuMascota.menu_mascotas()