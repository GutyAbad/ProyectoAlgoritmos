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
