dic_general = {
    "inventario": [],
    "libros": []
}
def validar_int(msg_input: str, hay_lim_inf: bool, hay_lim_sup: bool, lim_inf: int, lim_sup: int) -> int:
    while True:
        try:
            num = int(input(msg_input))
        except ValueError:
            print("Inválido! Debe ingresar un valor numérico.")
        else:
            if hay_lim_inf:
                if num < lim_inf:
                    print(f"Inválido! Debe ingresar un valor numérico mayor que {lim_inf}.")
                    continue
            elif hay_lim_inf and hay_lim_sup:
                if num < lim_inf or num > lim_sup:
                    print(f"Inválido! Debe ingresar un valor numérico entre {lim_inf} y {lim_sup}.")
                    continue
            elif hay_lim_sup:
                if num > lim_sup:
                    print(f"Inválido! Debe ingresar un valor numérico menor o igual a {lim_sup}.")
                    continue
            return num
def validar_float(msg_input: str, hay_lim_inf: bool, hay_lim_sup: bool, lim_inf: float, lim_sup: float) -> float:
    while True:
        try:
            num = float(input(msg_input))
        except ValueError:
            print("Inválido! Debe ingresar un número decimal.")
        else:
            if hay_lim_inf:
                if num < lim_inf:
                    print(f"Inválido! Debe ingresar un valor numérico mayor que {lim_inf}.")
                    continue
            elif hay_lim_inf and hay_lim_sup:
                if num < lim_inf or num > lim_sup:
                    print(f"Inválido! Debe ingresar un valor numérico entre {lim_inf} y {lim_sup}.")
                    continue
            elif hay_lim_sup:
                if num > lim_sup:
                    print(f"Inválido! Debe ingresar un valor numérico menor o igual a {lim_sup}.")
                    continue
            return num
def validar_str(msg_input: str, es_codigo: bool) -> str:
    while True:
        errores = False
        texto = input(msg_input).strip().title()
        if es_codigo:
            if len(texto) == 0:
                print("Inválido! El campo no puede estar vacío.")
                continue
            else:
                return texto
        for i in texto:
            if i.isdigit():
                print("Inválido! El campo no puede contener números.")
                errores = True
                break
        if len(texto) == 0:
            print("Inválido! El campo no puede estar vacío.")
            continue
        if not errores:
            return texto
def funcion_de_agregar_libro(codigo_libro: str, precio: float, stock: int, titulo_del_libro: str, formato: str, genero: str, clasificacion: str, disponibilidad_para_prestamo: bool, editorial: str, destino: dict[str, list[dict[str, list[str|float|int|bool]]]]) -> None:
    """Funcion que crea ambos diccionarios (uno para inventario y otro para información del libro) y los agrega a un diccionario general a su key correspondiente."""
    para_inventario = {
        codigo_libro: [stock, precio]
        }
    para_libro_info = {
        codigo_libro: [
            titulo_del_libro,
            formato,
            genero,
            clasificacion,
            disponibilidad_para_prestamo,
            editorial]
        }
    destino["inventario"].append(para_inventario)
    destino["libros"].append(para_libro_info)
    print(f"\nSe ha agregado el libro con código {codigo_libro} al inventario con los siguientes datos:\nPrecio: {precio}\nStock: {stock}\nTítulo del libro: {titulo_del_libro}\nFormato: {formato}\nGénero: {genero}\nClasificación: {clasificacion}\nDisponibilidad para préstamo: {disponibilidad_para_prestamo}\nEditorial: {editorial}")
