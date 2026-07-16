import random as ran
itera,pares,impares=0,0,0
lista=[]
while itera!=100:
    itera+=1
    num=ran.randint(1,100)
    lista.append(num)
    if num%2==0:
        pares+=1
    else:
        impares+=1
print(f"Cantidad de pares: {pares}\nCantidad de impares: {impares}")