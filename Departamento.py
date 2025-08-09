def buscar_por_departamento(self):
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
