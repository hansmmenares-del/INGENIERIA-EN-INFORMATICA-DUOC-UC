notebooks = {'PC1': ['Asus Rog Zephyrus', '16gb ram ddr5', '1tb disco', 'NVIDIA', 'rtx 4060', 14], 'PC2': ['Lenovo Legion 5', '16gb ram ddr4', '512gb disco', 'NVIDIA', 'rtx 3060', 15.6], 'PC3': ['Hp Victus', '8gb ram ddr4', '256gb disco', 'NVIDIA', 'rtx 3050', 15.6], 'PC4': ['Acer Nitro 5', '16gb ram ddr4', '1tb disco', 'NVIDIA', 'rtx 3050ti', 14], 'PC5': ['Asus Tuf Gaming', '16gb ram ddr4', '512gb disco', 'NVIDIA', 'rtx 3050ti', 15.6], 'PC6': ['Asus Rog Strix', '32gb ram ddr5', '1tb disco', 'NVIDIA', 'rtx 4070', 15.6]}; bodega = {'PC1': [1899990, 8], 'PC2': [699990, 15], 'PC3': [599990, 12], 'PC4': [599990, 6], 'PC5': [699990, 10], 'PC6': [1499990, 3]}
def leer_opcion(bodega: dict[str, list[float|int]], notebooks: dict[str, list[str|int]]) -> int:
    while True:
        try:
            opc = int(input(f"========== MENÚ PRINCIPAL ==========\n1. Stock de Notebook por código\n2. Búsqueda de Notebooks por rango de precio\n3. Actualizar precio de un Notebook\n4. Agregar nuevo Notebook\n5. Eliminar Notebook\n6. Salir del programa\n=====================================\nSelecciona una opcion: "))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico")
        else:
            if opc < 1 or opc > 6:
                print("Inválido! El rango de opciones es 1-6")
            return opc
def detalle_notebook(codigo: str, bodega: dict[str, list[float|int]], notebooks: dict[str, list[str|int]]) -> None:
    if codigo in bodega:
        print(f"Modelo: {bodega[codigo][0]}\n Ram: {bodega[codigo][1]}\nDisco: {bodega[codigo][2]}\nMarca grafica: {bodega[codigo][3]}\nGrafica: {bodega[codigo][4]}\nDimension de pantalla: {bodega[codigo][5]}\nPrecio: {notebooks[codigo][0]}\nStock: {notebooks[codigo][1]}"); return
    print("Error! El codigo ingresado no existe")
def busqueda_precio(precio_min: float, precio_max: float, bodega: dict[str, list[float|int]], notebooks: dict[str, list[str|int]]) -> None:
    contador_magico = 0
    for codigo in bodega:
        precio = bodega[codigo][0]; stock = bodega[codigo][1]
        if ((precio <= precio_max and precio >= precio_min) and stock > 0):
            print(f"Codigo: {codigo}\nModelo: {notebooks[codigo[0]]}\nPrecio: {precio}\nStock: {stock}"); contador_magico += 1
    if contador_magico == 0:
        print(f"Resultados de busqueda: No hay resultados."); return None
    print(f"Resultados de busqueda: {contador_magico} notebooks encontrados"); return None
def buscar_codigo(codigo: str, bodega: dict[str, list[float|int]], notebooks: dict[str, list[str|int]]) -> bool:
    if codigo in bodega:
        return True
    return False
def actualizar_precio(codigo: str, bodega: dict[str, list[float|int]], notebooks: dict[str, list[str|int]]) -> bool:
    while True:
        try:
            precio_nuevo = float(input("Ingrese el precio nuevo: "))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico (puede ser decimal con punto)")
        else:
            if precio_nuevo <= 0:
                print("Inválido! El precio debe ser mayor que 0"); continue
            precio_nuevo = bodega[codigo][0]; return True
def agregar_notebook(codigo: str, modelo: str, ram: str, disco: str, marca_grafica: str, grafica: str, dimension_pantalla: int, precio: float, stock: int, bodega: dict[str, list[float|int]], notebooks: dict[str, list[str|int]]) -> bool:
    notebooks[codigo] = [modelo, ram, disco, marca_grafica, grafica, dimension_pantalla]; bodega[codigo] = [precio, stock]; return True
def validar_str(msg_input: str, bodega: dict[str, list[float|int]], notebooks: dict[str, list[str|int]]) -> str:
    while True:
        texto = input(f"Ingrese el {msg_input} del notebook: ").strip().title()
        if texto == "":
            print("Inválido! Este campo no puede estar vacio"); continue
        return texto
def validar_precio(bodega: dict[str, list[float|int]], notebooks: dict[str, list[str|int]]) -> float:
    while True:
        try:
            precio = float(input("Ingrese el precio del notebook: $"))  
        except ValueError:
            print("Inválido! Debe ingresar un valor numérico (puede ser decimal con punto)")
        else:
            if precio <= 0:
                print("Inválido! El precio debe ser mayor que 0 (puede ser decimal con punto)"); continue
            return precio     
