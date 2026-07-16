contador_inputs=0
lista_num=[]
while contador_inputs!=10:
    try:
        num=int(input("Ingresa el numero: "))
    except ValueError:
        print("Error... Solo puedes ingresar numeros")
    else:
        lista_num.append(num)
        contador_inputs+=1
encontrar_repeticion=int(input("Ingresa el numero el cual quieres saber las repeticiones: "))
print(lista_num.count(encontrar_repeticion))
    