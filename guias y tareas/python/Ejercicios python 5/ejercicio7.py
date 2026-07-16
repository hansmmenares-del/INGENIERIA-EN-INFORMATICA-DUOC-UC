import random as ran
num,contador,suma,intentos=0,0,0,0
while True:
    num=ran.randint(1,20)
    suma+=num
    intentos+=1
    if num==13:
        break
print(f"Suma de todos los numeros: {suma}\nTotal de intentos para obtener valor de '13' fueron de: {intentos} Intentos")
    