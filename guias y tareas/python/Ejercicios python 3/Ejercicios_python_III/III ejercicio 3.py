frase=str(input("Ingresa la frase:\n"))
opc=int(input("\nDe qué lado deseas borrar los espacios?: Selecciona una opción\n(1) Lado derecho: \n(2) Lado Izquierdo:\n"))
if opc==1:
    print(f"Frase sin espacios a la derecha: {frase.rstrip()}")
elif opc==2:
    print(f"Frase sin espacios a la izquierda: {frase.lstrip()}")
else:
    print("Opción Inválida")
print(f"Frase sin espacios a la derecha y sin espacios a la izquierda: {frase.strip()}")
if frase.strip().find("Python")>=0:
    print(f"Se encontró 'Python' en la posicion: {frase.strip().find("Python")}")
elif frase.strip().find("Python")==-1:
    print("No se encontró 'Python'")
else:
    print("Inválido")