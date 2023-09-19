# Definición de la lista de frutas
frutas = []


# Función para calcular el costo total de las frutas
def calcular_costo_total(frutas):
    costo_total = sum(fruta["precio_unitario"] * fruta["cantidad"] for fruta in frutas)
    return costo_total


# Función para mostrar las frutas ordenadas por precio unitario de mayor a menor
def mostrar_frutas_ordenadas(frutas):
    frutas_ordenadas = sorted(frutas, key=lambda x: x["precio_unitario"], reverse=True)
    print("\nFrutas ordenadas por precio unitario de mayor a menor:")
    for fruta in frutas_ordenadas:
        print(
            f"ID: {fruta['id']}, Nombre: {fruta['nombre']}, Precio Unitario: {fruta['precio_unitario']:.2f}, Cantidad: {fruta['cantidad']}")


# Función para mostrar la fruta de mayor y menor precio unitario
def mostrar_frutas_extremas(frutas):
    fruta_menor_precio = min(frutas, key=lambda x: x["precio_unitario"])
    fruta_mayor_precio = max(frutas, key=lambda x: x["precio_unitario"])
    print("\nFruta de menor precio unitario:")
    print(
        f"ID: {fruta_menor_precio['id']}, Nombre: {fruta_menor_precio['nombre']}, Precio Unitario: {fruta_menor_precio['precio_unitario']:.2f}")
    print("\nFruta de mayor precio unitario:")
    print(
        f"ID: {fruta_mayor_precio['id']}, Nombre: {fruta_mayor_precio['nombre']}, Precio Unitario: {fruta_mayor_precio['precio_unitario']:.2f}")


# Función principal del programa
def main():
    cantidad_frutas = int(input("Ingrese la cantidad de frutas para el salpicón: "))

    for i in range(cantidad_frutas):
        print(f"\nFruta {i + 1}:")
        id_fruta = input("ID de la fruta: ")
        nombre_fruta = input("Nombre de la fruta: ")
        precio_unitario_fruta = float(input("Precio unitario de la fruta: "))
        cantidad_fruta = int(input("Cantidad de la fruta: "))

        fruta = {
            "id": id_fruta,
            "nombre": nombre_fruta,
            "precio_unitario": precio_unitario_fruta,
            "cantidad": cantidad_fruta
        }
        frutas.append(fruta)

    costo_total = calcular_costo_total(frutas)
    print(f"\nCosto total del salpicón: ${costo_total:.2f}")

    mostrar_frutas_ordenadas(frutas)

    mostrar_frutas_extremas(frutas)


if __name__ == "__main__":
    main()
