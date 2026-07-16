import random as ran
itera,sellos,caras,puntos=0,0,0,0
while itera!=100:
    itera+=1
    moneda=ran.randint(0,1)
    if moneda==0:
        sellos+=1
    else:
        caras+=1
        puntos+=2
print(f"Puntaje jugador: {puntos}\nCantidad sellos: {sellos}\nCantidad caras : {caras}")