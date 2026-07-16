frase=str(input("Ingresa una frase:\n"))
print(" ".join(frase.split()[::-1]))

# " ".join(lista) -> nos va a juntar todos los objetos,
# y estaran separados solamente por un espacio.
# Esto evita que aparezca en formato lista: ['a', 'b', 'c',...].
# Con " ".join(lista) tendrá formato: a b c ...
# frase.split()[::-1] -> se divide la frase donde hayan espacios
# luego se invierte el orden de los objetos de la lista [::-1]