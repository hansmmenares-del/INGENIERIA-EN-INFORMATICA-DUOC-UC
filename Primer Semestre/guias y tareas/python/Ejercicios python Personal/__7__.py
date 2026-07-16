### convertidor de texto: Elimina cualquier cosa a menos que sea alfabetico
entrada=str(input("Ingresa el texto:\n"))
texto_limpio=""
len_text=len(entrada.strip().lower())
for i in range(len_text):
    if entrada.strip().lower()[i].isalpha():
        texto_limpio+=entrada.strip().lower()[i]
    elif entrada.strip().lower()[i].isspace():
        if i+1<=len_text and entrada.strip().lower()[i+1].isspace()==False:
            texto_limpio+=entrada.strip().lower()[i]
print(texto_limpio.capitalize())