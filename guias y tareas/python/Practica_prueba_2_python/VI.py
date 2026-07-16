(
    num,
    rondas_ingresadas,
    ronda_completada,
    pares,
    impares,
    suma_pares,
    suma_impares,
    suma_todo_nums,
    mayor_50,
    num_valido,
    energia_alta,
    energia_par,
    energia_triple,
    energia_simple,
) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
lista_nums = []
rondas_uncheck = True
print("----- PANEL DE ENERGÍA -----\n")
while rondas_uncheck:
    if num == 666:
        break
    try:
        rondas_ingresadas = int(input("Ingresa el número de rondas: "))
    except ValueError:
        print("Debes ingresar un número entero mayor que 0")
    else:
        if rondas_ingresadas <= 0:
            print("Debes ingresar un número entero mayor que 0")
        else:
            rondas_uncheck = False
while rondas_ingresadas != ronda_completada:
    if num == 666:
        break
    ronda_iniciada = True
    while ronda_iniciada:
        try:
            num = int(input("Ingresa un número positivo: "))
        except ValueError:
            print("Inválido! Debes ingresar un número mayor que 0")
        else:
            if num <= 0:
                print(
                    "El número ingresado es negativo. Debes ingresar un número mayor que 0"
                )
            else:
                ronda_iniciada = False
                num_valido += 1
                if num == 666:
                    break
                if num > 50:
                    mayor_50 += 1
                if num % 2 == 0:
                    pares += 1
                    suma_pares += num
                else:
                    impares += 1
                    suma_impares += num
    if num % 2 == 0 and num % 3 == 0:
        print("Enería Alta")
        energia_alta += 1
    elif num % 2 == 0:
        print("Energía Par")
        energia_par += 1
    elif num % 3 == 0:
        print("Energía Triple")
        energia_alta += 1
    else:
        print("Energía Simple")
        energia_simple += 1
    if num >= 1 and num <= 20:
        print("Número ingresado es pequeño")
    elif num >= 21 and num <= 50:
        print("Número ingresado es mediano")
    elif num < 50:
        print("Número ingresado es grande")
    lista_nums.append(num)
    suma_todo_nums += num
    ronda_completada += 1
numero_mayor = max(lista_nums)
numero_menor = min(lista_nums)
print(
    f"RESUMEN FINAL:\nTotal de números válidos ingresados: {num_valido}\nCantidad de números en cada categoria de energía:\nEnergía Alta: {energia_alta}\nEnergía Par: {energia_par}\nEnergía Triple: {energia_triple}\nEnergía Simple: {energia_simple}\nCantidad de números pares: {pares}\nCantidad de números impares: {impares}\nCantidad de números mayores que 50: {mayor_50}\nNúmero mayor: {numero_mayor}\nNúmero menor: {numero_menor}\nSuma de todos los números: {suma_todo_nums}\nSuma de todos los números pares: {suma_pares}\nSuma de todos los números impares: {suma_impares}\nPromedio general de los números ingresados: {suma_todo_nums / num_valido}\nRondas jugadas: {ronda_completada} de {rondas_ingresadas}"
)
