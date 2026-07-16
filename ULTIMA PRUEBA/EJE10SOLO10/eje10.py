
lista_de_juegos = []
def validar_int(msg_input: str, msg_de_error: str, msg_out_of_bounds: str, hay_lim_inf: bool, hay_lim_sup: bool, lim_inf: int|float, lim_sup: int|float) -> int|float:
    while True:
        try:
            num = int(input(msg_input))
        except ValueError:
            print(msg_de_error)
        else:
            if hay_lim_inf:
                if num < lim_inf:
                    print(msg_out_of_bounds)
                    continue
            elif hay_lim_inf and hay_lim_sup:
                if num < lim_inf or num > lim_sup:
                    print(msg_out_of_bounds)
                    continue
            elif hay_lim_sup:
                if num > lim_sup:
                    print(msg_out_of_bounds)
                    continue
            return num
def validar_str(msg_input: str, msg_vacio: str, msg_tiene_numeros: str) -> str:
    while True:
        errores = False
        texto = input(msg_input).strip()
        for i in texto:
            if i.isnumeric():
                print(msg_tiene_numeros)
                errores = True
                break
        if errores:
            continue
        if texto == "":
            print(msg_vacio)
            continue
        return texto
def codigo_anterior(lista_para_analizar: list) -> int:
    lista_para_obtener_codigo_anterior = []
    codigo_anterior = 1000
    for vj in lista_para_analizar:
        lista_para_obtener_codigo_anterior.append(vj["codigo"])
    if len(lista_para_obtener_codigo_anterior) == 0:
        return codigo_anterior
    else:
        codigo_anterior = max(lista_para_obtener_codigo_anterior)
        return codigo_anterior
def agregar_vj(lista_donde_ira_vj_nuevo: list):
    codigo = codigo_anterior(lista_de_juegos)
    titulo = validar_str(
        "Ingresa el titulo del vj: ",
        "Inválido! No puede estar vacío el titulo del vj.",
        "Inválido! No puede contener números el titulo"
        )
    genero = validar_str(
        "Ingresa el genero del vj: ",
        "Inválido! No puede estar vacío el genero del vj.",
        "Inválido! No puede contener números el genero del vj")
    precio = validar_int(
        "Ingresa el precio del vj: $",
        "Inválido! Solo se permiten valores numéricos",
        "Inválido! El valor debe ser mayor que 0",
        True, False, 0.0001, 0
        )
    stock = validar_int(
        "Ingresa la cantidad de stock del vj: ",
        "Inválido! Solo se permiten valores numéricos",
        "Inválido! El valor debe ser mayor que 0",
        True, False, 0, 9
        )
    dic_juego = {
    "codigo": codigo,
    "titulo": titulo,
    "genero": genero,
    "precio": precio,
    "stock": stock
}
    lista_donde_ira_vj_nuevo.append(dic_juego)
    print("¡Se agrego el juego con exito!")
def buscar_vj(key_de_busqueda: str, lista_para_busqueda: list) -> dict[str, str|int]|None:
    if key_de_busqueda == "por_codigo":
        codigo_a_buscar = validar_int(
            "Ingrese el codigo para encontrar el vj: ",
            "Inválido! Solo se permiten valores numéricos",
            "Inválido! Los codigos empiezan desde el 1000 en adelante",
            True, False, 1000, 0
            )
        for vj in lista_para_busqueda:
            if codigo_a_buscar == vj["codigo"]:
                print("¡VJ ENCONTRADO!")
                print(
                    f"== RESULTADO ==\n- CODIGO: {vj["codigo"]}\n- TITULO: {vj["titulo"]}\n- GENERO: {vj["genero"]}\n- PRECIO: {vj["stock"]}\n- STOCK: {vj["stock"]}\n- PRECIO UNITARIO: {vj["precio"]}\n-- PRECIO TOTAL (stock*precio): {vj["precio"]*vj["stock"]}"
                    )
                return vj
            else:
                print("VJ NO ENCONTRADO")
                return None
    elif key_de_busqueda == "por_titulo":
        titulo_a_buscar = validar_str(
            "Ingresa el titulo del vj: ",
            "Inválido! No puede estar vacio el campo de busqueda",
            "Inválido! No se permiten numéros en este campo"
            )
        for vj in lista_para_busqueda:
            if titulo_a_buscar == vj["titulo"]:
                print("¡VJ ENCONTRADO!")
                print(
                    f"== RESULTADO ==\n- CODIGO: {vj["codigo"]}\n- TITULO: {vj["titulo"]}\n- GENERO: {vj["genero"]}\n- PRECIO: {vj["stock"]}\n- STOCK: {vj["stock"]}\n- PRECIO UNITARIO: {vj["precio"]}\n-- PRECIO TOTAL (stock*precio): {vj["precio"]*vj["stock"]}"
                    )
                return vj
            else:
                print("VJ NO ENCONTRADO")
                return None
