empleados=[
    {"codigo":102, "salario":2000000, "nombre":"Fernando Pascal"},
    {"codigo":105, "salario":4000000, "nombre":"Andrea Perez"},
    {"codigo":109, "salario":6000000, "nombre":"Fernando Pascal"},
    {"codigo":105, "salario":7000000, "nombre":"Fernando Pascal"},
    {"codigo":115, "salario":8000000, "nombre":"Mike Scott"},
    {"codigo":117, "salario":2000000, "nombre":"Juan Ramirez"},
    {"codigo":125, "salario":1500000, "nombre":"John Smith"},
    {"codigo":135, "salario":2700000, "nombre":"Patrick Sousa"},
    {"codigo":101, "salario":2000000, "nombre":"Wendy Rouse"},
    {"codigo":165, "salario":3000000, "nombre":"Lana Ridss"}
]

##filtrar los empleados con salarios mayores 2.5

empleadosAltosSalarios=[empleado for empleado in empleados if empleado["salario"]>2500000]

print(empleadosAltosSalarios)

#se organicen por codigo de menor a mayor

altosSalariosOrdenados=sorted(empleadosAltosSalarios,key=lambda empleado:empleado["codigo"])

for empleado in altosSalariosOrdenados:
    print(f"Codigo: {empleado['codigo']} ----Nombre:{empleado['nombre']} ")