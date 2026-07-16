prendas = {
    "S001": ["Polera Basica", "polera", "M", "negro", "algodon", True],
    "S002": ["Jeans Slim", "pantalon", "L", "azul", "denim", False],
    "S003": ["Chaqueta Urban", "chaqueta", "M", "gris", "poliester", True],
    "S004": ["Vestido Sol", "vestido", "S", "rojo", "lino", False],
    "S005": ["Poleron Cozy", "poleron", "XL", "verde", "algodon", True],
    "S006": ["Camisa Formal", "camisa", "M", "blanco", "algodon", False],
}
bodega = {
    "S001": [7900, 12],
    "S002": [19990, 0],
    "S003": [29990, 3],
    "S004": [24990, 6],
    "S005": [17990, 8],
    "S006": [14990, 2]
}
def leer_opcion():
    while True:
        try:
            opc = int(input("Seleccione una opcion: ")) 
        except ValueError:
            print("Inválido! Debe ingresar una valor numerico")
        else:
            if opc > 6 or opc < 1:
                print("Inválido!")
                continue
            return opc
def unidades_categoria(categoria) -> None:
    resultado = 0
    for codigo in prendas:
        if categoria == prendas[codigo][2]:
            resultado += bodega[codigo][1]
    print(f"En la categoría {categoria} hay {resultado} prendas")
    return None
def busqueda_precio(p_min, p_max) -> None:
    hay_prendas = False
    resultado_busqueda = []
    for codigo in bodega:
        precio = bodega[codigo][0]
        cantidad = bodega[codigo][1]
        if precio <= p_max and precio >= p_min and cantidad > 0:
            hay_prendas = True
            resultado_busqueda.append([prendas[codigo][0], codigo, precio, cantidad])
    resultado_busqueda.sort()
    if hay_prendas:
        for prenda in resultado_busqueda:
            codigo = prenda[1]
            nombre = prenda[0]
            precio = prenda[2]
            cantidad = prenda[3]
            print(f"Codigo: {codigo}\nNombre: {nombre}\nPrecio: {precio}\nCantidad: {cantidad}")
    elif not hay_prendas:
        print(f"No hay prendas dentro del rango de precio ${p_min} - ${p_max}")
    return None
def buscar_codigo(codigo) -> bool:
    if codigo in bodega:
        return True
    return False
def actualizar_codigo(codigo, nuevo_precio) -> bool:
    bodega[codigo][0] = nuevo_precio
    return True
def agregar_prenda(codigo_prenda, nombre, categoria, talla, color, material, es_unisex, precio, unidades):
    prendas[codigo_prenda] = [nombre, categoria, talla, color, material, es_unisex]
    bodega[codigo_prenda] = [precio, unidades]
    return True
def eliminar_prenda(codigo):
    del prendas[codigo]
    del bodega[codigo]
    return True
def menu() -> None:
    while True:
        print("(1) Unidades por categoria.\n(2) Búsqueda de prendas por rango de precio.\n(3) Actualizar precio de prenda.\n(4) Agreagar prenda.\n(5) Eliminar prenda.\n(6) Salir.")
        opc = leer_opcion()
        if opc == 1:
            categoria = input("Ingrese la categoria para ver la cantidad de unidades: ").strip()
            if categoria == "":
                print("Inválido! El campo está vacío")
                continue
            unidades_categoria(categoria)
        elif opc == 2:
            while True:
                try:
                    p_min = float(input("Ingresa el precio minimo: $"))
                except ValueError:
                    print("Inválido! Debes ingresar un valor numérico (demical va con punto)")
                    continue
                else:
                    if p_min <= 0:
                        print("Inválido! El valor debe ser mayor que 0")
                        continue
                    break
            while True:
                try:
                    p_max = float(input("Ingresa el precio maximo: $"))
                except ValueError:
                    print("Inválido! Debes ingresar un valor numérico (demical va con punto)")
                    continue
                else:
                    if p_min > p_max:
                        print("Inválido! El precio maximo debe ser mayor que el minimo...")
                        continue
                    break
            busqueda_precio(p_min, p_max)
        elif opc == 3:
            codigo = input("Ingresa el codigo de la prenda que quieres actualizar: ")
            existe_codigo = buscar_codigo(codigo)
            if existe_codigo:
                while True:
                    try:
                        nuevo_precio = int(input("Ingresa el nuevo precio del la prenda: $"))
                    except ValueError:
                        print("Inválido! Debes ingresar un valor numérico")
                    else:
                        if nuevo_precio <= 0:
                            print("Inválido! El precio debe ser mayor que 0")
                            continue
                        break
                precio_actualizado = actualizar_codigo(codigo, nuevo_precio)
                if precio_actualizado:
                    print("Precio actualizado con exito!")
                    continue
            elif not existe_codigo:
                print("Inválido! El codigo no existe en la bodega")
                continue
        elif opc == 4:
            codigo_prenda = input("Ingresa el codigo de la prenda nueva que deseas agregar: ")
            existe_codigo = buscar_codigo(codigo_prenda)
            if not existe_codigo:
                while True:
                    nombre = input("Ingresa el nombre").strip()
                    if nombre == "":
                        print("Inválido! El campo no puede estar vacío")
                        continue
                    break
                while True:
                    categoria = input("Ingresa el categoria").strip()
                    if categoria == "":
                        print("Inválido! El campo no puede estar vacío")
                        continue
                    break
                while True:
                    talla = input("Ingresa el talla").strip()
                    if talla == "":
                        print("Inválido! El campo no puede estar vacío")
                        continue
                    break
                while True:
                    color = input("Ingresa el color").strip()
                    if color == "":
                        print("Inválido! El campo no puede estar vacío")
                        continue
                    break
                while True:
                    material = input("Ingresa el material").strip()
                    if material == "":
                        print("Inválido! El campo no puede estar vacío")
                        continue
                    break
                while True:
                    es_unisex = input("¿Es unisex?: \nIngresa 's' si es unisex\nIngresa 'n' si NO es unisex").strip().lower()
                    if es_unisex not in ["n", "s"]:
                        print("Inválido! Selecciona una opcion ingresando 's' o 'n'.")
                        continue
                    if es_unisex == "s":
                        es_unisex = True
                    elif es_unisex == "n":
                        es_unisex = False
                    break
                while True:
                    try:
                        precio = int(input("Ingresa el precio"))
                    except ValueError:
                        print("Inválido! Debes ingresar un valor numerico")
                    else:
                        if precio <= 0:
                            print("Inválido! El precio debe ser mayor que 0")
                            continue
                        break
                while True:
                    try:
                        unidades = int(input("Ingresa el unidades"))
                    except ValueError:
                        print("Inválido! Debes ingresar un valor numérico")
                    else:
                        if unidades < 0:
                            print("Inválido! La cantidad de unidades solo puede ser mayor o igual a 0")
                            continue
                        break
                prenda_agregada = agregar_prenda(codigo_prenda, nombre, categoria, talla, color, material, es_unisex, precio, unidades)
                if prenda_agregada:
                    print("Se agregó prenda exitosamente!")
                    continue
            elif existe_codigo:
                print("No se puede agregar una prenda con ese codigo, el codigo ya existe")
                continue
        elif opc == 5:
            codigo = input("Ingresa el codigo de la prenda que quieres eliminar: ")
            existe_codigo = buscar_codigo(codigo)
            if existe_codigo:
                prenda_eliminada = eliminar_prenda(codigo)
                print("Prenda eliminada")
                continue
            elif not existe_codigo:
                print("EL codigo no existe, se cancela la accion de eliminar prenda.")
                continue
        elif opc == 6:
            return None
menu()