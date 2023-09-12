def saludar(name):
    return f"hola, te saludo: {name}"

print (saludar("Santiago"))

def mult(numero1, numero2):
    return numero1*numero2
print (mult(50, 2))



horaSalario=1160000/188
rtfFte=2/100
segSocial=8/100
operarios=[]
operario={}
operario["id"] ="123456"
operario["nombre"] ="Santiago"
operario["horas"] = 168
operario["novedades"] = "trabajo todos los dias"
operario["fotografias"] ="imagen"

def horaBase(salario, horasTotales):
    return salario/horasTotales
def retencionSeguro(salario, porcentajeRetencion, porcentajeSeguridadSocial):
    retencion=salario*(porcentajeRetencion/100)
    seguridad=salario*(porcentajeSeguridadSocial/100)
    return retencion+seguridad
def calcularSalario(horas, cantidadSalario):
    if horas<1 and horas>188:
        print("Cantidad  no valida, supera el tope de horas permitidas")
    else:
        horaBase()



