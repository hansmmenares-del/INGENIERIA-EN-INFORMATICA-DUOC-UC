nombre = " f a b i a n "
print(nombre[4])
print(nombre[2:6])
print(len(nombre))
print(nombre.upper())
print(nombre.lower())
print(nombre.capitalize()) # Convierte
print(nombre.strip()) # Quita espacios vacios al inicio
print(nombre.lstrip()) # Quita espacios vacios a la izquierda
print(nombre.rstrip()) # Quita espacios vacios a la derecha
print(nombre.replace("a","@").replace("n","x")) # intercambia caracter1 por caracter2.
print(nombre.find("a")) # Entrega posicion.
print(nombre.find("s")) # -1 si falla.
## Limpiar, esperar
import os
import time
import math
print(math.pi)
print("HOLA")
time.sleep(3)
os.system("cls")

nombre_2 = "cristiaan"
for i in nombre_2:
    if i == "a":
        print("Encontramos una letra 'a'... ")

input("Esperando tecla")
