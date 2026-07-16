codigo = 0
titulo = ""
genero = ""
precio = 0
stock = 0
lista_de_juegos = []
def validar_int(msg_input:str, hay_lim_inf:bool, hay_lim_sup:bool, lim_inf:int|float, lim_sup:int|float) -> int:
    while True:
        try:
            num = int(input(f"{msg_input}"))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico")
        else:
            if hay_lim_inf:
                if num < lim_inf:
                    print(f"Inválido! El valor debe ser mayor que {lim_inf}")
                    continue
            elif hay_lim_inf and hay_lim_sup:
                if num < lim_inf or num > lim_sup:
                    print(f"Inválido El valor debe estar en el rango ({lim_inf} - {lim_sup})")
                    continue
            elif hay_lim_sup:
                if num > lim_sup:
                    print(f"Inválido! El valor debe ser mayor que {lim_inf}")
                    continue
            return num                
def validar_str(msg_input:str) -> str:
    while True:
        errores = False
        texto = input(f"{msg_input}")
        for i in texto:
            if i.isnumeric() == True:
                print("Inválido! El campo no puede contener números")
                errores = True
                break
        if texto == "":
            print("Inválido! El campo no puede estar vacío")
            errores = True
        if errores:
            continue
        else:
            return texto
def agregar_vj() -> None:
    while True:
        errores = False
        print("VAMOS A AGREGAR UN VJ NUEVO...")
        codigo = validar_int("Ingresa el código id del vj: ", True, False, 1000, 0)
        for vj in lista_de_juegos:
            if codigo == vj["codigo"]:
                print("Inválido! El codigo ya está asociado a un numero")
                errores = True
                break
        if errores:
            continue
        else:
            break
    while True:
        errores = False
        titulo = validar_str("Ingresa el título del vj: ")
        for vj in lista_de_juegos:
            if titulo == vj["titulo"]:
                print("Inválido! El titluo ya está asociado a un vj")
                errores = True
                break
        if errores:
            continue
        else:
            break
    genero = validar_str("Ingresa el genero del vj: ")
    precio = validar_int("Ingresa el precio del vj: $", True, False, 0.0001, 0).__round__(2)
    stock = validar_int("Ingresa el stock del vj: ", True, False, 1, 0)
    dic = {
    "codigo" : codigo,
    "titulo" : titulo,
    "genero" : genero,
    "precio" : precio,
    "stock" : stock
    }
    lista_de_juegos.append(dic)
    return None
def registrar_venta() -> None:
    print("VAMOS A LAS VENTAS")
    while True:
        errores = False
        codigo = validar_int("Ingresa el código id del vj a vender: ", True, False, 1000, 0)
        for vj in lista_de_juegos:
            if codigo == vj["codigo"]:
                print("¡¡¡VJ encontrado!!!")
                break
            elif codigo != vj["codigo"]:
                errores = True
        if errores:
            continue
        if vj["stock"] <= 0:
            print("No es posible hacer la venta, no queda stock del juego buscado...")
            break
        else:
            while True:
                print(f"Juego '{vj["titulo"]}' tiene {vj["stock"]} unidades disponibles")
                cantidad_ventas = validar_int("Ingresa la cantidad de ejemplares a vender", True, True,0, vj["stock"])
                if (vj["stock"] - cantidad_ventas) < 0:
                    print("Inválido! Intenta con una cantidad menor de ejemplares...")
                    continue
                else:
                    print(f"Total de la venta ${(vj["precio"]*cantidad_ventas)}")
                    vj["stock"] -= cantidad_ventas
                    break
            break
def mostrar_inventario() -> None:
    for vj in lista_de_juegos:
        print(f"--\nCodigo: {vj["codigo"]}\nTítulo: {vj["titulo"]}\nGénero: {vj["genero"]}\nPrecio: {vj["precio"]}\nStock: {vj["stock"]}")
    return None
def buscar_por_genero() -> None:
    contador = 0
    genero = validar_str("Ingresa el genero para ver los titulos: ")
    for vj in lista_de_juegos:
        if genero == vj["genero"]:
            print(f"TITULO: {vj["titulo"]}")
            contador += 1
    print(f"Juegos encontrados: {contador}")
    if contador == 0:
        print("Ningun juego encontrado D:")
def buscar_por_codigo() -> None:
     while True:
        errores = False
        codigo = validar_int("Ingresa el codigo del vj: ",True, False, 1000, 0)
        for vj in lista_de_juegos:
            if codigo == vj["codigo"]:
                print("¡¡¡VJ ENCONTRADO!!!")
                errores = False
                return None
            else:
                errores = True
        if errores:
            print("No se ha encontrado el juego, intenta de nuevo...")
            continue
def cambio_de_codigo() -> None:
    while True:
        errores = False
        codigo = validar_int("Ingresa el codigo nuevo: ", True, False, 1000, 0)
        for vj in lista_de_juegos:
            if codigo == vj["codigo"]:
                print("Inválido! El código ingresado ya está en uso.")
                errores = True
                break
        if errores:
            continue
        vj["codigo"] = codigo
        print("¡¡¡ Cambio logrado con éxito !!!")
        return None
