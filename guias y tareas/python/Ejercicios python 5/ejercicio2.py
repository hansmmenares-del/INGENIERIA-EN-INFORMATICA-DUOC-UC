import random as ran
lista=[]
total=0
while total<=500:
    num=ran.randint(10,50)
    total+=num
    lista.append(num)
print(f"Suma total = {total}\nNumeros generados: {lista}")
