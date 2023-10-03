ventas=[
    {"id": "afc001", "nombre": "Peter","costo":3500000},
    {"id": "afc030","nombre": "Albert","costo":1200000},
    {"id": "afc500","nombre": "Jonas","costo":1100000},
    {"id": "afc980","nombre": "Ray","costo":4100000},
    {"id":"afc320","nombre": "Scarlet","costo":2600000},
    {"id": "afc981","nombre": "Sammy","costo":800000}
]

#Los ids en mayuscula, compras superiores a 60000, comprar superiores de menor a mayor (afc320---nombre costo:120000)

convertirMayusculas=lambda texto:texto.upper()
for venta in ventas:
    venta["id"]=convertirMayusculas(venta["id"])

costosAltos=[venta for venta in ventas if venta["costo"]>600000]

ventasOrdenadas=sorted(costosAltos, key=lambda venta:venta["costo"])

for venta in ventasOrdenadas:
    print(f"{venta['id']}---{venta['nombre']} costo: {venta['costo']}")
