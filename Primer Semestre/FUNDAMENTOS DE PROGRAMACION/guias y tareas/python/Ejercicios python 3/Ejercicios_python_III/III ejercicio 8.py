cadena_texto=str(input("Ingresa una cadena de texto:\n"))
print(f"CADENA ORIGINAL:\n{cadena_texto}")
# 'i' tiene que recorrer numeros, no caracteres.
# Por lo tanto el rango que recorre debe ser desde 0 hasta la ultima posicion.
# len()-> obtiene cantidad de caracteres totales
# podría incluirse range(0, len(cadena_texto, 2)) siendo el '2' el salto, pudiendo evitar i%2.
# i%2==0 -> para filtrar posiciones pares.
print("CADENA MODIFICADA:")
for i in range(0, len(cadena_texto)):
    if i%2==0:
        print(cadena_texto[i],end="")  
    else:
        pass
### Forma incluso más simplificada:
# print(cadena_texto[::2]) -> inicio:final:paso