# VARIABLES GLOBALES
opcion = 0
bandas = []

# DEFINICIÓN DE FUNCIONES

def mostrar_menu():
    print("\n---- Menú de Bandas ----")
    print("1. Agregar una banda")
    print("2. Mostrar todas las bandas")
    print("3. Buscar una banda")
    print("4. Editar una banda")
    print("5. Eliminar una banda")
    print("6. Salir")

def agregar_banda():
    banda = {}
    banda["nombreBanda"] = input("Ingresa el nombre de la banda: ")
    banda["codigoBanda"] = input("Ingresa el código de la banda: ")
    banda["generoBanda"] = input("Ingresa el género de la banda: ")
    banda["horaPresentacion"] = input("Ingresa la hora de presentación de la banda: ")
    pago_input = input("Ingresa el pago para la banda: ")
    
    # Solicita al usuario que ingrese "True" o "False" para el estado de presentación
    estado_presentacion_input = input("¿La banda está presentada? (True/False): ").strip().lower()
    if estado_presentacion_input == "true":
        banda["estadoPresentacion"] = True
    elif estado_presentacion_input == "false":
        banda["estadoPresentacion"] = False
    else:
        print("\nError: Ingresa 'True' o 'False' para el estado de presentación.")
        return

    try:
        banda["pagoAgrupacion"] = float(pago_input)
        bandas.append(banda)
        print(f"\nBanda {banda['nombreBanda']} agregada exitosamente.")
    except ValueError:
        print("\nError: El pago debe ser un número válido.")

def mostrar_bandas():
    if not bandas:
        print("\nNo hay bandas registradas.")
    else:
        print("\n---- Lista de Bandas ----")
        for banda in bandas:
            print(f"Código de Banda: {banda['codigoBanda']}")
            print(f"Nombre de Banda: {banda['nombreBanda']}")
            print(f"Género de Banda: {banda['generoBanda']}")
            print(f"Hora de Presentación: {banda['horaPresentacion']}")
            print(f"Pago de la Banda: {banda['pagoAgrupacion']}")
            print(f"Estado de Presentación de la Banda: {banda['estadoPresentacion']}")
            print("-" * 30)

def buscar_banda():
    buscar = input("\nIngresa el nombre de la banda a buscar: ")
    bandaEncontrada = False
    for banda in bandas:
        if buscar == banda["nombreBanda"]:
            print(f"\nBanda encontrada: {banda['nombreBanda']}")
            bandaEncontrada = True
            break
    if not bandaEncontrada:
        print("\nBanda no encontrada.")

def editar_banda():
    buscar = input("\nIngresa el nombre de la banda a editar: ")
    for banda in bandas:
        if buscar == banda["nombreBanda"] and not banda["estadoPresentacion"]:
            print(f"\nEditando banda: {banda['nombreBanda']}")
            banda["horaPresentacion"] = input("Ingresa la nueva hora de presentación de la banda: ")
            print("\nBanda editada exitosamente.")
            break
    else:
        print("\nLa banda no se puede editar, ya ha sido presentada.")

def eliminar_banda():
    buscar = input("\nIngresa el nombre de la banda a eliminar: ")
    for banda in bandas:
        if buscar == banda["nombreBanda"] and not banda["estadoPresentacion"]:
            bandas.remove(banda)
            print(f"\nBanda {banda['nombreBanda']} eliminada exitosamente.")
            break
    else:
        print("\nLa banda no se puede eliminar o no se encontró.")

# INICIO DEL PROGRAMA
while opcion != 6:
    mostrar_menu()
    opcion = int(input("Ingresa una de las opciones: "))

    if opcion == 1:
        agregar_banda()
    elif opcion == 2:
        mostrar_bandas()
    elif opcion == 3:
        buscar_banda()
    elif opcion == 4:
        editar_banda()
    elif opcion == 5:
        eliminar_banda()
    elif opcion == 6:
        print("\nSaliendo del programa...")
    else:
        print("\nOpción no válida. Ingresa un número del 1 al 6.")
