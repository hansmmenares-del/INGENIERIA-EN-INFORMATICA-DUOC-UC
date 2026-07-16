import random as ran
itera,contador=0,0
while itera!=80:
    itera+=1
    num=ran.randint(1,100)
    if num>30 and num<70:
        contador+=1
print(f"La cantidad de numeros aleatorios entre 30 y 70 son: {contador}")