def mayor_edad():
    edad=int(input("Ingresa tu edad:\n"))
    if edad>=18:
        print("Mayor de edad")
    elif edad<18 and edad>0:
        print("Menor de edad")
    else:
        print("Aun no nace")
    return(edad)
edad=mayor_edad()