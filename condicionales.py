#digitar 2 numeros diferentes y decir cual es el mayor

#nro1=int(input("numero 1: "))
#nro2=int(input("numero 2: "))

#if nro1 > nro2:
    #print(f"el nro {nro1} es mayor que {nro2}")
#else:
   # print(f"el nro {nro2} es mayor que {nro1}")
   #---------------------------------------------------------------------------------------------------

genero=int(input(" 1. masculino \n 2. Femenino \n 3. No binario \n 4. otro \n ingrese la opcion: ")) # el \n sirve para hacer un salto de linea

if genero == 1:
    print("su genero es Masculino")
elif genero == 2:
    print("su genero es Femenino")
elif genero == 3:
    print("su genero es No binario")
elif genero == 4:
    print("su genero es otro")
else:
    print("Error digitando la opcion")