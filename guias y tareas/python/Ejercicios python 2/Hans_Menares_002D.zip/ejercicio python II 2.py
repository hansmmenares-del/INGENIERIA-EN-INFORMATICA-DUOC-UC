def numero_par_impar():
    num=int(input("Ingresa el numero para saber si es par o impar:\n"))
    if num%2==0:
        print(f"{num} es par.")
    elif num%2!=0:
        print(f"{num} es impar.")
    else:
        print("opcion invalida")
    return()
numero_par_impar()