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
