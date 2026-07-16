import random as ran
lista=[]
contador_aleatorios=0
while contador_aleatorios!=50:
    num=ran.randint(1,6)
    contador_aleatorios+=1
    lista.append(num)
for i in range(1,6+1):
    print(f"El numero {i} aparece {lista.count(i)}")