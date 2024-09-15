import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crud_veterinarios.veterinario import Veterinario
from crud_veterinarios.menuvet import MenuVeterinario
MenuVeterinario.menu_veterinario()