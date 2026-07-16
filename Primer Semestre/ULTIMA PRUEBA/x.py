inventario,errores,contador,codigo,titulo,genero,precio,stock,dic = [],True,0,999,"","",0,0,{}
def codigo_contador_eterno_del_diablo(codigo) -> int:
    """Funcion la cual su misera existencia es asignar un codigo identificador a los vj... Lo unico que hace es sumar 1 en 1 eternamente. Devuelve el valor del codigo para asignarlo en el diccionario"""
    codigo += 1
    return codigo
def checkeo_texto(msg:str) -> str:
    """Funcion que anuncia error si el input de usuario (string) está vacío o contiene números. En caso de error se vuelve a pedir el input, de lo contrario, se acaba la funcion y hace return texto"""
    while True:    
        texto = input(f"Ingresa el {msg} del videojuego: ")
        for i in texto:
            if i.isnumeric():
                print("Inválido! Este campo no puede contener números")
                break
        if texto == "":
            print("Inválido! Este campo no puede estar vacío")
        else:
            break
    return texto
def checkeo_float(msg:str) -> float:
    while True:
        try:
            num = float(input(f"Ingresa el {msg} del videojuego: "))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico. (Decimales van con punto, NO coma)")
        else:
            if num <= 0:
                print("Inválido! El valor ingresado debe ser mayor a 1")
            else:
                num = num.__round__(2)
                break
    return num
def checkeo_int(msg:str) -> int:
    while True:
        try:
            num = int(input(f"Ingresa el {msg} del videojuego: "))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico")
        else:
            if num <= 0:
                print("Inválido! El valor ingresado debe ser mayor a 1")
            else:
                break
    return num
def agregar_vj() -> list:
    """Funcion para agregar videojuego. Crea diccionario con keys, los valores los asigna el usuario. El código identificador del videojuego es asignado automaticamente"""
    global codigo
    codigo = codigo_contador_eterno_del_diablo(codigo)
    titulo = checkeo_texto("titulo")
    genero = checkeo_texto("genero")
    precio = checkeo_float("precio")
    stock = checkeo_int("stock")
    dic = {
        "codigo":codigo,
        "titulo":titulo,
        "genero":genero,
        "precio":precio,
        "stock":stock
    }
    inventario.append(dic)
    return inventario
def venta_de_vj(contador) -> None:
    while True:
        print(f"Hay {inventario[contador]["stock"]} ejemplares de {inventario[contador]["titulo"]} (Código buscado: {inventario[contador]["codigo"]})")
        try:
            venta = int(input("Ingresa cuántos ejemplares desea comprar: "))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico.")
        else:
            if venta > inventario[contador]["stock"]:
                print("No puedes hacer la compra/venta. No hay suficientes ejemplares. Intenta con una cantidad menor o igual de ejemplares disponibles en el inventario.")
            elif venta <= 0:
                print("Inválido! Ingresa una cantidad mayor que '0'")
            else:
                inventario[contador]["stock"] -= venta
                print(f"VENTA REALZIADA CON EXITO! Quedan {inventario[contador]["stock"]} unidades de {inventario[contador]["titulo"]}")
                break
def registrar_venta() -> None:
    #validar codigo, cantidad a vender (+ > 0), no sobrepasar stock y restar del stock
    while True:
        contador = 0
        try:
            num = int(input("Ingresa el codigo del juego: "))
        except ValueError:
            print("Inválido! Debes ingresar un código de juego válido")
        else:
            if num < 1000:
                print("Inválido! Los codigos comienzan desde el valor 1000 en adelante")
                continue
            for vj in inventario:
                if num == vj["codigo"]:
                    encontrado = True
                    print("GAME FOUND! :D")
                    break
                else:
                    encontrado = False
                contador += 1
            if encontrado == True:
                if inventario[contador]["stock"] == 0:
                    print("No hay stock del videojuego. Se cancelará la compra/venta.")
                else:
                    ### VENTA
                    venta_de_vj(contador)
                    break
            else:
                print(f"No se ha encontrado el juego con el codigo: {num}")
                break
