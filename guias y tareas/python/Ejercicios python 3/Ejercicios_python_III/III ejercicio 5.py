palabra=str(input("Ingresa una palabra para ver los caracteres en la posicion 2, 4 y 6:\n"))
if len(palabra)<6:
    print(f"Palabra ingresada tiene menos de 6 caracteres.\nCARACTERES\nPosicion 2: {palabra[2]}\nPosicion 4: {palabra[4]}")
elif len(palabra)>=6:
    print(f"CARACTERES\nPosicion 2: {palabra[2]}\nPosicion 4: {palabra[4]}\nPosicion 6: {palabra[6]}")
