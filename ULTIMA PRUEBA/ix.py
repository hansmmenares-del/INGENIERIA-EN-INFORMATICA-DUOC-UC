lista_productos = []
lista_cantidad = []
dic = {}
int_valueErr_msg = "Inválido! Debes ingresar un valor numérico"
str_nonumErr = "Inválido! Este campo no puede contener números"
str_empty = "Inválido! Este campo no puede estar vacío"
## utilidad
def validar_int(msg_input:str, msg_error:str, usar_lim_inf:bool, lim_inf:int, usar_lim_sup:bool, lim_sup:int) -> int:
    """Funcion que valida input tipo [int]. Pide [input()] que mostrará el mensaje [msg_input], evalua si hay ValueError mostrando [msg_error] y evalua condicionales, en caso de que el limite inferior y/o superior sean [True]. Los limites son excluyentes, o sea ['>' y '<']"""
    while True:    
        try:
            num = int(input(msg_input))
        except ValueError:
            print(msg_error)
        else:
            if usar_lim_inf and not usar_lim_sup:
                if num < lim_inf:
                    print(f"Inválido! El valor no puede ser menor que {lim_inf}")
                    continue
            elif usar_lim_inf and usar_lim_sup:
                if num < lim_inf or num > lim_sup:
                    print(f"Inválido! El valor no puede ser menor que {lim_inf} ni mayor que {lim_sup}")
                    continue
            elif not usar_lim_inf and usar_lim_sup:
                if num > lim_sup:
                    print(f"Inválido! El valor no puede ser mayor que {lim_sup}")
                    continue
            return num
def validar_str(msg_input:str) -> str:
    ready = True
    while True:    
        texto = input(msg_input)
        for i in texto:
            if i.isnumeric():
                print(str_nonumErr)
                ready = False
                break
        if not ready:
            continue
        elif texto == "":
            print(str_empty)
            continue
        return texto
def opc_selection(msg_input:str, lim_inf:int, lim_sup:int, msg_error:str, msg_opc_is_out_of_bounds:str) -> int | None:
    try:
        opc = int(input(f"{msg_input}"))
    except ValueError:
        print(f"{msg_error}")
    else:
        if opc < lim_inf or opc > lim_sup:
            print(f"{msg_opc_is_out_of_bounds}")
        else:
            return opc
## menus_1
def revisar_en_lista(nombre_producto_nuevo) -> bool:
    if nombre_producto_nuevo in lista_productos:
        print("El producto ya existe en la lista!")
        ya_existe = True
    else:
        ya_existe = False
    return ya_existe
def menu_1_agregar_prod() -> tuple[list[str],list[int]]:
    while True:
        nombre_producto_nuevo = validar_str("Ingresa el nombre del producto que deseas agregar a la lista de productos: ")
        ya_existe = revisar_en_lista(nombre_producto_nuevo)
        if not ya_existe:
            cantidad_nombre_producto_nuevo = validar_int(f"Ingresa la cantidad del producto '{nombre_producto_nuevo}: ",int_valueErr_msg, True, 0, False, 0)
            lista_productos.append(nombre_producto_nuevo)
            lista_cantidad.append(cantidad_nombre_producto_nuevo)
            return lista_productos, lista_cantidad
        elif ya_existe:
            continue
## menus_2
def menu_2_mostrar_lista() -> None:
    print(f"El orden de los elementos es correlativo,\nLista de productos: {lista_productos}\nLista de cantidad por producto: {lista_cantidad}")
## menus_3
def menu_3_buscar_prod() -> None:
    while True:
        founded = False
        producto_a_buscar = validar_str("Ingresa el nombre del producto que quieres encontrar: ")
        for producto, cantidad in zip(lista_productos,lista_cantidad):
            if producto_a_buscar == producto:
                print(f"// Producto encontrado //\nNombre: {producto}\nCantidad: {cantidad}")
                founded = True
                break
        if not founded:
            print("Producto no encontrado :p ...")
        opc = opc_selection("¿Desdeas buscar otro producto?\n1. Si\n0. No\nIngresa el número de una opción: ",0,1,int_valueErr_msg,"Inválido! El rango de opciones es (0-1)")
        if opc == 0:
            break
        elif opc == 1:
            continue
## menus_4
def menu_4_modificar_cantidad_de_producto() -> None:
    while True:
        found = False
        mod_done = False
        producto_a_modificar = validar_str("Ingresa el nombre del producto a modificar")
        for producto, cantidad in zip(lista_productos,lista_cantidad):
            if producto_a_modificar == producto:
                found = True
                print(f"// Producto encontrado //\nNombre: {producto}\nCantidad: {cantidad}")
                opc = opc_selection("¿Qué deseas modificar del producto?\n1. Modificar nombre\n2. Modificar cantidad\n3. No modificar, salir",1,3,int_valueErr_msg,"Inválido! El rango de opciones es (1-3)")
                if opc == 1:
                    cambio_de_nombre = validar_str(f"Ingresa el nombre nuevo para el producto de nombre '{producto_a_modificar}'")
                    lista_productos[lista_productos.index(producto_a_modificar)] = cambio_de_nombre
                    print("Modificacion completa! :D")
                    mod_done = True
                    break
                elif opc == 2:
                    cambio_de_cantidad = validar_int(f"Ingresa la cantidad de stock disponible del producto {producto_a_modificar}", int_valueErr_msg, True, 0, False, 0)
                    lista_cantidad[lista_productos.index(producto_a_modificar)] = cambio_de_cantidad
                    print("Modificacion completa! :D")
                    mod_done = True
                elif opc == 3:
                    break
        if not found or mod_done or opc == 3:
            if not found:
                print("Producto no encontrado D:")
            break
    return None
## menus_5
def menu_5_eliminar_producto_de_lista_de_productos() -> None:
    ocurre_error = False
    while True:
        producto_a_borrar = validar_str("Ingresa el nombre del producto que quieres eliminar: ")
        for a_borrar in lista_productos:
            pass
        if not ocurre_error:
            for a_borrar,j in zip(lista_productos,lista_cantidad):
                if a_borrar == producto_a_borrar:
                    lista_cantidad.remove([lista_productos.index(producto_a_borrar)])
                    lista_productos.remove(producto_a_borrar)
                    print(f"Elminacion de {producto_a_borrar} se ha completado")
                    break
    return None
def menu(msg_titulo:str, *opc_en_orden:str) -> None:
    while True:
        menu_printeado = f"=== {msg_titulo} ===\n"
        for i, opc in enumerate(opc_en_orden):
            menu_printeado += f"{i+1}. {opc}\n"
        print(menu_printeado)
        opc = opc_selection("Selecciona una opción: ", 1, 6, int_valueErr_msg,"Inválido! El rango de opciones es (1-6)")
        if opc == 1:
            menu_1_agregar_prod()
        elif opc == 2:
            menu_2_mostrar_lista()
        elif opc == 3:
            menu_3_buscar_prod()
        elif opc == 4:
            menu_4_modificar_cantidad_de_producto()
        elif opc == 5:
            menu_5_eliminar_producto_de_lista_de_productos()
        elif opc == 6:
            break

#########################################################

menu(
    "Menú",
    "Agregar producto y cantidad",
    "Mostrar la lista de compras completa",
    "Buscar un producto",
    "Modificar la cantidad de un producto",
    "Eliminar un producto de la lista de productos",
    "Salir"
    )