def mostrar_inventario() -> None:
    for vj in inventario:
        print(f"\n--===--\nCódigo: {vj["codigo"]}\nTítulo: {vj["titulo"]}\nGénero: {vj["genero"]}\nPrecio: ${vj["precio"]}\nStock: {vj["stock"]}\nVALOR TOTAL = ${vj["precio"]*(vj["stock"])}\n--===--\n")
def buscar_codigo() -> None:
    while True:
        contador = 0
        try:
            codigo_a_buscar = int(input("Ingresa el código que deseas buscar: "))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico")
        else:
            if codigo_a_buscar < 1000:
                print("Inválido! Los códigos de videojuegos empiezan desde el 1000 en adelante...")
                continue
            for vj in inventario:
                if codigo_a_buscar == vj["codigo"]:
                    print(f"\n===\nGAME FOUND\n{inventario[contador]}\n===\n")
                    break
                contador += 1
            break
def buscar_titulo() -> None:
    errores = False
    while True:
        contador = 0
        titulo_a_buscar = input("Ingresa el código que deseas buscar: ")
        for i in titulo_a_buscar:
            if i.isnumeric():
                print("Inválido! Este campo no puede contener números")
                errores = True
                break
        if titulo_a_buscar == "":
            print("Inválido! Este campo no puede estar vacío")
            continue
        if errores == False:
            for vj in inventario:
                if titulo_a_buscar == vj[contador]["titulo"]:
                    print(f"\n===\nGAME FOUND\n{inventario[contador]}\n===\n")
                    break
                contador += 1
            break
def buscar_genero() -> None:
    errores = False
    lista_generos = []
    while True:
        contador = 0
        print("-- Reminder --\nGeneros existentes en inventario:")
        for gen in inventario:
            if gen["genero"] not in lista_generos:
                lista_generos.append(gen["genero"])
        print(lista_generos)
        genero_a_buscar = input("Ingresa el genero que deseas buscar: ")
        for i in genero_a_buscar:
            if i.isnumeric():
                print("Inválido! Este campo no puede contener números")
                errores = True
                break
        if genero_a_buscar == "":
            print("Inválido! Este campo no puede estar vacío")
            errores = True
            continue
        else:
            errores = False
            if errores == False:
                print("\n===\nGAMES FOUNDED\n")
                for vj in inventario:
                    if genero_a_buscar == vj[contador]["genero"]:
                        print(f"{inventario[contador]}\n===\n")
                        break
                    contador += 1
                break
def buscar() -> None:
    while True:
        print("=== BUSQUEDA ===\n1. Por Código\n2. Por Título\n3. Por Género\n4. Por Precio\n5. Por Stock disponible\n0. Salir\n")
        try:
            opc = int(input("Ingresa una opción: "))
        except ValueError:
            print("Inválido! Debes ingresar el número de una opción valida (0-5)")
        else:
            if opc == 1:
                buscar_codigo()               
            elif opc == 2:
                buscar_titulo()  
            elif opc == 3:
                buscar_genero()    
            elif opc == 4:
                pass    
            elif opc == 5:
                pass    
            elif opc == 0:
                pass
def opc_menu() -> None:
    while True:
        print("=== MENU ===\n1. Agregar.\n2. Registrar venta.\n3. Mostrar inventario.\n4. Buscar Videojuego.\n5. Salir\n============\n")
        try:
            opc = int(input("Ingresa una opción: "))
        except ValueError:
            print("Inválido! Debes ingresar una opción valida (1-5)")
        else:
            if opc == 1:
                agregar_vj()
            elif opc == 2:
                registrar_venta()
            elif opc == 3:
                mostrar_inventario()
            elif opc == 4:
                buscar()
            elif opc == 5:
                break
opc_menu()