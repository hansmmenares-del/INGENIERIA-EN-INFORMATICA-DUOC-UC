def promedio_de_tres_numeros ():
    num1 = float(input("Ingresa el primer número:\n"))
    num2 = float(input("Ingresa el segundo número:\n"))
    num3 = float(input("Ingresa el tercer número:\n"))
    promedio_final = (num1+num2+num3)/3
    print(f"El promedio es: {promedio_final}")
    return()
promedio_de_tres_numeros()