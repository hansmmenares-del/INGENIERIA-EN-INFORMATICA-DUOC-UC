itera,positivos=0,0
while itera!=10:
    try:
        num=int(input("Ingrese un número: "))
    except ValueError:
        print("Inválido! Debes ingresar un número entero")
    else:
        itera+=1
        if num>0:
            positivos+=1
print(f"Cantidad de números positivos: {positivos}")
        
    