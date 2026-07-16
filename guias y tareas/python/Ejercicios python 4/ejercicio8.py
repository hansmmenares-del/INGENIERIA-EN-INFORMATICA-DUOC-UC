total=0
contador_inputs=0
while contador_inputs!=10:
    try:
        num=int(input("Ingresa el numero: "))
    except ValueError:
        print("Error... Solo se pueden ingresar numeros. ")
    else:
        contador_inputs+=1
        if num>100:
            total+=num
print(f"La suma de todos los numeros mayores que 100 ingresados es: {total}")
