lista_inventario = [stock, valor_libro]
lista_info = [titulo_del_libro, formato, genero, clasificacion, editorial, prestamo]
dic_inventario = {
    codigo: lista_inventario
}
dic_info_libros = {
    codigo: lista_info
}
def validar_int(msg_input: str, lim_inf:int, lim_sup:int, hay_lim_inf: bool, hay_lim_sup: bool) -> int:
    while True:
        try:
            num = int(input(msg_input))
        except ValueError:
            print("Inválido! Debe ingresar un _libro numérico")
        else:
            if hay_lim_inf and hay_lim_sup:
                if num < lim_inf or num > lim_sup:
                    print(f"Inválido! El rango va desde {lim_inf} a {lim_sup}")
                    continue
            elif hay_lim_inf:
                if num < lim_inf:
                    print(f"Inválido! El _libro debe ser mayor que {lim_inf}")
                    continue
            elif hay_lim_sup:
                if num > lim_sup:
                    print(f"Inválido! El _libro debe ser menor que {lim_sup}")
                    continue
            return num
def validar_str(msg_input: str) -> str:
    while True:
        errores = False
        texto = input(msg_input).strip()
        for i in texto:
            if i.isnumeric():
                errores = True
                print("Inválido! No puede contener numeros")
                break
        if texto == "":
            print("Inválido! No puede estár vacio este campo")
            continue
        if errores:
            continue
def validar_float(msg_input: str, lim_inf:float, lim_sup:float, hay_lim_inf: bool,hay_lim_sup: bool) -> float:
    while True:
        try:
            num = int(input(msg_input))
        except ValueError:
            print("Inválido! Debe ingresar un _libro numérico")
        else:
            if hay_lim_inf and hay_lim_sup:
                if num < lim_inf or num > lim_sup:
                    print(f"Inválido! El rango va desde {lim_inf} a {lim_sup}")
                    continue
            elif hay_lim_inf:
                if num < lim_inf:
                    print(f"Inválido! El _libro debe ser mayor que {lim_inf}")
                    continue
            elif hay_lim_sup:
                if num > lim_sup:
                    print(f"Inválido! El _libro debe ser menor que {lim_sup}")
                    continue
            return num
def validar_codigo(msg_input: str) -> str:
    while True:
        codigo = input(msg_input).strip().upper()
        if codigo[0] != "L":
            print("Inválido! El primer caracter debe ser una 'L'")
            continue
        if not codigo[1:3].isnumeric():
            print("Inválido! Solo se aceptan 3 _libroes numericos despues de la 'L' en el codigo")
            continue
        if len(codigo) != 4:
            print("Inválido! Solo se aceptan 4 caracteres totales en el codigo")
            continue
def agregar_libro() -> None:
    codigo_ingresado = validar_codigo("Ingresa el codigo unico del libro\nRecuerda: Debe seguir este formato 'L001' (debe iniciar con una 'L' y contener solo 3 números):")
    titulo_del_libro = validar_str("Ingrese el titulo del libro: ")
    formato = validar_str("Ingrese el formato del libro: ")
    genero = validar_str("Ingrese el genero del libro: ")
    clasificacion = validar_str("Ingrese la clasificacion de libro: ")
    editorial = validar_str("Ingrese la editorial del libro: ")
    prestamo_si_o_no = validar_int("Ingrese si está disponible para prestamo el libro\n(1) Si, está disponible.\n(2) No, no está disponible.", 1, 2, True, True)
    if prestamo_si_o_no == 1:
        prestamo = True
    elif prestamo_si_o_no == 2:
        prestamo = False
    stock = validar_int("Ingresa el stock: ", -1, 0, True, False)
    valor_libro = validar_float("Ingresa el valor del libro: $", 0, 0, True, False)
    lista_inventario = [stock, valor_libro]
    lista_info = [titulo_del_libro, formato, genero, clasificacion, editorial, prestamo]
    dic_inventario[codigo_ingresado] = lista_inventario
    dic_info_libros[codigo_ingresado] = lista_info
    return None
def buscar_libro_por_codigo(codigo_de_libro_que_se_busca: str, dic_info_libros: dict[str,list[str|int|float]]) -> dict[str,list[str|int|float]] | None:
    if codigo_de_libro_que_se_busca in dic_info_libros:
        libro_encontrado = {
            codigo_de_libro_que_se_busca: dic_info_libros[codigo_de_libro_que_se_busca]
            }
    else:
        print("No se encontró el libro con el código ingresado.\nIntente con otro código.")
    return libro_encontrado
def mostrar_todos_los_libros() -> None:
    pass
