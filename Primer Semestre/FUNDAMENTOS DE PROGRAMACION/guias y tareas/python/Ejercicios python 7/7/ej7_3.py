acumulador_minutos = 0
acumulador_minutos_mas_de_60 = 0
acumulador_minutos_menos_de_60 = 0
contador_dia_mas_de_60_min = 0
contador_dia_menos_de_60_min = 0
dias_acumulador_minutos_mas_de_60 = 0
dias_acumulador_minutos_menos_de_60 = 0
while True:
    print("(1) Registrar días de entrenamiento.\n(2) Ver reumen.\n(3) Salir.")
    try:
        opc = int(input("Selecciona un opción:\n"))
    except ValueError:
        print("Inválido! Debes ingresar una opción válida (1, 2 o 3)")
    else:
        if opc < 1 or opc > 3:
            print("Inválido! Debes ingresar una opción válida (1, 2 o 3)")
        else:
            if opc == 1:
                while True:
                    try:
                        cantidad_días = int(input("Ingresa la cantidad de días que quieres registrar:\n"))
                    except ValueError:
                        print("Inválido! Ingresa una cantidad de días mayor que 0")
                    else:
                        if cantidad_días <= 0:
                            print("Inválido! Ingresa una cantidad de días mayor que 0")
                        else:
                            break
                for i in range(cantidad_días):
                    while True:
                        try:
                            minutos = float(input(f"Ingresa la cantidad de minutos a entrenar en el dia {i+1}:\n"))
                        except ValueError:
                            print("Inválido! Debes ingresar una cantidad numerica de minutos")
                        else:
                            if minutos <= 0:
                                print("Inválido! Debes ingresar una cantidad de minutos mayor que 0")
                            else:
                                acumulador_minutos += minutos
                                if minutos >= 60:
                                    acumulador_minutos_mas_de_60 += minutos
                                    dias_acumulador_minutos_mas_de_60 += 1
                                elif minutos < 60:
                                    acumulador_minutos_menos_de_60 += minutos
                                    dias_acumulador_minutos_menos_de_60 += 1
                                break
            elif opc == 2:
                print(f"Días registrados: {cantidad_días} días\nTotal de minutos registrados: {acumulador_minutos} min\nPromedio de minutos por día: {round((acumulador_minutos/cantidad_días),2)} min/día\nCantidad de días donde se entrena 60 min o más: {dias_acumulador_minutos_mas_de_60}\nCantidad de días donde se entrena menos de 60 min: {dias_acumulador_minutos_menos_de_60}\nCantidad de minutos entrenados (>= 60 min): {acumulador_minutos_mas_de_60}\nCantidad de minutos entrenados (< 60 min): {acumulador_minutos_menos_de_60}")
            elif opc == 3:
                pass