from Obra import ObraDeArte
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
 
    def _cargar_obras_iniciales(self):
 
        departamentos_a_precargar = [11, 6]
        for dep_id in departamentos_a_precargar:
            print(f"Cargando obras del departamento '{self.departamentos.get(dep_id, 'Desconocido')}'...")
            search_data = get_api_data("search", {"isHighlight": True, "departmentId": dep_id})
            if search_data and search_data["total"] > 0:
                object_ids = search_data["objectIDs"][:30]
                for obj_id in object_ids:
                    obra_data = get_api_data(f"objects/{obj_id}")
                    if obra_data:
                        obra = ObraDeArte(
                            object_id=obra_data.get("objectID"),
                            title=obra_data.get("title"),
                            artist_name=obra_data.get("artistDisplayName", "Desconocido"),
                            artist_nationality=obra_data.get("artistNationality", "Desconocida"),
                            artist_begin_date=obra_data.get("artistBeginDate", "Desconocida"),
                            artist_end_date=obra_data.get("artistEndDate", "Desconocida"),
                            classification=obra_data.get("classification", "Desconocida"),
                            object_date=obra_data.get("objectDate", "Desconocida"),
                            image_url=obra_data.get("primaryImage", "No disponible")
                        )
                        self.obras.append(obra)
 
    def _imprimir_listado_obras(self, obras_encontradas: list):
        if not obras_encontradas:
            print("No se encontraron obras que cumplan con la condición.")
            return
 
        print("\n--- Obras encontradas ---")
        for obra in obras_encontradas:
            print(f"ID de Obra: {obra.object_id} | Título: {obra.title} | Autor: {obra.artist_name}")
        print("-------------------------\n")
 
    def buscar_por_departamento(self):
        print("\n--- Departamentos del Museo ---")
        for dep_id, dep_name in self.departamentos.items():
            print(f"ID: {dep_id} | Departamento: {dep_name}")
        print("------------------------------")
 
        dep_id_str = input("Ingrese el ID del departamento que desea buscar: ")
        try:
            dep_id = int(dep_id_str)
            departamento_seleccionado = self.departamentos.get(dep_id)
            if not departamento_seleccionado:
                print("ID de departamento no válido.")
                return
 
            obras_encontradas = [
                obra for obra in self.obras
                if get_api_data(f"objects/{obra.object_id}").get("departmentId") == dep_id
            ]
            self._imprimir_listado_obras(obras_encontradas)
 
        except ValueError:
            print("Por favor, ingrese un número válido para el ID del departamento.")
 
    def buscar_por_nacionalidad(self):
        print("\n--- Nacionalidades de artistas disponibles ---")
        nacionalidades_unicas = sorted(list(set(obra.artist_nationality for obra in self.obras if obra.artist_nationality != "Desconocida")))
        for nacionalidad in nacionalidades_unicas:
            print(f"- {nacionalidad}")
        print("-------------------------------------------\n")
 
        nacionalidad_elegida = input("Ingrese la nacionalidad que desea buscar: ")
        obras_encontradas = [
            obra for obra in self.obras
            if obra.artist_nationality.lower() == nacionalidad_elegida.lower()
        ]
        self._imprimir_listado_obras(obras_encontradas)
 
    def buscar_por_autor(self):
        nombre_autor = input("Ingrese el nombre del autor que desea buscar: ")
        obras_encontradas = [
            obra for obra in self.obras
            if nombre_autor.lower() in obra.artist_name.lower()
        ]
        self._imprimir_listado_obras(obras_encontradas)
 
    def mostrar_detalles_obra(self):
        try:
            object_id = int(input("Ingrese el ID de la obra para ver sus detalles: "))
            obra_encontrada = next((obra for obra in self.obras if obra.object_id == object_id), None)
 
            if obra_encontrada:
                print("\n--- Detalles de la Obra ---")
                print(f"Título: {obra_encontrada.title}")
                print(f"Nombre del Artista: {obra_encontrada.artist_name}")
                print(f"Nacionalidad del artista: {obra_encontrada.artist_nationality}")
                print(f"Fecha de nacimiento: {obra_encontrada.artist_begin_date}")
                print(f"Fecha de muerte: {obra_encontrada.artist_end_date}")
                print(f"Tipo (classification): {obra_encontrada.classification}")
                print(f"Año de creación (objectDate): {obra_encontrada.object_date}")
                print("----------------------------\n")
 
                if obra_encontrada.image_url and obra_encontrada.image_url != "No disponible":
                    mostrar_img = input("¿Desea ver la imagen de la obra? (s/n): ").lower()
                    if mostrar_img == 's':
                        mostrar_imagen_pillow(obra_encontrada.image_url, obra_encontrada.title)
                else:
                    print("Imagen no disponible para esta obra.")
            else:
                print(f"No se encontró ninguna obra con el ID {object_id} en el catálogo.")
 
        except ValueError:
            print("Por favor, ingrese un ID numérico válido.")
