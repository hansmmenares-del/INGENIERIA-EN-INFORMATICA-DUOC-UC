itera,pares=0,0
while itera!=8:
    try:
        num=int(input("Ingresa un número:"))
    except ValueError:
        print("Inválido! Debes ingresar un número entero")
    else:
        itera+=1
        if num%2==0:
            pares+=1
print(f"Cantidad de números pares: {pares}")