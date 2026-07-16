while True:
    try:
        opc = int(
            input(
                "Selecciona una opción\n(1) Ejercicio 1\n(2) Ejercicio 2\n(0) Salir\n"
            )
        )
    except ValueError:
        print("Ingresa '1', '2' o '0'")
    else:
        if opc == 0:
            exit()
        elif opc != 1 and opc != 2:
            print("Opción inválida")
        else:
            if opc == 1:
                pond1 = 30
                pond2 = 40
                pond3 = 30
                pond_prom = 60
                pond_examen = 40
                while True:
                    try:
                        nota1 = float(input("Ingrese la nota de la EA1: "))
                    except ValueError:
                        print("Ingrese un valor numérico para la nota de la EA1")
                    else:
                        if nota1 < 1 or nota1 > 7:
                            print("La nota debe estar en el rango de 1.0 a 7.0")
                        else:
                            break
                while True:
                    try:
                        nota2 = float(input("Ingrese la nota de la EA2: "))
                    except ValueError:
                        print("Ingrese un valor numérico para la nota de la EA2")
                    else:
                        if nota2 < 1 or nota2 > 7:
                            print("La nota debe estar en el rango de 1.0 a 7.0")
                        else:
                            break
                while True:
                    try:
                        nota3 = float(input("Ingrese la nota de la EA3: "))
                    except ValueError:
                        print("Ingrese un valor numérico para la nota de la EA3")
                    else:
                        if nota3 < 1 or nota3 > 7:
                            print("La nota debe estar en el rango de 1.0 a 7.0")
                        else:
                            break
                promedio_pre_examen = (
                    nota1 * pond1 + nota2 * pond2 + nota3 * pond3
                ) / 100
                print(
                    f"El promedio de presentacion al examen es: {promedio_pre_examen}"
                )
                while True:
                    try:
                        nota_examen = float(input("Ingrese la nota del examen: "))
                    except ValueError:
                        print("Ingrese un valor numérico para la nota del examen")
                    else:
                        if nota_examen < 1 or nota_examen > 7:
                            print("La nota debe estar en el rango de 1.0 a 7.0")
                        else:
                            break
                promedio_final = (
                    promedio_pre_examen * pond_prom + nota_examen * pond_examen
                ) / 100
                print(f"El promedio final es: {promedio_final}")
            elif opc == 2:
                itera = 0
                pares = 0
                impares = 0
                suma_total = 0
                suma_es_mayor_a_100 = False
                suma_es_par = False
                while itera < 3:
                    try:
                        num = int(input("Ingresa un número: "))
                    except ValueError:
                        print("Ingrese un valor numérico")
                    else:
                        if num % 2 == 0:
                            pares += 1
                        else:
                            impares += 1
                        suma_total += num
                        if suma_total > 100:
                            suma_es_mayor_a_100 = True
                        if suma_total % 2 == 0:
                            suma_es_par = True
                        itera += 1
                print(
                    f"Se ingresaron {pares} números pares\nSe ingresaron {impares} números impares"
                )
                if suma_es_mayor_a_100:
                    print("La suma es mayor a 100")
                if suma_es_par:
                    print("La suma es par")
