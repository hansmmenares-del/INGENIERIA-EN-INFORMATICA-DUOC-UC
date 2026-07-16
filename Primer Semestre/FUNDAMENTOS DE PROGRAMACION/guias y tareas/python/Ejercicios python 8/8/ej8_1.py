ESPACIOS_MAXIMOS = 60
espacios_libres = ESPACIOS_MAXIMOS
espacios_ocupados = 0
print("¡Bienvenido al sistema de gestión de espacios de Almacén Industrial!\n")
while True:
    print("====MENÚ PRINCIPAL====\n1. Espacios disponibles\n2. Ocupar espacio\n3. Liberar espacio\n4. Historial de ocupaciones\n5. Salir")
    try:
        opc = int(input("Selecciona una opción:\n"))
    except ValueError:
        print("Inválido! Debes ingresar una opcion valida dentro del rango")
    else:
        if opc < 1 or opc > 5:
            print("Inválido! Selecciona un opcion dentro del rango")
        else:
            if opc == 1:
                print(f"Espacios disponibles en Almacen: {espacios_libres} espacios")
            elif opc == 2:
                while True:
                    try:
                        a_usar = int(input("Ingresa la cantidad de espacios a utilizar:\n"))
                    except ValueError:
                        print("Inválido! Debes ingresar un cantidad positiva de espacios.")
                    else:
                        if a_usar <= 0:
                            print("No se aceptan valores negativos o cero, debes ingresar un valor positivo.")
                        elif espacios_libres < a_usar:
                            print(f"Espacio insuficiente. Quedan {espacios_libres} espacios libres en Almacén.")
                        else:
                            espacios_libres -= a_usar
                            espacios_ocupados += a_usar
                            break
            elif opc == 3:
                while True:
                    try:
                        a_liberar = int(input("Ingresa la cantidad de espacios a liberar:\n"))
                    except ValueError:
                        print("Inválido! Debes ingresar una cantidad positiva de espacios.")
                    else:
                        if a_liberar <= 0:
                            print("La cantidad de espacios a liberar debe ser mayor que 0.")
                        elif (espacios_libres + a_liberar) > ESPACIOS_MAXIMOS:
                            print("No se pueden liberar más de 60 espacios en Almacén.")
                        else:
                            espacios_libres += a_liberar
                            espacios_ocupados -= a_liberar
                            break
            elif opc == 4:
                print(f"Espacios ocupados: {espacios_ocupados}\nEspacios Libres: {espacios_libres}")
            elif opc == 5:
                print("Gracis por utilizar nuestro software, hasta la proxima.")
                break

contador_mayores_que_5 = 0     
while True:
    try:
        numero_repeticiones_for = int(input("Ingresa las veces de repeticion ciclo 'for':\n"))
    except ValueError:
        print("Inválido!!")
    else:
        if numero_repeticiones_for <= 0:
            print("Inválido!!")
        else:
            break  
for i in range(numero_repeticiones_for):
    while True:
        try:
            input_usuario = int(input("Ingresa un numero:\n"))
        except ValueError:
            print("Inválido!!")
        else:
            # CONDICIONALES DE ERROR
            if input_usuario <= 0:
                print("Inválido!!")
            elif input_usuario >= 1000:
                print("Inválido!!")
            else:
                # CONDICIONALES SI SALE BIEN
                if input_usuario > 5:
                    contador_mayores_que_5 += 1
                    break
            
            
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            