def validar_stock(bodega: dict[str, list[float|int]], notebooks: dict[str, list[str|int]]) -> int:
    while True:
        try:
            stock = int(input("Ingresa el stock del notebook: "))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico")
        else:
            if stock < -1:
                print("Inválido! El stock solo puede tener valor 0 o mayor"); continue
            return stock
def validar_dimension_pantalla(bodega: dict[str, list[float|int]], notebooks: dict[str, list[str|int]]) -> int:
    while True:
        try:
            dimension_pantalla = int(input("Ingresa las dimensiones en pulgadas de la pantalla del notebook: "))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico")
        else:
            if dimension_pantalla < -1:
                print("Inválido! Las dimensiones de la pantalla deben ser mayores o igual que 0"); continue
            return dimension_pantalla
def eliminar_notebook(codigo: str, bodega: dict[str, list[float|int]], notebooks: dict[str, list[str|int]]) -> bool:
    del bodega[codigo]; del notebooks[codigo]; return True
def menu(bodega, notebooks) -> None:
    while True:
        opc = leer_opcion(bodega, notebooks)
        if opc == 1:
            codigo = input("Ingresa el codigo del notebook que quieres consultar: ").strip().upper(); detalle_notebook(codigo, bodega, notebooks)
        elif opc == 2:
            print("Deberás ingresar un rango de precios para ver los notebooks...")
            while True:
                try:
                    precio_min = float(input("Ingresa el valor minimo de precio para la busqueda"))
                except ValueError:
                    print("Inválido! Debes ingresar un valor numérico (puede ser decimal con punto)"); continue
                else:
                    if precio_min < 0:
                        print("Inválido! No se permiten valores negativos"); continue
                    break
            while True:
                try:
                    precio_max = float(input("Ingresa el valor maximo de precio para la busqueda"))
                except ValueError:
                    print("Inválido! Debes ingresar un valor numérico (puede ser decimal con punto)"); continue
                else:
                    if precio_min > precio_max:
                        print(f"Error! El 'valor maximo' ingresado debe ser mayor que el 'valor minimo'. Intente con un valor mayor que {precio_min}"); continue
                    break
            busqueda_precio(precio_min, precio_max, bodega, notebooks)
        elif opc == 3:
            contador_magico = 0
            while True:
                if contador_magico == 0:
                    opc = input("¿Desea actualizar un precio? (s/n)").strip().lower()
                elif contador_magico > 0:
                    opc = input("¿Desea actualizar otro precio? (s/n)").strip().lower()
                if opc == "n":
                    break
                elif opc == "s":
                    contador_magico += 1; codigo = input("Ingresa el codigo del notebook que quieres consultar: ").strip().upper(); notebook_existe = buscar_codigo(codigo, bodega, notebooks)
                    if notebook_existe:
                        se_actualizo_notebook = actualizar_precio(codigo, bodega, notebooks)
                        if not se_actualizo_notebook:
                            print("El código no existe")
                        elif se_actualizo_notebook:
                            print("Precio actualizado"); continue
                else:
                    print("Por favor, debe escribir 's' o 'n'.)")
        elif opc == 4:
            while True:
                codigo = input("Ingresa el codigo nuevo que deseas ingresar: ").strip().upper()
                if codigo == "":
                    print("Inválido! El codigo a ingresar no puede estár vacío"); continue
                break
            existe_notebook = buscar_codigo(codigo, bodega, notebooks)
            if not existe_notebook:
                modelo = validar_str("modelo", bodega, notebooks); ram = validar_str("ram", bodega, notebooks); disco = validar_str("disco", bodega, notebooks); marca_grafica = validar_str("marca grafica", bodega, notebooks); grafica = validar_str("grafica", bodega, notebooks); dimension_pantalla = validar_dimension_pantalla(bodega, notebooks); precio = validar_precio(bodega, notebooks); stock = validar_stock(bodega, notebooks); se_agrego_notebook = agregar_notebook(codigo, modelo, ram, disco, marca_grafica, grafica, dimension_pantalla, precio, stock, notebooks, bodega)
            if se_agrego_notebook:
                print("Notebook agregado"); continue
            print("Codigo de notebook ya existe")
        elif opc == 5:
            codigo = input("Ingresa el codigo del notebook que deseas eliminar: "); existe_notebook = buscar_codigo(codigo, bodega, notebooks)
            if existe_notebook:
                notebook_eliminado = eliminar_notebook(codigo, bodega, notebooks)
                if notebook_eliminado:
                    print("Eliminacion comlpeta"); continue
            print("Inválido! El codigo no existe")
        elif opc == 6:
            print("Muchas gracias por usar el programa"); return None
menu(bodega, notebooks)