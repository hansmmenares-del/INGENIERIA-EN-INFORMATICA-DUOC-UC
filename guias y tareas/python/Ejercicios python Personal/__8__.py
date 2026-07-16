frase=str(input("Ingresa la frase:\n"))
tratamiento=frase.strip().lower().replace(" ","")
left_tratamiento=tratamiento[::-1]
print(left_tratamiento)
if tratamiento==left_tratamiento:
    print("Es palindromo")
else:
    print("No es palindromo")

