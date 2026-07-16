total_vendido = 0
mayores_a_1000 = 0
menores_o_iguales_a_1000 = 0
total_vendido_mayor_a_1000 = 0
total_vendido_menor_o_igual_a_1000 = 0
cantidad_de_ventas = 0
while True:
    print("(1) Ingresar ventas de productos.\n(2) Mostrar Reporte.\n(3) Salir.\n")
    try:
        opc = int(input("Selecciona una opción:\n"))
    except ValueError:
        print("Inválido! Debes ingresar una opcion válida (1, 2 o 3)")
    else:
        if opc < 1 or opc > 3:
            print("Inválido! Debes ingresar una opcion válida (1, 2 o 3)")
        else:
            if opc == 1:
                while True:
                    try:
                        registro = int(input("¿Cuántas ventas desea registrar?:\n"))
                    except ValueError:
                        print("Inválido! Debes ingresar un número mayor que 0.")
                    else:
                        if registro <= 0:
                            print("Inválido! Debes ingresar un número mayor que 0.")
                        else:
                            break
                comodin_iterable = 0
                for i in range(registro):
                    comodin_iterable += 1
                    while True:
                        try:
                            monto = int(input(f"Ingresa el monto de la venta número {comodin_iterable}:\n"))
                        except ValueError:
                            print("Monto inválido! Debes ingresar un monto mayor a 0")
                        else:
                            if monto <= 0:
                                print("Monto inválido! Debes ingresar un monto mayor a 0")
                            else:
                                if monto > 1000:
                                    mayores_a_1000 += 1
                                    total_vendido_mayor_a_1000 += monto
                                elif monto <= 1000:
                                    menores_o_iguales_a_1000 += 1
                                    total_vendido_menor_o_igual_a_1000 += monto
                                total_vendido += monto
                                break
                    cantidad_de_ventas += 1
            elif opc == 2:
                if cantidad_de_ventas >= 1:
                    promedio_ventas = total_vendido/cantidad_de_ventas
                else:
                    promedio_ventas = "No hay suficientes ventas"
                if mayores_a_1000 >= 1:
                    promedio_ventas_mayores_a_1000 = total_vendido_mayor_a_1000/mayores_a_1000
                else:
                    promedio_ventas_mayores_a_1000 = "No hay suficientes ventas mayores a 1000"
                if menores_o_iguales_a_1000 >= 1:
                    promedio_ventas_menores_o_iguales_a_1000 = total_vendido_menor_o_igual_a_1000/menores_o_iguales_a_1000
                else:
                    promedio_ventas_menores_o_iguales_a_1000 = "No hay suficientes ventas"
                print(f"Cantidad total de ventas registradas: {cantidad_de_ventas}\nCantidad de ventas mayores a 1000: {mayores_a_1000}\nCantidad de ventas menores o iguales a 1000: {menores_o_iguales_a_1000}\nPromedio de ventas: {promedio_ventas}\nPromedio de ventas mayores a 1000: {promedio_ventas_mayores_a_1000}\nPromedio de ventas menores o iguales a 1000: {promedio_ventas_menores_o_iguales_a_1000}")
            elif opc == 3:
                break
