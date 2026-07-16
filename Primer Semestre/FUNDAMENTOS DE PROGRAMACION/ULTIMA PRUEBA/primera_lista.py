lista = [1, 2, 3, 4, 5, 6]
# print(len(lista))
# print(lista)
# print(lista[3])
# for i in lista:
#     print(i)


#### AGREGAR ELEMENTOS A UNA LISTA ####
lista.append("hola")
print(lista)

lista.insert(2, "hola")
print(lista)

lista.remove("hola") # ESPEECIFICO; SE PONE EL VALOR
# try:
#    lista()-> remove por ejemplo y da ValueError:

print(lista)
lista.pop(-1) # ESPECIFICO; SE PONE INDICE DE POSICION
print(lista)
contador = 0
for i in lista:
    if i == 4:
        print(f"ENCONTRADO EN LA POSICION: {contador}")
        lista.pop(contador)
        lista.insert(contador,10)
        break
    contador+=1
print(lista)