def ventas(diccionario_de_vj: dict[str, str|int]) -> int | None:
    vj = diccionario_de_vj
    if vj["stock"] == 0:
        print("No es posible vender, hay 0 ejemplares del juego")
        return None
    else:
        cantidad_ejemplares_venta = validar_int(
            "Ingrese la cantidad de ejemplares a vender: ",
            "Inválido! Solo se permiten valores numéricos",
            "Inválido! La cantidad de ventas no puede ser un numero negativo",
            True, True, 0, int(vj["stock"]))
        if vj["stock"] - cantidad_ejemplares_venta < 0:
            print("No es posible hacer la venta.")
            return None
        else:
            print(
            f"Cantidad de ejemplares vendidos: {cantidad_ejemplares_venta}\nPrecio total: {cantidad_ejemplares_venta*float(vj["precio"])}"
            )
            return cantidad_ejemplares_venta
def mostrar_todo_el_intenvario(lista_a_mostrar: list) -> None:
    for vj in lista_a_mostrar:
        print(f"- CODIGO: {vj["codigo"]}\n- TITULO: {vj["titulo"]}\n- GENERO: {vj["genero"]}\n- STOCK: {vj["stock"]}\n- PRECIO: {vj["precio"]}\n-- PRECIO TOTAL (stock*precio): {vj["stock"]*vj["precio"]}")
def menu(lista_de_juegos_enuso) -> None:
    while True:
        print(
            "== MENU ==\n(1) Agregar vj.\n(2) Registrar venta de vj.\n(3) Mostrar todo el inventario.\n(4) Buscar por genero.\n(4) Salir."
            )
        opc = validar_int(
            "Selecciona una opcion: ",
            "Inválido! No se permiten números en este campo",
            "Inválido! El rango de opciones es (1-4)",
            True, True, 1, 4
            )
        if opc == 1:
            agregar_vj(lista_de_juegos)
            continue
        elif opc == 2:
            if len(lista_de_juegos_enuso) == 0:
                print("AUN NO HAY JUEGOS, DEBES REGISTRAR ALMENOS 1...")
                continue
            print("== REGISTRAR VENTA ==")
            opc = validar_int(
                "(1) Buscar por codigo\n(2) Buscar por titulo\nSeleccione una opcion: ",
                "Inválido! Solo se permiten valores numéricos",
                "Inválido! El rango de opciones es (1-2)",
                True, True, 1, 2
                )
            if opc == 1:
                vj = buscar_vj("por_codigo", lista_de_juegos)
                if vj != None:
                    while True:
                        cantidad_de_ventas = ventas(vj)
                        
                        if vj["stock"] - cantidad_de_ventas < 0:
                            print(f"Ingrese una cantidad menor, el stock disponible es de {vj["stock"]}")
                            continue
                        else:
                            vj["stock"] -= cantidad_de_ventas
                            
                            
            elif opc == 2:
                vj = buscar_vj("por_titulo", lista_de_juegos)
                if vj != None:
                    ventas(vj)
            continue
        elif opc == 3:
            mostrar_todo_el_intenvario(lista_de_juegos)
        elif opc == 4:
            break
menu(lista_de_juegos)