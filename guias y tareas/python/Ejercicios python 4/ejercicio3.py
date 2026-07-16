contador_inputs=0
pares=0
while contador_inputs!=8:
    try:
        num=int(input("Ingresa los numeros uno a uno: "))
    except ValueError:
        print("Error... Solo debes ingresar numeros enteros")
    else:
        if num%2==0:
            pares+=1
            print(f"{num} es Par")
        else:
            print(f"{num} es Impar")
        contador_inputs+=1
print(f"Cantidad de numeros pares: {pares}")
