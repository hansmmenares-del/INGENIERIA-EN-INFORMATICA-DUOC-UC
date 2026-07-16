import random as ran
itera,total=0,0
while itera!=40:
    itera+=1
    num=ran.randint(1,200)
    if num%5==0:
        total+=num
print(f"La suma de los mutliplos de 5 es: {total}")