texto=str(input("Ingresa un texto:\n"))
# Muchas aproximaciones...
# Considero más simple concatenar letra por letra
# .isalpha() -> si está entre a-z , mayusculas, tildes = True
# .isalpha() -> numeros, signos, espacios = False
# Entonces, 'i' debe recorrer cada caracter y revisar si es alfabetico
# Si es 'True' se concatena en texto_limpio=texto_limpio+i
texto_limpio=""
for i in texto:
    if i.isalpha()==True:
        texto_limpio=texto_limpio+i
    else:
        pass
print(texto_limpio)