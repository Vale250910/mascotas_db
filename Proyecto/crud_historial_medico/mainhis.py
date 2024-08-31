import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crud_historial_medico.historialmedico import HistorialMedico
from crud_historial_medico.menuhis import MenuHistorialMedico
MenuHistorialMedico.menu_historial_medico()