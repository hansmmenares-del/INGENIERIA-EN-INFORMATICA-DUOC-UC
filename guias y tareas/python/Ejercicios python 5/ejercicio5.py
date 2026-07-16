import random as ran
itera,total_suma,bajo_cero,sobre_25=0,0,0,0
lista=[]
while itera!=30:
    temp=ran.randint(-5,35)
    total_suma+=temp
    if temp>25:
        sobre_25+=1
    elif temp<0:
        bajo_cero+=1
    lista.append(temp)
    itera+=1
print(f"El promedio de temperatura es: °{total_suma/len(lista)}\nSuma total de temperaturas: °{total_suma}\nCantidad de temperaturas bajo °0 son: {bajo_cero}\nCantidad de temperaturas sobre °25 son: {sobre_25}")

    