def agregar_libro() -> None:
    # Explicacion: 'dic_general' es un diccionario con dos 'keys': 'inventario' y 'libros'.
    # 'inventario' es una key y su valor es una lista de diccionarios.
    # Cada diccionario dentro de la lista tiene como key el código del libro para identificarlo.
    # Lo mismo ocurre con 'libros'.
    
    # Visualizacion mental de cómo va quedando:
    # dic_general = {
    #   key1: [
    #           {libro_1: [a,b]},
    #           {libro_2: [a,b]},
    #               ...
    #       ],
    #   key2: [
    #           {libro_1: [a,b,c,d,e,f]},
    #           {libro_2: [a,b,c,d,e,f]},
    #               ...
    #       ]
    #  }
    codigo_libro = validar_str("Ingrese el código del libro: ", True)
    precio = validar_float("Ingrese el precio del libro: ", True, False, 0.01, 0)
    stock = validar_int("Ingrese el stock del libro: ", True, False, -1, 0)
    titulo_del_libro = validar_str("Ingrese el título del libro: ", False)
    formato = validar_str("Ingrese el formato del libro: ", False)
    genero = validar_str("Ingrese el género del libro: ", False)
    clasificacion = validar_str("Ingrese la clasificación del libro: ", False)
    opc = validar_int("Disponibilidad de prestamo\n(1) Disponible\n(0) No disponible\n(Recuerde, si tiene 0 stock se asigna automaticamente como 'No disponible')\nSeleccione una opción: ", True, True, 0, 1)
    if opc == 1:
        disponibilidad_para_prestamo = True
    elif opc == 0:
        disponibilidad_para_prestamo = False
    editorial = validar_str("Ingrese la editorial del libro: ", False)
    funcion_de_agregar_libro(codigo_libro, precio, stock, titulo_del_libro, formato, genero, clasificacion, disponibilidad_para_prestamo, editorial, dic_general)
    return None
def buscar_libro_por_codigo(dic_general: dict[str, list[dict[str, list[str|float|int|bool]]]]) -> dict[str, list[str|float|int|bool]] | None:
    libro_a_buscar = validar_str("Ingrese el código del libro a buscar: ", True)
    for libro in dic_general["libros"]:
        if libro_a_buscar in libro:
            print(f"\nLIBRO ENCONTRADO '{libro_a_buscar}'.\nTítulo del libro: {libro[libro_a_buscar][0]}\nFormato: {libro[libro_a_buscar][1]}\nGénero: {libro[libro_a_buscar][2]}\nClasificación: {libro[libro_a_buscar][3]}\nDisponibilidad para préstamo: {libro[libro_a_buscar][4]}\nEditorial: {libro[libro_a_buscar][5]}")
            return libro
    print(f"LIBRO NO ENCONTRADO... NO EXISTE LIBRO CODIGO: {libro_a_buscar}")
    return None
def mostrar_todos_los_libros(ver_inventario_o_info: int) -> None:
    if ver_inventario_o_info == 1:
        ver_contenido = "inventario"
        for libro in dic_general[ver_contenido]:
            print(f"= MOSTRAR TODO ==\nCODIGO")
    elif ver_inventario_o_info == 2:
        ver_contenido = "libros"
        for libro in dic_general[ver_contenido]:
            print(f"= MOSTRAR TODO ==\nCODIGO: {libro[0]}\nTITULO: {libro[1]}\nFORMATO: {libro[1]}\nGénero: {libro[2]}\nClasificación: {libro[3]}\nDisponibilidad para préstamo: {libro[4]}\nEditorial: {libro[5]}")
def modificar_libro():
    pass
def eliminar_libro():
    pass
def mostrar_libros_por_rango_de_precio():
    pass
def menu():
    while True:
        print(f"\n1. Agregar libro.\n2. Buscar libro por código.\n3. Mostrar todos los libros.\n4. Modificar libro.\n5. Eliminar libro.\n6. Mostrar libros por rango de precio\n7. Salir.")
        opc = validar_int("Selecciona una opción: ", True, True, 1, 7)
        if opc == 1:
            agregar_libro()
        elif opc == 2:
            codigo_ingresado = validar_int("Ingrese el código del libro a buscar: ", True, False, 1, 0)
            buscar_libro_por_codigo(dic_general)
        elif opc == 3:
            opc = validar_int("Deseas ver:\n(1) Inventario.\n(2) Información de libros.", True, True, 1, 2)
            if opc == 1:
                mostrar_todos_los_libros(1)
            elif opc == 2:
                mostrar_todos_los_libros(2)
            continue
        elif opc == 4:
            modificar_libro()
        elif opc == 5:
            eliminar_libro()
        elif opc == 6:
            mostrar_libros_por_rango_de_precio()
        elif opc == 7:
            print("xao xao :D")
            break
menu()