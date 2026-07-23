dic_info_libros = {"L001": ["Cien años de soledad", "tapa dura", "novela", "A", True, "Sudamericana"], "L002": ["El principito", "bolsillo", "infantil", "A", True, "Salamandra"], "L003": ["1984", "tapa blanda", "distopia", "B", False, "Debolsill"]}
dic_inventario_libros = {"L001": [12, 15990.0], "L002": [8, 8990.0], "L003": [5, 10990.0]}
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
            print("Inválido! El código debe tener 4 caracteres (ej: L123)")
            continue
        if codigo[0] != "L":
            print("Inválido! El código debe comenzar con la letra 'L' (ej: L123)")
            continue
        if not codigo[1:].isnumeric():
            print("Inválido! Los últimos 3 caracteres deben ser números (ej: L123)")
            continue
        return codigo
def validar_clasificacion(msg_input: str) -> str:
    while True:
        clasificacion = input(msg_input).strip().upper()
        if clasificacion not in ["A","B","C"]:
            print("Inválido! La calificación debe ser A, B o C")
            continue
        return clasificacion
def agregar_libro(dic_inventario_libros: dict[str, list[int | float]], dic_info_libros: dict[str, list[str | int | bool]]) -> None:
    print("== AGREGAR LIBRO ==")
    while True:    
        codigo = validar_codigo("Ingrese el código del libro que desea agregar (ej: L123): ")
        if codigo in dic_inventario_libros:
            print("El código ingresado ya existe. Intente nuevamente.")
            continue
        break
    nombre = validar_str("Ingrese el nombre del libro: ")
    formato = validar_str("Ingrese el formato del libro (tapa dura, tapa blanda, bolsillo): ")
    genero = validar_str("Ingrese el género del libro: ")
    calificacion = validar_clasificacion("Ingrese la calificación del libro (A, B, C): ")
    disponible = validar_int("-_Seleccion de disponibilidad_-\n1. Disponible para prestamo\n2. No disponible para préstamo\nIngrese una opción: ", True, True, 1, 2)
    editorial = validar_str("Ingrese la editorial del libro: ")
    stock = validar_int("Ingrese el stock del libro: ", True, True, 0, 1000)
    precio = validar_float("Ingrese el precio del libro: ", True, False, 0, 0)
    dic_info_libros[codigo] = [nombre, formato, genero, calificacion, disponible, editorial]
    dic_inventario_libros[codigo] = [stock, precio]
    return None
def buscar_libro_por_codigo(dic_inventario_libros: dict[str, list[int | float]], dic_info_libros: dict[str, list[str | int | bool]]) -> dict[str, list[str | int | bool | float]] | None:
    codigo = validar_codigo("Ingrese el código del libro que desea buscar (ej: L123): ")
    if codigo in dic_info_libros:
        print("LIBRO ENCONTRADO!")
        libro_encontrado = {codigo:[dic_info_libros[codigo][0], dic_info_libros[codigo][1], dic_info_libros[codigo][2], dic_info_libros[codigo][3], dic_info_libros[codigo][4], dic_info_libros[codigo][5], dic_inventario_libros[codigo][0], dic_inventario_libros[codigo][1]]}
        return libro_encontrado
    else:
        print("No se encontró ningún libro con el código ingresado.")
        return None
def mostrar_todos_los_libros(dic_inventario_libros: dict[str, list[int | float]], dic_info_libros: dict[str, list[str | int | bool]]) -> None:
    print(f"== TODOS LOS LIBROS ==")
    for i in dic_info_libros:
        print(f"--------\nCodigo: {i}\nNombre: {dic_info_libros[i][0]}\nFormato: {dic_info_libros[i][1]}\nGenero: {dic_info_libros[i][2]}\nCalificacion: {dic_info_libros[i][3]}\nDisponible: {dic_info_libros[i][4]}\nEditorial: {dic_info_libros[i][5]}\nStock: {dic_inventario_libros[i][0]}\nPrecio: {dic_inventario_libros[i][1]}\n--------")
    return None
