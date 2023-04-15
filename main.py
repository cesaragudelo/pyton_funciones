#declaracion de funcion
def Inicio():
    # Use a breakpoint in the code line below to debug your script.
    #print("hola como estas el print es para mostrar en pantalla")  # Press Ctrl+F8 to toggle the breakpoint.
    #print("vamos a conectar datos")
    #nro1=123
    #nro2=23
    #mensaje="estas sumando, "
    #formas de imprimir y concatenar.
    #print("el numero 1 es ", nro1, "y el numero 2 es ", nro2)
    #print(f"el numero 1 es  {nro1} y el numero dos es {nro2}")
    #-------------------------------------------------------------------

    #para usar numeros en operaciones debo decirle que es un numero (int--float)
    #el input me sirve como print y me captura la informacion que digitan
    #nro1= int(input("escriba numero 1 "))
    #nro2= int(input("escriba numero 2 "))
    #suma= nro1+nro2
    #print(f"{nro1} + {nro2} = {suma}")
    #---------------------------------------------------------------------

    nombre= input("ingrese el nombre: ")
    salario= float(input("ingrese su salario: "))
    nHorasTrabajadas= float(input("ingrese el numero de horas trabajadas: "))
    valorHora= float(input("ingrese el valor de la hora: "))
    netoPagar= (nHorasTrabajadas*valorHora)+salario
    print("-----------------------------------------------------------")
    print("                  Colilla de pago                          ")
    print("-----------------------------------------------------------")
    print(f"Nombre: {nombre}")
    print(f"Salario: {salario}")
    print(f"horas trabajadas: {nHorasTrabajadas}")
    print(f"valor hora: {valorHora}")
    print(f"Neto a pagar: {netoPagar}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Inicio()
