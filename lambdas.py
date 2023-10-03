def sumar(numeroUno, numeroDos):
    return numeroUno + numeroDos

#Funcion Lambda

sumarAlternativo=lambda numeroUno,numeroDos:numeroUno+numeroDos

#Llamando funciones

resultado=sumar(5,10)

resultadolambda=sumarAlternativo(20, 10)
print (resultado)
print (resultadolambda)

def saludar (nombre):
    return 'hola',nombre

saludarAlternativo=lambda nombre:'hola'+nombre

#Emular las operaciones basicas a eleccion del usuario

lsumar=lambda n1, n2:n1+n2

resta=lambda n1,n2:n1-n2

multiplicar= lambda n1,n2:n1*n2

dividir=lambda n1,n2:n1/n2

opcion=1

while (opcion!=0):
        opcion=int(input("Digita la opcion deseada"))
        if opcion==1:
            lsumar(4,10)
        elif opcion==2:
            resta (15,5)
        elif opcion==3:
            multiplicar (12, 4)
        elif opcion==4:
            dividir(10,2)

