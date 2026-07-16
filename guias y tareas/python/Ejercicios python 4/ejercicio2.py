total=0
cantidad_inputs=0
while cantidad_inputs!=5:
    try:
        num=int(input("Ingresa los numeros uno a uno para sumarlos: "))
    except ValueError:
        print("Error... Solo se pueden ingresar numeros")
    else:
        print(f"Se sumará al total: {num}")
        cantidad_inputs+=1
        total+=num
print(f"El total de la suma es: {total}")