#MENU DE OPCIONES
#1. Ingresar producto
#2 Verificar los productos
#3. Buscar un producto
#4. Editar un producto
#5. Retirar un producto bodega

opcion=0

#MENU DE OPCIONES
print("1. Ingresar producto")
print("2 Verificar los productos")
print("3. Buscar un producto")
print("4. Editar un producto")
print("5. Retirar un producto bodega")
print("6. Salir")
productos=[]
while(opcion!=6):
    producto={}
    opcion=int(input("Digita la opcion: "))

    if opcion==1:
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["codigo"]=int(input("Digita el codigo del producto: "))
        producto["descripcion"]=input("Digita la descripcion del producto: ")
        producto["foto"]=input("Digita la url de foto del producto: ")
        producto["precio"]=float(input("Digita el precio del producto: "))
        producto["stock"]=int(input("Digita el stock del producto: "))
        producto["fechaEntregaBodega"]=input("Digita la fecha del producto: ")
        productos.append(producto)
    elif opcion==2:
        for productoSeleccionado in productos:
            print(f"codigo: {productoSeleccionado['codigo']}")
            print(f"nombre: {productoSeleccionado['nombre']}")
            print(f"precio: {productoSeleccionado['precio']}")
            print(f"descripcion: {productoSeleccionado['descripcion']}")
            print(f"foto: {productoSeleccionado['foto']}")
            print(f"stock: {productoSeleccionado['stock']}")
            print(f"fechaEntregaBodega: {productoSeleccionado['fechaEntregaBodega']}")

    elif opcion==3:
        buscar=input("Digita el nombre del producto a buscar: ")
        productoBuscado=False
        for producto in productos:
            if buscar==producto['nombre']:
                print (f" Producto encontrado: {producto['nombre']}")
                productoBuscado = True
                break
            else:
                print ("producto no encontrado")

    elif opcion==4:
        buscar=input("Digita el nombre del producto para editar: ")
        for producto in productos:
            if buscar == producto['nombre']:
                print(f"Editando producto: {producto['nombre']}")
                producto["precio"] = float(input("Digita el nuevo precio del producto: "))
                producto["stock"] = int(input("Digita el nuevo stock del producto: "))
                producto["fechaEntregaBodega"] = input("Digita la nueva fecha del producto: ")
                print("Producto editado exitosamente")
                break
        else:
            print("Producto no encontrado")
    elif opcion==5:
        buscar = input("Digita el nombre del producto a retirar: ")
        for producto in productos:
            if buscar == producto['nombre']:
                productos.remove(producto)
                print(f"Producto {producto['nombre']} retirado exitosamente")
                break
        else:
            print("Producto no encontrado")
    elif opcion==6:
        pass
    else:
        print ("Opcion Invalida, vuelva a intentarlo")