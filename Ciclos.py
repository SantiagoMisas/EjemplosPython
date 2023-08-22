print("Departamento de confeccion")
print("0. Ingresar producto a fabrica")
print("1. Mostrar inventario de fabrica")
print("2. Salir")
opcion=100
listaProductos=[]
while opcion!=0:
    opcion = int(input("Digite una opcion: "))
    if opcion == 1:
        producto = input("Ingrese el nombre del producto: ")
        #Agregar un producto a la lista de productos
        listaProductos.append(producto)
    elif opcion == 2:
        print("mostrar el inventaro: ")
        print(listaProductos)
    elif opcion == 0:
        print("programa cerrado")

    else:
        print("opcion no valida")

print("fin del programa")

# Tarea calcular la estacion segun un mes proporcionado por consola fechas
# dia no mayor a 30
# mes
# enero
# febrero
# hasta 20 marzo Invierno
# 21 marzo hasta 10 de junio=verano
# 11 de junio hasta septiembre 25=otoño
# septiembre 26 hasta 30 de diciembre=primavera
# subido en git
# 3225962363
#
# Tarea etapas de la vida
# 0-14 años niño
# 15-28 joven
# 28 a 60 adulto
# mas de 60 adulto mayor
# hacer menu ciclico que deje intentar varias veces