def modificar_vj() -> None:
    while True:
        print("VAMOS A MODIFICAR UN JUEGO")
        opc = validar_int("(0) Salir.\n(1) Buscar juego para modificar\nSelecciona una opción: ",True, True, 0, 1)
        if opc == 0:
            break
        elif opc == 1:
            opc = validar_int("(1) Buscar por código\n(2) Buscar por título\nSelecciona una opción: ",True, True, 1, 2)
            if opc == 1:
                buscar_por_codigo()
                opc = validar_int(f"¿Qué desea cambiar de {vj['titulo']}?\n(0) Nada, salir.\n(1) Código.\n(2) Título.\n(3) Género.\n(4) Precio.\n(5) Stock.\nSelecciona una opción: ", True, True, 0, 5)
                if opc == 0:
                    break
                elif opc == 1:
                    cambio_de_codigo()
                elif opc == 2:
                    while True:
                        errores = False
                        nuevo_titulo = validar_str("Ingresa el nuevo título: ")
                        for juego in lista_de_juegos:
                            if nuevo_titulo == juego["titulo"]:
                                print("Inválido! El título ya existe.")
                                errores = True
                                break
                        if errores:
                            continue
                        vj["titulo"] = nuevo_titulo
                        print("¡¡¡ Cambio logrado con éxito !!!")
                        break
                elif opc == 3:
                    vj["genero"] = validar_str("Ingresa el nuevo género: ")
                    print("¡¡¡ Cambio logrado con éxito !!!")
                elif opc == 4:
                    vj["precio"] = validar_int("Ingresa el nuevo precio: $", True, False, 1, 0)
                    print("¡¡¡ Cambio logrado con éxito !!!")
                elif opc == 5:
                    vj["stock"] = validar_int("Ingresa el nuevo stock: ", True, False, 0, 0)
                    print("¡¡¡ Cambio logrado con éxito !!!")
                break
        elif opc == 2:
            while True:
                errores = False
                titulo = validar_str("Ingresa el título del vj: ")
                for vj in lista_de_juegos:
                    if titulo == vj["titulo"]:
                        print("¡¡¡VJ ENCONTRADO!!!")
                        errores = False
                        break
                    else:
                        errores = True
                if errores:
                    print("No se ha encontrado el juego, intenta de nuevo...")
                    continue
                opc = validar_int(f"¿Qué desea cambiar de {vj['titulo']}?\n(0) Nada, salir.\n(1) Código.\n(2) Título.\n(3) Género.\n(4) Precio.\n(5) Stock.\nSelecciona una opción: ", True, True, 0, 5)
                if opc == 0:
                    break
                elif opc == 1:
                    while True:
                        errores = False
                        nuevo_codigo = validar_int("Ingresa el codigo nuevo: ", True, False, 1000, 0)
                        for juego in lista_de_juegos:
                            if nuevo_codigo == juego["codigo"]:
                                print("Inválido! El código ingresado ya está en uso.")
                                errores = True
                                break
                        if errores:
                            continue
                        vj["codigo"] = nuevo_codigo
                        print("¡¡¡ Cambio logrado con éxito !!!")
                        break
                elif opc == 2:
                    while True:
                        errores = False
                        nuevo_titulo = validar_str("Ingresa el nuevo título: ")
                        for juego in lista_de_juegos:
                            if nuevo_titulo == juego["titulo"]:
                                print("Inválido! El título ya existe.")
                                errores = True
                                break
                        if errores:
                            continue
                        vj["titulo"] = nuevo_titulo
                        print("¡¡¡ Cambio logrado con éxito !!!")
                        break
                elif opc == 3:
                    vj["genero"] = validar_str("Ingresa el nuevo género: ")
                    print("¡¡¡ Cambio logrado con éxito !!!")
                elif opc == 4:
                    vj["precio"] = validar_int("Ingresa el nuevo precio: $", True, False, 1, 0)
                    print("¡¡¡ Cambio logrado con éxito !!!")
                elif opc == 5:
                    vj["stock"] = validar_int("Ingresa el nuevo stock: ", True, False, 0, 0)
                    print("¡¡¡ Cambio logrado con éxito !!!")
                break
def borrar_vj():
    print("--- VAMOS A BORRAR UN JUEGO ---")
    while True:
        opc = validar_int("Buscar juego a eliminar por:\n(1) Código.\n(2) Título.\n(3)Genero\n(4) Precio.\n(5) Stock.\nSelecciona una opción: ", True, True, 0, 0)
        if opc == 0:
            break
        elif opc == 1:
            while True:
                errores = False
                codigo = validar_int("Ingresa el código a buscar: ", True, False, 1000, 0)
                for vj in lista_de_juegos:
                    if codigo == vj["código"]:
                        print("¡¡¡ VJ ENCONTRADO !!!")
                        print(f"Codigo: {vj}")
                        break
                    else:
                        errores = True
                if errores:
                    continue
                else:
                    
        elif opc == 2:
            titulo = validar_str("Ingresa el código a buscar: ")
        elif opc == 3:
            genero = validar_str("Ingresa el código a buscar: ")
        elif opc == 4:
            precio = validar_str("Ingresa el código a buscar: ")
        elif opc == 5:
            stock = validar_str("Ingresa el código a buscar: ")
def menu() -> None:
    while True:
        opc = validar_int("== MENU ==\n(1) Agregar vj.\n(2) Registrar venta.\n(3) Mostrar inventario\n(4) Buscar por genero.\n(5) Modificar vj.\nSelecciona una opción: ", True, True, 0, 4)
        if opc == 1:
            agregar_vj()
        elif opc == 2:
            registrar_venta()
        elif opc == 3:
            mostrar_inventario()
        elif opc == 4:
            buscar_por_genero()
        elif opc == 5:
            modificar_vj()
        elif opc == 6:
            borrar_vj()
        elif opc == 0:
            break
menu()