from catalogo_met import CatalogoMet

def main():
    catalogo = CatalogoMet()

    while True:
        print("\n--- Menú Principal del Catálogo ---")
        print("1. Ver lista de obras por Departamento")
        print("2. Ver lista de obras por Nacionalidad del autor")
        print("3. Ver lista de obras por nombre del autor")
        print("4. Mostrar detalles de una obra por ID")
        print("5. Salir")
        print("----------------------------------\n")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            catalogo.buscar_por_departamento()
        elif opcion == '2':
            catalogo.buscar_por_nacionalidad()
        elif opcion == '3':
            catalogo.buscar_por_autor()
        elif opcion == '4':
            catalogo.mostrar_detalles_obra()
        elif opcion == '5':
            print("Saliendo del programa. ¡Gracias por usar el catálogo!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
