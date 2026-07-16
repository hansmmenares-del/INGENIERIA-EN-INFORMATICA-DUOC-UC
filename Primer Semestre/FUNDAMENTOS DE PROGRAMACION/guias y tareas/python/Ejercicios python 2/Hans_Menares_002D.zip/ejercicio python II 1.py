def num_mayor ():
    num1 = float(input("Ingresa el primer numero:\n"))
    num2 = float(input("Ingresa el segundo numero:\n"))
    if num1>num2 and num1!=num2:
        print(f"El numero mayor es: {num1}")
    elif num1<num2 and num1!=num2:
        print(f"El numero mayor es: {num2}")
    elif num1==num2:
        print("Los numeros ingresados son iguales...")
    else:
        print("Inválido...")
    return()
num_mayor()