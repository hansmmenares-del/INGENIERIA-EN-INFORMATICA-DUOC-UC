cont_inputs=0
cont_mult_de_tres=0
while cont_inputs!=15:
    try:
        num=int(input("Ingresa un numero: "))
    except ValueError:
        print("Error... Solo se pueden ingresar numeros.")
    else:
        if num%3==0:
            cont_mult_de_tres+=1
        cont_inputs+=1
print(f"La cantidad de numeros ingresados que son multiplos de 3 son: {cont_mult_de_tres}")
            
        