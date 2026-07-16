positivos=0
negativos=0
cantidad_inputs=0
while cantidad_inputs!=10:
    try:
        num=int(input("Ingresa un numero:"))
    except ValueError:
        print("Debes ingresar numeros")
    else:
        if num>0:
            positivos+=1
            cantidad_inputs+=1
        elif num<0:
            negativos+=1
            cantidad_inputs+=1
        elif num==0:
            cantidad_inputs+=1
print(f"Positivos: {positivos}\nNegativos: {negativos}")