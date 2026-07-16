nombre=str(input("Ingresa tu nombre completo:\n"))
print(nombre.upper())
print(nombre.lower())
# capitalized todos los nombres y apellidos
print(nombre.title())
########################################################################
# Version con 'for'.                                                   #
# Explicacion:                                                         #
# - slpit() para partir la string completa donde haya espacios         #
# - slpit() arroja una lista.                                          #
# - i.capitalize()-> convierte a mayuscula la primera letra del string #
# - + " "  -> concatena un espacio                                     #
# - , end=""  -> evita que se haga un cambio de linea (como \n)        #
#                                                                      #
#  nombre_spliteado=nombre.split()                                     #
#  for i in nombre_spliteado:                                          #
#      print(i.capitalize()+" ", end="")                               #
########################################################################
# Version con 'for' optimizado.                                        #
# Literalmente me salto el paso de asignar a una variable el split     #
# En este caso ya se asume que nombre.split() -> es una lista          #
#                                                                      #
# for i in nombre.split():                                             #
#     print(i.capitalize()+" ",end="")                                 #
########################################################################
