nota_mayor = 0
nota_menor = 8
suma_notas = 0
aprobados = 0
reprobados = 0
while True:
    print("(1) Registrar notas de estudiantes.\n(2) Mostrar estadísticas.\n(3) Salir.")
    try:
        opc = int(input("Selecciona una opción:\n"))
    except ValueError:
        print("Inválido! Debes ingresar una opción valida (1, 2 o 3)")
    else:
        if opc < 1 or opc > 3:
            print("Inválido! Debes ingresar una opción valida (1, 2 o 3)")
        else:
            if opc == 1:
                while True:
                    try:
                        cantidad_notas = int(input("Indíca la cantidad de notas a ingresar:\n"))
                    except ValueError:
                        print("Inválido! La cantidad de notas a ingresar debe ser un número mayor que 0 (No se aceptan decimáles)")
                    else:
                        if cantidad_notas <= 0:
                            print("Inválido! La cantidad de notas a ingresar debe ser un número mayor que 0")
                        else:
                            break
                for i in range(cantidad_notas):
                    while True:
                        try:
                            nota = float(input(f"Ingresa la nota número {i+1}:\n"))
                        except ValueError:
                            print("Nota Inválida! Debes ingresar las notas como decimáles con punto (ej; 6.5)")
                        else:
                            if nota < 1.0 or nota > 7.0:
                                print("Nota Inválida! El rango de notas aceptado está entre 1.0 y 7.0")
                            else:
                                if nota <= 7.0 and nota >= 4.0:
                                    aprobados += 1
                                elif nota < 4.0:
                                    reprobados += 1
                                elif nota > nota_mayor:
                                    nota_mayor = nota
                                elif nota < nota_menor:
                                    nota_menor = nota
                                suma_notas += nota
                                break
            elif opc == 2:
                print(f"Notas válidas ingresadas: {cantidad_notas}\nPromedio general: {round(suma_notas/cantidad_notas,2)}\nCantidad de aprobados: {aprobados}\nCantidad de reprobados: {reprobados}\nPorcentaje de aprobación: {round((aprobados*100/cantidad_notas),2)}%\nNota mayor: {nota_mayor}\nNota menor: {nota_menor}")
            elif opc == 3:
                break
            