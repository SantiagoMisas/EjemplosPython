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


resultado=0
def impTemporada():
    return "la temporada es"
def resultadoIntervalos(resultado):
    if resultado>0 and resultado <=80:
        return f"{impTemporada()} invierno"
    elif resultado>80 and resultado<=160:
        return f"{impTemporada()} verano"
    elif resultado>160 and resultado<=265:
        return f"{impTemporada()} otoño"
    elif resultado >265 and resultado <=360:
        return f"{impTemporada()} primavera"
    else:
        return "Los datos ingresados son invalidos"

def calcularTemporada(mes, dia):
        resultado= (mes * 30)+dia
        return resultadoIntervalos(resultado)

mes=int(input("Ingrese el numero de mes a consultar correspondiente de 1 a 12: "))
dia=int(input("Ingrese el dia de en curso del mes: "))
if mes>=1 and mes<=12:
    if dia>=1 and dia<=30:
        temporada=calcularTemporada(mes,dia)
        print(temporada)
    else:
        print("El numero de dia ingresado no es valido.")
else:
        print("El numero de mes ingresado no es valido")

def impEdad(edad):
    return f"Edad: {edad}"
edad=int(input("Ingrese la edad correspondiente: "))
def etapaDeVida(edad):
    if edad>=0 and edad<=14:
        return f"{impEdad(edad)} Niño"
    elif edad>15 and edad<=28:
        return f"{impEdad(edad)} Joven"
    elif edad>28 and edad<=60:
        return f"{impEdad(edad)} Adulto"
    elif edad>60 and edad<=110:
        return f"{impEdad(edad)} Adulto Mayor"
    else:
        return "La edad ingresada no es correcta"

etapa = etapaDeVida(edad)
print(etapa)