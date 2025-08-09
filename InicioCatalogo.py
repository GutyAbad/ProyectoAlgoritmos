from obra import ObraDeArte
from utils import get_api_data, cargar_nacionalidades, mostrar_imagen_pillow

class CatalogoMet:
    def __init__(self):
        self.obras = []
        self.departamentos = {}
        self.nacionalidades = []
        print("Cargando catálogo inicial, por favor espere...")
        self._cargar_departamentos()
        self.nacionalidades = cargar_nacionalidades()
        self._cargar_obras_iniciales()
        print("Catálogo cargado. Listo para usar.")

    def _cargar_departamentos(self):
        data = get_api_data("departments")
        if data and "departments" in data:
            self.departamentos = {d["departmentId"]: d["displayName"] for d in data["departments"]}



