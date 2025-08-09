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
