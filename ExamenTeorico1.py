opcion = 0

# MENU DE OPCIONES
print("1. Agregar una banda")
print("2. Mostrar todas las bandas")
print("3. Buscar una banda")
print("4. Editar una banda")
print("5. Eliminar una banda")
print("6. Salir")
bandas = []

while opcion != 6:
    if opcion == 1:
        banda = {}
        banda["nombreBanda"] = input("Ingresa el nombre de la banda: ")
        banda["codigoBanda"] = input("Ingresa el código de la banda: ")
        banda["generoBanda"] = input("Ingresa el género de la banda: ")
        banda["horaPresentacion"] = input("Ingresa la hora de presentación de la banda: ")
        banda["pagoAgrupacion"] = float(input("Ingresa el pago para la banda: "))
        banda["estadoPresentacion"] = input("Ingresa el estado si ya se presentó la banda (True/False): ").lower() == 'true'
        bandas.append(banda)
    elif opcion == 2:
        for banda in bandas:
            if not banda["estadoPresentacion"]:
                print(f"Código de Banda: {banda['codigoBanda']}")
                print(f"Nombre de Banda: {banda['nombreBanda']}")
                print(f"Género de Banda: {banda['generoBanda']}")
                print(f"Hora de Presentación: {banda['horaPresentacion']}")
                print(f"Pago de la Banda: {banda['pagoAgrupacion']}")
                print(f"Estado de Presentación de la Banda: {banda['estadoPresentacion']}")
                print("-" * 40)
            else:
                print(f"La banda {banda['nombreBanda']} ya ha hecho su presentación.")
    elif opcion == 3:
        buscar = input("Ingresa el nombre de la banda a buscar: ")
        bandaBuscada = False
        for banda in bandas:
            if buscar == banda['nombreBanda']:
                print(f"Banda encontrada: {banda['nombreBanda']}")
                bandaBuscada = True
                break
        if not bandaBuscada:
            print("Banda no encontrada")
    elif opcion == 4:
        buscar = input("Ingresa el nombre de la banda a editar: ")
        for banda in bandas:
            if buscar == banda["nombreBanda"] and not banda["estadoPresentacion"]:
                print(f"Editando banda: {banda['nombreBanda']}")
                banda["horaPresentacion"] = input("Ingresa la nueva hora de presentación de la banda: ")
                print("Banda editada exitosamente")
                break
        else:
            print("La banda no se puede editar, o ya se ha presentado.")
    elif opcion == 5:
        buscar = input("Ingresa el nombre de la banda a eliminar: ")
        for banda in bandas:
            if buscar == banda["nombreBanda"] and not banda["estadoPresentacion"]:
                bandas.remove(banda)
                print(f"Banda {banda['nombreBanda']} eliminada exitosamente")
                break
        else:
            print("Banda no encontrada o no se puede eliminar.")
    elif opcion == 6:
        break
    else:
        print("Opción ingresada no válida, vuelva a intentarlo")

    opcion = int(input("Ingresa una de las opciones: "))
