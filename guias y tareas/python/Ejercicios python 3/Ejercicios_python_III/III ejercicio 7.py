frase=str(input("Ingresa una frase: \n"))
palabra=str(input("Ingresa una palabra: \n"))
print(f"La palabra ' {palabra} ' aparece {frase.lower().count(palabra.lower())} veces en la frase ingresada")
#frase.lower().count(palabra.lower())   -> convierte a minusculas la frase, cuenta las veces que aparece la palabra convertida en minusculas... podría hacerce con '.upper()' o con '.casefold()'