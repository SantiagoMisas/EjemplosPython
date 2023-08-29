productoTerminado1={
    'referencia':5087,
    'marca':"americanino",
    'descripcion':"chompa",
    'color': "naranja",
    'costoUnitario': 100000,
    'disponibleBodega': True,
    'costoVenta':85000,
    'puntosVenta':['cc mayorca', 'terminalNorte','puerta Del Norte','centro de la moda']
}

productoTerminado2={
    'referencia':5088,
    'marca':"americanino",
    'descripcion':"Camiseta Polo",
    'color': "Azul Oscuro",
    'costoUnitario': 30000,
    'disponibleBodega': True,
    'costoVenta':150000,
    'puntosVenta':['cc mayorca', 'terminalNorte','puerta Del Norte','centro de la moda']
}

#Creando Una Lista De Diccionarios

productos=[productoTerminado1, productoTerminado2]

#Recorriendo una lista con ciclo For

'''for contador in range(1, 10, 2):
    print(contador)'''

for producto in productos:
    print(producto)