def modificar_libro(dic_inventario_libros: dict[str, list[int | float]], dic_info_libros: dict[str, list[str | int | bool]]) -> None:
    print("== MODIFICAR LIBRO ==")
    libro_a_modificar = buscar_libro_por_codigo(dic_inventario_libros, dic_info_libros)
    if libro_a_modificar != None:
        while True:    
            codigo = validar_codigo("Ingrese el nuevo código del libro (ej: L123): ")
            if codigo in dic_inventario_libros:
                print("El código ingresado ya existe. Intente nuevamente.")
                continue
            break
        nombre = validar_str("Ingrese el nuevo nombre del libro: ")
        formato = validar_str("Ingrese el nuevo formato del libro (tapa dura, tapa blanda, bolsillo): ")
        genero = validar_str("Ingrese el nuevo género del libro: ")
        calificacion = validar_clasificacion("Ingrese la calificación nueva del libro (A, B, C): ")
        disponible = validar_int("-_Seleccion de disponibilidad_-\n1. Disponible para prestamo\n2. No disponible para préstamo\nIngrese una opción: ", True, True, 1, 2)
        editorial = validar_str("Ingrese la editorial nueva del libro: ")
        stock = validar_int("Ingrese el nuevo stock del libro: ", True, True, 0, 1000)
        precio = validar_float("Ingrese el nuevo precio del libro: ", True, False, 0, 0)
        for codigo_libro_a_borrar in libro_a_modificar:
            break
        del dic_info_libros[codigo_libro_a_borrar]
        del dic_inventario_libros[codigo_libro_a_borrar]
        dic_info_libros[codigo] = [nombre, formato, genero, calificacion, disponible, editorial]
        dic_inventario_libros[codigo] = [stock, precio]
    else:
        print("No se puede ejecutar la modificacion, libro inexistente...")
    return None
def eliminar_libro(dic_inventario_libros: dict[str, list[int | float]], dic_info_libros: dict[str, list[str | int | bool]]) -> None:
    libro_a_eliminar = buscar_libro_por_codigo(dic_inventario_libros, dic_info_libros)
    if libro_a_eliminar != None:
        for codigo in libro_a_eliminar:
            break
        del dic_info_libros[codigo]
        del dic_inventario_libros[codigo]
        print("Libro eliminado exitosamente.")
        return None
    print("No se puede ejecutar la eliminación, libro inexistente...")
def mostrar_libros_por_rango_de_precio(dic_inventario_libros: dict[str, list[int | float]], dic_info_libros: dict[str, list[str | int | bool]]) -> None:
    print("== MOSTRAR LIBROS POR RANGO DE PRECIO ==")
    lista_de_precios_y_codigo = []
    for codigo in dic_inventario_libros:
        lista_de_precios_y_codigo.append([dic_inventario_libros[codigo][1], codigo])
    lista_de_precios_y_codigo.sort()
    for i in lista_de_precios_y_codigo:
        codigo = i[1]
        print(f"--------\nCodigo: {codigo}\nNombre: {dic_info_libros[codigo][0]}\nFormato: {dic_info_libros[codigo][1]}\nGenero: {dic_info_libros[codigo][2]}\nCalificacion: {dic_info_libros[codigo][3]}\nDisponible: {dic_info_libros[codigo][4]}\nEditorial: {dic_info_libros[codigo][5]}\nStock: {dic_inventario_libros[codigo][0]}\nPrecio: {i[0]}\n--------")
    return None
def menu(msg_input: str, hay_lim_inf: bool, hay_lim_sup: bool, lim_inf: int, lim_sup: int) -> None:
    while True:
        opc = validar_int(msg_input, hay_lim_inf, hay_lim_sup, lim_inf, lim_sup)
        if opc == 1:
            agregar_libro(dic_inventario_libros, dic_info_libros)
        elif opc == 2:
            libro_encontrado = buscar_libro_por_codigo(dic_inventario_libros, dic_info_libros)
            if libro_encontrado is not None:
                for codigo in libro_encontrado:
                    break
                print(f"Codigo: {codigo}\nNombre: {libro_encontrado[codigo][0]}\nFormato: {libro_encontrado[codigo][1]}\nGenero: {libro_encontrado[codigo][2]}\nCalificacion: {libro_encontrado[codigo][3]}\nDisponible: {libro_encontrado[codigo][4]}\nEditorial: {libro_encontrado[codigo][5]}\nStock: {libro_encontrado[codigo][6]}\nPrecio: {libro_encontrado[codigo][7]}\n")
        elif opc == 3:
            mostrar_todos_los_libros(dic_inventario_libros, dic_info_libros)
        elif opc == 4:
            modificar_libro(dic_inventario_libros, dic_info_libros)
        elif opc == 5:
            eliminar_libro(dic_inventario_libros, dic_info_libros)
        elif opc == 6:
            mostrar_libros_por_rango_de_precio(dic_inventario_libros, dic_info_libros)
        elif opc == 7:
            print("PROGRAMA FINALIZADO")
            return None
menu("== MENU ==\n1. agregar libro\n2. buscar libro por código\n3. mostrar todos los libros\n4. modificar libro\n5. eliminar libro\n6. mostrar libros por rango de precio\n7. salir\nSelecciona una opción: ", True, True, 1, 7)