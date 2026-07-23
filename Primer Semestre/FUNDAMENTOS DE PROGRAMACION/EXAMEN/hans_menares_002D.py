peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español',False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles',False]
    }
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3]
    }
def validar_opc() -> int:
    while True:
        try:
            opc = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Inválido! Debe ingresar un valor numérico")
        else:
            if opc > 6 or opc < 1:
                print("Inválido! El rango de opciones es (1-6)")
                continue
            return opc
def validar_int(msg_input: str, hay_lim_inf: bool, hay_lim_sup: bool, lim_inf: int, lim_sup: int) -> int:
    while True:
        try:
            num = int(input(msg_input))
        except ValueError:
            print("Inválido! Debe ingresar valores enteros")
        else:
            if hay_lim_inf and hay_lim_sup:
                if num > lim_sup or num < lim_inf:
                    print(f"Inválido! Los limites permitidos son {lim_inf} hasta {lim_sup}")
                    continue
            elif hay_lim_inf:
                if num < lim_inf:
                    print(f"Inválido! Solo se permiten valores mayores que {lim_inf}")
                    continue
            elif hay_lim_sup:
                if num > lim_sup:
                    print(f"Inválido! Solo se permiten valores menores que {lim_sup}")
                    continue
            return num
def validar_str(msg_input: str) -> str:
    while True:
        texto = input(msg_input).strip().lower()
        if texto == "":
            print("Inválido! El campo no puede quedar vacío")
            continue
        return texto
def cupos_genero(genero: str) -> None:
    cantidad_total_de_cupos = 0
    for codigo in peliculas:
        if genero == peliculas[codigo][1]:
            cupos_de_pelicula = cartelera[codigo][1]
            cantidad_total_de_cupos += cupos_de_pelicula
    print(f"Total de cupos en el genero buscado: {cantidad_total_de_cupos}")
    return None
def busqueda_precio(p_min, p_max):
    hay_peliculas = False
    resultado_busqueda = []
    for codigo in cartelera:
        titulo = peliculas[codigo][0]
        precio = cartelera[codigo][0]
        cupos = cartelera[codigo][1]
        if precio <= p_max and precio >= p_min and cupos > 0:
            hay_peliculas = True
            resultado_busqueda.append([titulo, codigo, precio, cupos])
    resultado_busqueda.sort()
    if hay_peliculas:
        print(f"{titulo}--{codigo}\nPrecio: {precio}\nCupos: {cupos}")
        return None
    elif not hay_peliculas:
        print("No hay peliculas en ese rango de precios")
        return None
def actualizar_precio(codigo, nuevo_precio) -> bool:
    contador_de_actualizaciones_realizadas = 0
    exitoso = False
    while True:
        if contador_de_actualizaciones_realizadas > 0:
            continuar_o_no = input("¿Desea actualizar otro precio (s/n)?").strip().lower()
            if continuar_o_no == "n":
                return exitoso
            elif continuar_o_no == "s":
                pass
        codigo = input("Ingresa el codigo de la pelicula que quieres buscar para actualizar su precio: ").upper().strip()
        if codigo in cartelera:
            existe_pelicula = True
        elif codigo not in cartelera:
            existe_pelicula = False
        if not existe_pelicula:
            print("Codigo no existe!")
            contador_de_actualizaciones_realizadas += 1
            continue
        elif existe_pelicula:
            precio_nuevo = validar_int("Ingrese el precio nuevo para la pelicula: $", True, False, 0, 0)
            contador_de_actualizaciones_realizadas += 1
            cartelera[codigo][0] = precio_nuevo
            exitoso = True
            print("Precio actualizado!")
            continue
def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos) -> bool:
    if 1 == 1:    
        lista_a_agregar_peliculas = []
        lista_a_agregar_peliculas.append(titulo, genero, duracion, clasificacion, idioma, es_3d)
        lista_a_agregar_cartelera = []
        lista_a_agregar_cartelera.append(precio, cupos)
        peliculas[codigo] = lista_a_agregar_peliculas
        cartelera[codigo] = lista_a_agregar_cartelera
        return True
    else:
        return False
def eliminar_pelicula(codigo) -> False:
    while True:
        if codigo == "":
            print("Inválido! El campo no puede estar vacío")
            continue
        break
    if codigo not in cartelera:
        print("El codigo no existe! se cancela la accion de borrar pelicula")
        return False
    else:
        del peliculas[codigo]
        del cartelera[codigo]
        print("Pelicula eliminada")
        return True
def menu() -> None:
    while True:
        print("========== MENÚ PRINCIPAL ==========\n1. Cupos por género\n2. Búsqueda de películas por rango de precio\n3. Actualizar precio de película\n4. Agregar película\n5. Eliminar película\n6. Salir\n=====================================")
        opc = validar_opc()
        if opc == 1:
            genero = input("Ingresa el genero que quieres buscar: ").lower().strip()
            cupos_genero(genero)
        elif opc == 2:
            p_min = validar_int("Ingresa el limite inferior de precio: $", True, False, 0, 0)
            p_max = validar_int("Ingresa el limite superior de precio: $", True, False, p_min, 0)
            busqueda_precio(p_min, p_max)
        elif opc == 3:
            codigo = input("Ingresa el codigo de la pelicula a actualizar: ")
            nuevo_precio = validar_int("Ingrese el precio nuevo para la pelicula: ", True, False, 0, 0)
            actualizar_precio(codigo, nuevo_precio)
            # creo que en el enunciado deberia especificar solo los requerimientos y no cómo implementarlos en codigo...
        elif opc == 4:
            while True:
                codigo = input("Ingresa el codigo de la pelicula que quieres agregar: ").strip().upper()
                if codigo == "":
                    print("Inválido! Este campo no puede estár vacio")
                    continue
                if codigo in cartelera:
                    print("Inválido! El codigo ya existe, intenta ingresando otro")
                    continue
                break
            titulo = validar_str("Ingresa el titulo de la pelicula: ").lower()
            genero = validar_str("Ingresa el genero de la pelicula: ").lower()
            duracion = validar_int("Ingresa la duracion de la pelicula (min): ", True, False, 0, 0)
            while True:    
                clasificacion = input("ingresa la clasificacion de la pelicula: (A, B o C)").strip().upper()
                if clasificacion not in ["A", "B", "C"]:
                    print("Inválido! Las clasificaciones que se aceptan son solo 'A', 'B' o 'C'...")
                    continue
                break
            idioma = validar_str("Ingresa el idioma de la pelicula: ")
            while True:    
                es_3d = input("¿La pelicula está en 3D?\nIngresa 's' o 'n': ").strip().lower()
                if es_3d == "n":
                    es_3d = False
                elif es_3d == "s":
                    es_3d = True
                else:
                    print("Inválido! Debes ingresar 's' o 'n'...")
                    continue
                break
            precio = validar_int("Ingrese el precio de la pelicula: ", True, False, 0, 0)
            cupos = validar_int("Ingrese la cantidad de cupos disponibles: ", True, False, 0, 0)
            se_agrego_pelicula = agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos)
            if se_agrego_pelicula:
                print("Pelicula agregada")
                continue
            elif not se_agrego_pelicula:
                print("No se pudo agregar la pelicula")
                continue
        elif opc == 5:
            codigo = input("Ingrese el codigo de la pelicula que quieres eliminar: ").strip().upper()
            eliminacion_de_pelicula = eliminar_pelicula(codigo)
            if not eliminacion_de_pelicula:
                print("El codigo no existe")
                continue
        elif opc == 6:
            print("Programa finalizado.")
            return None
menu()