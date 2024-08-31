import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from citas import Citas
from menucit import MenuCitas
MenuCitas.menu_citas()