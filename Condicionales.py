#
# edadUsuario=int(input("Digite su edad: "))
#
# if edadUsuario>=18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted es meyor de edad")
#     print("No puedes entrar al lugar")
#
# print("Continua el programa")

#Evaluando multiples condiciones

metrosCubicos=int(input("Nivel en metros cubicos: "))

if metrosCubicos>=0 and metrosCubicos<=200:
    print(f"El nivel de metros cubicos es aceptable, esta dentro del rango {metrosCubicos} metros, nivel bajo")

elif metrosCubicos>200 and metrosCubicos<=400:
    print(f"El nivel opera con normalidad {metrosCubicos} metros, nivel medio")

elif metrosCubicos>400:
    print(f"Nivel superior {metrosCubicos} metros, nivel alto, inicie plan de evacuacion")

else:
    print(f" Nivel no aceptado revisar los datos")