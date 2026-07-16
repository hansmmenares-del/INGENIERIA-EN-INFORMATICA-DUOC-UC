litros_totales = 0
contador_meses_sup_a_15000L = 0
contador_meses_men_o_igual_15000L = 0
litros_sup_15000L = 0
litros_men_o_igual_15000L = 0
while True:
    print("(1) Registrar consumo mensual\n(2) Mostrar informe\n(3) Salir")
    try:
        opc = int(input("Selecciona una opción:\n"))
    except ValueError:
        print("Inválido! Debes seleccionar una opción válida (1, 2 o 3)")
    else:
        if opc < 1 or opc > 3:
            print("Inválido! Debes seleccionar una opción válida (1, 2 o 3)")
        else:
            if opc == 1:
                while True:
                    try:
                        meses = int(input("Ingresa la cantidad de meses que deseas registrar:\n"))
                    except ValueError:
                        print("Inválido! Debes ingresar una cantidad de meses mayor que 0")
                    else:
                        if meses <= 0:
                            print("Inválido! Debes ingresar una cantidad de meses mayor que 0")
                        else:
                            break
                for i in range(meses):
                    while True:
                        try:
                            litros = float(input(f"Ingresa la cantidad de litros consumidos en el mes {i+1}:\n"))
                        except ValueError:
                            print("Inválido! Debes ingresar una cantidad de litros positiva o 0 (decimales deben ir con punto)")
                        else:
                            if litros < 0:
                                print("Inválido! Debes ingresar una cantidad de litros positiva o 0 (decimales deben ir con punto)")
                            else:
                                litros_totales += litros
                                if litros > 1500:
                                    litros_sup_15000L += litros
                                    contador_meses_sup_a_15000L += 1
                                elif litros <= 1500:
                                    litros_men_o_igual_15000L += litros 
                                    contador_meses_men_o_igual_15000L += 1
                                break     
            elif opc == 2:
                print(f"Total consumido: {litros_totales} Litros\nPromedio mensual: {round((litros_totales/meses),2)} Litros/mes\nCantidad de meses donde consumo > 1500L: {contador_meses_sup_a_15000L}\nCantidad de meses donde consumo <= 1500L: {contador_meses_men_o_igual_15000L}")
            elif opc == 3:
                break