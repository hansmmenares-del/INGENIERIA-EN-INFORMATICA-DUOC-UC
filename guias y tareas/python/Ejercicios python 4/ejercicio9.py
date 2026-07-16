vocales=0
palabra=str(input("Ingresa la palabra: ")).lower()
for i in palabra:
    if i in "aeiou":
        vocales+=1
print(f"Tu palabra contiene {vocales} vocales.")