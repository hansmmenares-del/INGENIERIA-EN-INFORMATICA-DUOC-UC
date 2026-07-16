import random as ran
itera,zona_baja,zona_media,zona_alta=0,0,0,0
while itera!=60:
    itera+=1
    num=ran.randint(1,100)
    if num>=1 and num<=33: # Tambien podría ser: if num in range(inicio,final+1)
        zona_baja+=1
    elif num>=34 and num<=66:
        zona_media+=1
    elif num>=67 and num<=100:
        zona_alta+=1
print(f"Zona Alta: {zona_alta}\nZona Media: {zona_media}\nZona Baja: {zona_baja}")