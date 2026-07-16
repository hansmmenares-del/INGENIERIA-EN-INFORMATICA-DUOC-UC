total=0
is_going=True
while is_going==True:
    try:
        num=int(input("Ingresa el valor del producto. Si quieres finalizar la suma ingresa 0: $"))
    except ValueError:
        print("Error... Solo se pueden ingresar numeros enteros")
    else:
        if num!=0:
            total+=num
        else:
            is_going=False
print(f"El total es: ${total}")