total=0
while True:
    try:
        num=int(input("Ingresa numeros para sumar. Si quieres terminar la suma y ver el total ingresa 0: "))
    except ValueError:
        print("Error... Solo se pueden ingresar numeros.")
    else:
        total+=num
        if num==0:
            break # while True -> es una condicion verdadera, podría reemplazarse por cualquier boleano al inicio... por ejemplo: while is_going==True, luego si num==0 entonces is_going=False y se corta el ciclo
print(f"El total es: {total}")