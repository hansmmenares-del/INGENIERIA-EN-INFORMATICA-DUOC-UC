def num_dentro_rango():
    num=int(input("Ingresa el numero:\n"))
    if num<=100 and num>=1:
        return(True)
    else:
        return(False)
num=num_dentro_rango()
print(num)