def modificar_libro(codigo_de_libro_que_se_busca: str,dic_info_libros: dict[str,list[str|int|float]], dic_inventario: dict[str,list[int|float]]) -> None:
    print("== Modificar libro ==")
    opc = validar_int("¿Qué deseas modificar?\n1. Titulo del libro.\n2. Formato.\n3. Genero.\n4. Clasificacion.\n5. Editorial.\n6. Prestamo.\n7. Stock.\n8. Valor del libro.\n9. Salir\nSelecciona una opción: ", 1, 9, True, True)
    if opc == 0:
        print("Se modificará todo:")
        dic_info_libros[codigo_de_libro_que_se_busca][0] = validar_str("Ingrese el titulo del libro: ")
        dic_info_libros[codigo_de_libro_que_se_busca][1] = validar_str("Ingrese el formato del libro: ")
        dic_info_libros[codigo_de_libro_que_se_busca][2] = validar_str("Ingrese el genero del libro: ")
        dic_info_libros[codigo_de_libro_que_se_busca][3] = validar_str("Ingrese la clasificacion de libro: ")
        dic_info_libros[codigo_de_libro_que_se_busca][4] = validar_str("Ingrese la editorial del libro: ")
        dic_info_libros[codigo_de_libro_que_se_busca][5] = validar_int("Ingrese si está disponible para prestamo el libro\n(1) Si, está 
        dic_inventario[codigo_de_libro_que_se_busca][0] = validar_int("Ingresa el stock: ", -1, 0, True, False)
        dic_inventario[codigo_de_libro_que_se_busca][1] = validar_float("Ingrese el valor del libro: ", 0.001, 0, True, False)
    elif opc == 1:
        dic_info_libros[codigo_de_libro_que_se_busca][0] = validar_str("Ingrese el titulo del libro: ")
    elif opc == 2:
        dic_info_libros[codigo_de_libro_que_se_busca][1] = validar_str("Ingrese el formato del libro: ")
    elif opc == 3:
        dic_info_libros[codigo_de_libro_que_se_busca][2] = validar_str("Ingrese el genero del libro: ")
    elif opc == 4:
        dic_info_libros[codigo_de_libro_que_se_busca][3] = validar_str("Ingrese la clasificacion de libro: ")
    elif opc == 5:
        dic_info_libros[codigo_de_libro_que_se_busca][4] = validar_str("Ingrese la editorial del libro: ")
    elif opc == 6:
        dic_info_libros[codigo_de_libro_que_se_busca][5] = validar_int("Ingrese si está disponible para prestamo el libro\n(1) Si, está disponible.\n(2) No, no está disponible.", 1, 2, True, True)
    elif opc == 7:
        dic_inventario[codigo_de_libro_que_se_busca][0] = validar_int("Ingresa el stock: ", -1, 0, True, False)
    elif opc == 8:
        dic_inventario[codigo_de_libro_que_se_busca][1] = validar_float("Ingrese el valor del libro: ", 0.001, 0, True, False)
    elif opc == 9:
        return None
def eliminar_libro(libro_a_eliminar: dict[str,list[str|int|float]]) -> None:
    pass
def mostrar_libros_por_rango_de_precio() -> None:
    pass
def menu() -> None:
    while True:
        print(f"\n1. Agregar libro.\n2. Buscar libro por código.\n3. Mostrar todos los libros.\n4. Modificar libro.\n5. Eliminar libro.\n6. Mostrar libros por rango de precio\n7. Salir.")
        opc = validar_int("Selecciona una opción: ", 1, 7, True, True)
        if opc == 1:
            agregar_libro()
        elif opc == 2:
            print("== Buscar por codigo ==")
            codigo_de_libro_que_se_busca = validar_codigo("Ingresa el codigo del libro que estas buscando: ")
            buscar_libro_por_codigo(codigo_de_libro_que_se_busca, dic_info_libros)
        elif opc == 3:
            mostrar_todos_los_libros()
        elif opc == 4:
            codigo_de_libro_que_se_busca = validar_codigo("Ingresa el codigo del libro que estas buscando para modificarlo: ")
            libro_a_modificar = buscar_libro_por_codigo(codigo_de_libro_que_se_busca, dic_info_libros)
            if libro_a_modificar != None:
                modificar_libro(codigo_de_libro_que_se_busca)
            else:
                print("No se puede modificar un libro que no existe.")
                continue
        elif opc == 5:
            libro_a_eliminar = validar_codigo("Ingresa el codigo del libro que deseas eliminar: ")
            if libro_a_eliminar != None:
                eliminar_libro(libro_a_eliminar)
            else:
                print("No se puede eliminar un libro que no existe.")
                continue
        elif opc == 6:
            mostrar_libros_por_rango_de_precio()
        elif opc == 7:
            print("xao xao")
            break