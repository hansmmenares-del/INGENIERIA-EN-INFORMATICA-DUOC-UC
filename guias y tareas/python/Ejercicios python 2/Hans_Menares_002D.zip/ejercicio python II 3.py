def positivo_negativo():
    num=float(input("Ingrsa un numero para saber si es +, - o 0:\n"))
    if num>0:
        print("Positivo")
    elif num<0:
        print("Negativo")
    elif num==0:
        print("El numero es 0")
    else:
        print("opción inválida")
    return()
positivo_negativo()    