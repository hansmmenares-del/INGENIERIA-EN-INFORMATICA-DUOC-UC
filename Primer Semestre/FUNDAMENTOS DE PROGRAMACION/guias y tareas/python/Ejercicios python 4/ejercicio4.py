contador_inputs=0
total=0
while contador_inputs!=10:
    try:
        num=int(input(f"Ingresa el numero: "))
    except ValueError:
        print("Error... Solo se deben ingresar numeros")
    else:
        if num>0:
            total+=num
        contador_inputs+=1
print(f"La suma de los positivos es: {total}")