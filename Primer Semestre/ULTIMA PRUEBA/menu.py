def validar_enteros_positivos(msg:str):
    while True:
        try:
            valor = int(input(msg))
            if valor == 0:
                print("El valor no puede ser 0")
            elif valor < 0:
                print("El valor no puede ser negativo")
            else:
                return valor
        except ValueError:
            print("Solo se permiten números enteros")
def sumar(num1, num2):
    return(num1+num2)
while True:
    print("1. Sumar\n2. Restar\n3. Dividar\n4. Multiplicar\n5. Salir")
    opc = validar_enteros_positivos("ingrese una opción: ")
    if opc == 1:
        num1 = validar_enteros_positivos("Ingresa el primer valor: ")
        num2 = validar_enteros_positivos("Ingresa el segundo valor: ")
        print(f"La suma entre {num1} + {num2} = {sumar(num1,num2)}")    