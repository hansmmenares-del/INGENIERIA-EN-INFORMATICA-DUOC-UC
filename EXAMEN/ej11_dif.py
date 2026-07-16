dic_info_libros = {
    'L001': ['Cien años de soledad', 'tapa dura', 'novela', 'A', True, 'Sudamericana'],
    'L002': ['El principito', 'bolsillo', 'infantil', 'A', True, 'Salamandra'],
    'L003': ['1984', 'tapa blanda', 'distopia', 'B', False, 'Debolsillo']
    }
dic_inventario_libros = {
    'L001': [12, 15990],
    'L002': [8, 8990],
    'L003': [5, 10990]
    }
# titulo_del_libro, formato, genero, clasificacion, disponibilidad_para_prestamo, editorial
def validar_int(msg_input: str, hay_lim_inf: bool, hay_lim_sup: bool, lim_inf: int, lim_sup: int) -> int:
    while True:
        try:
            num = int(input(msg_input))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico")
        else:
            if hay_lim_inf and hay_lim_sup:
                if num < lim_inf or num > lim_sup:
                    print(f"Inválido! Debes ingresar un valor entre {lim_inf} y {lim_sup}")
                    continue
            elif hay_lim_sup:
                if num > lim_sup:
                    print(f"Inválido! Debes ingresar un valor menor que {lim_sup}")
                    continue
            elif hay_lim_inf:
                if num < lim_inf:
                    print(f"Inválido! Debes ingresar un valor mayor que {lim_inf}")
                    continue
            return num
def validar_str(msg_input: str) -> str:
    while True:
        errores = False
        texto = input(msg_input).strip()
        for i in texto:
            if i.isnumeric():
                print("Inválido! Este campo no puede contener numeros")
                errores = True
                break
        if texto == "":
            print("Inválido! Este campo no puede estar vacío")
            continue
        if not errores:
            return texto
def validar_float(msg_input: str, hay_lim_inf: bool, hay_lim_sup: bool, lim_inf: float, lim_sup: float) -> float:
    while True:
        try:
            num = float(input(msg_input))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico")
        else:
            if hay_lim_inf and hay_lim_sup:
                if num < lim_inf or num > lim_sup:
                    print(f"Inválido! Debes ingresar un valor entre {lim_inf} y {lim_sup}")
                    continue
            elif hay_lim_sup:
                if num > lim_sup:
                    print(f"Inválido! Debes ingresar un valor menor que {lim_sup}")
                    continue
            elif hay_lim_inf:
                if num < lim_inf:
                    print(f"Inválido! Debes ingresar un valor mayor que {lim_inf}")
                    continue
            return num
def validar_codigo(msg_input: str) -> str:
    while True:
        codigo = input(msg_input).strip().upper()

        if len(codigo) != 4:
            print("Inválido. El código debe tener el formato L001.")
            continue

        if codigo[0] != "L":
            print("Inválido. Debe comenzar con la letra L.")
            continue

        if not codigo[1:].isdigit():
            print("Inválido. Debe contener tres números.")
            continue

        return codigo
def agregar_libro(dic_destino_inventario_libros: dict[int, list[int|float]], dic_destino_info_libros: dict[int, list[str|bool]]) -> None:
    while True:
        codigo_ingresado = validar_int("Ingresa el codigo del libro: ", True, False, -1, 0)
        if codigo_ingresado in dic_destino_inventario_libros:
            print("Inválido! El codigo ya existe, intenta ingresando otro.")
        else:
            break
    titulo_del_libro = validar_str("Ingresa el titulo del libro: ", True)
    formato = validar_str("Ingresa el formato del libro: ", False)
    genero = validar_str("Ingresa el genero del libro: ", False)
    clasificacion = validar_str("Ingresa la clasificacion del libro: ", True)
    editorial = validar_str("Ingresa el titulo del libro: ", False)
    prestamo = validar_int("(1) Si, está disponible para prestamo.\n(2) No, no está disponible para prestamo.\nSelecciona una opcion para continuar: ", True, True, 0, 1)
    stock = validar_int("Ingrese el stock del libro: ", True, False, 0, 0)
    valor = validar_float("Ingrese el valor del libro (valor por unidad): ", True, False, 0.001, 0)
    if stock != 0:
        if prestamo == 1:
            disponibilidad_para_prestamo = True
        elif prestamo == 2:
            disponibilidad_para_prestamo = False
    else:
        disponibilidad_para_prestamo = False
        
    lista_info_libro = [titulo_del_libro, formato, genero, clasificacion, disponibilidad_para_prestamo, editorial]
    lista_inventario_libro = [stock, valor]
    dic_destino_info_libros[codigo_ingresado] = lista_info_libro
    dic_destino_inventario_libros[codigo_ingresado] = lista_inventario_libro
    return None
def buscar_libro_por_codigo(dic_destino_inventario_libros: dict[int, list[int|float]], dic_destino_info_libros: dict[int, list[str|bool]]):
    codigo_ingersado = validar_int("Ingresa el codigo del libro que buscas: ", True, False, 0, )
def mostrar_todos_los_libros(diccionario_inventario:dict[str, str|int|float|bool]):
    for libro in diccionarios.
    print(f"{dic_info_libros[libro]}{dic_inventario_libros}")
def modificar_libro():
    pass
def eliminar_libro():
    pass
def mostrar_libros_por_rango_de_precio():
    pass
def menu() -> None:
    while True:
        print(f"\n1. Agregar libro.\n2. Buscar libro por código.\n3. Mostrar todos los libros.\n4. Modificar libro.\n5. Eliminar libro.\n6. Mostrar libros por rango de precio\n7. Salir.")
        opc = validar_int("Selecciona una opción: ")
        if opc == 1:
            agregar_libro()
        elif opc == 2:
            buscar_libro_por_codigo()
        elif opc == 3:
            mostrar_todos_los_libros()
        elif opc == 4:
            modificar_libro()
        elif opc == 5:
            eliminar_libro()
        elif opc == 6:
            mostrar_libros_por_rango_de_precio()
        elif opc == 7:
            print("xao xao")
            break