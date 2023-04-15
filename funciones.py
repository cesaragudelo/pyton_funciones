import math
def Greet():
    print("hola como estas, espero te diviertas con python")

def GreetName(nombre):
    print("Hola como estas ", nombre, "bienvenid@ al curso de python")

def Suma():
    nro1=int(input("nro1: "))
    nro2 = int(input("nro2: "))
    suma= nro1 + nro2
    print(f"la suma de {nro1} + {nro2} es de: {suma}")

def SumaDos(nro1 , nro2=55):
    suma = nro1 + nro2
    print(f"la suma de {nro1} + {nro2} es de: {suma}")

def CalcularNota(nota1,nota2,nota3):
    Definitiva=(nota1+nota2+nota3)/3
    return Definitiva

def Observacion(notaFinal):
    if notaFinal>3:
        print("gano")
    else:
        print("reprovo")
#----------funciones calificables---------------------
#indice de masa corporal
def imc():
    peso = float(input("Ingrese su peso en Kilogramos: "))
    estatura = float(input("Ingrese su estatura en metros: "))

    IMC = round(peso / math.pow(estatura, 2), 1)

    print("Su IMC es de " + str(IMC))

#factura
def subtotal(cantidad,precio):
    return cantidad*precio

def descuento(cantidad,subtotal):
    if cantidad>10:
        return (subtotal*7)/100
    else:
        return 0

def imprimir(producto,cantidad,precio,subtotal,descuento):
    print("-----------------------------------------------------------")
    print("                  Factura de pago                          ")
    print("-----------------------------------------------------------")
    print(f"producto: {producto}")
    print(f"cantidad: {cantidad}")
    print(f"precio: {precio}")
    print(f"subtotal: {subtotal}")
    print(f"descuento: {descuento}")
    print(f"total a pagar: {subtotal-descuento}")




if __name__ == '__main__':
    print("iniciando con las funciones")


    #Greet()

    #GreetName("Cesar")

   # GreetName("sara")

    #nombre = input("Digite nombre: ")

    #GreetName(nombre)

    #Suma()

    #SumaDos(40,10)

# fincion con parametro o argumento por defecto, es opcional enviar dato
# SumaDos(1)

#notaFinal= CalcularNota(4,3,5)
#print(f"nota final: {notaFinal}")
#Observacion(notaFinal)

#---------------trabajo evaluativo-------------------------------

#imc()

producto= input("ingrese el producto: ")
cantidad= int(input("ingrese la cantidad: "))
precio= float(input("ingrese el precio: "))
subtotal= subtotal(cantidad,precio)

descuento=descuento(cantidad,subtotal)

imprimir(producto,cantidad,precio,subtotal,descuento)

