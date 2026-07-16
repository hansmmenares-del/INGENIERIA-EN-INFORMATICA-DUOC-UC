dict[str, list[str|int|float]]
dict[str, list[float|int]]
notebooks = {
    'PC1': [
        'Asus Rog Zephyrus',
        '16gb ram ddr5',
        '1tb disco',
        'NVIDIA', 
        'rtx 4060', 
        14],
    'PC2': [
        'Lenovo Legion 5',
        '16gb ram ddr4', 
        '512gb disco',
        'NVIDIA',
        'rtx 3060',
        15.6],
    'PC3': [
        'Hp Victus',
        '8gb ram ddr4', 
        '256gb disco',
        'NVIDIA', 
        'rtx 3050', 
        15.6],
    'PC4': [
        'Acer Nitro 5', 
        '16gb ram ddr4',
        '1tb disco', 
        'NVIDIA',
        'rtx 3050ti',
        14],
    'PC5': [
        'Asus Tuf Gaming',
        '16gb ram ddr4',
        '512gb disco',
        'NVIDIA',
        'rtx 3050ti',
        15.6],
    'PC6': [
        'Asus Rog Strix',
        '32gb ram ddr5',
        '1tb disco',
        'NVIDIA',
        'rtx 4070',
        15.6]
    }
bodega = {
    'PC1': [1899990, 8],
    'PC2': [699990, 15],
    'PC3': [599990, 12],
    'PC4': [599990, 6],
    'PC5': [699990, 10],
    'PC6': [1499990, 3]
    }
def leer_opcion() -> int:
    """Functions that validate the option selection. Returns opc value (integer)"""
    while True:
        try:
            opc = int(input("Selecciona una opcion: "))
        except ValueError:
            print("Inválido! Debes ingresar un valor numérico")
        else:
            if opc < 1 or opc > 6:
                print("Inválido! El rango de opciones es (1-6)")
                continue
            return opc      
def leer_codigo() -> str|None:
    codigo = input("Ingresa el código: ").strip().upper()
    if codigo == "":
        print("Inválido! El codigo ingresado está vacío")
        return None
    return codigo
def buscar_codigo(codigo: str|None, notebooks: dict[str, list[str|int|float]], bodega: dict[str, list[float|int]]) -> bool:
    codigo = leer_codigo()
    if codigo != None:
        if codigo in bodega:
            print("Encontrado!")
            return True
    return False
            

def detalle_notebook(codigo: str|None, notebooks: dict, bodega: dict) -> None:
    codigo = leer_codigo()
    buscar_codigo(codigo, notebooks, bodega)
    
def busqueda_precio(precio_min: float, precio_max: float, bodega: dict, notebooks: dict) -> None:
    pass

def actualizar_precio(codigo: str|None, nuevo_precio: int, bodega: dict, notebooks: dict) -> bool:
    codigo = leer_codigo()
    buscar_codigo(codigo, notebooks, bodega)
    return True
return False
    
def agregar_notebook(codigo: str, modelo: str, ram: str, disco: str, marca_grafica: str, grafica: str, dimension_pantalla: int, precio: int, stock: int, notebooks: dict, bodega: dict) -> bool:
    buscar_codigo()
    
def eliminar_notebook(codigo: str, notebooks: dict, bodega: dict) -> bool:
    buscar_codigo()

def validar_codigo(codigo: str) -> bool:
    pass
def validar_modelo(modelo: str) -> bool:
    pass
def validar_ram(ram: str) -> bool:
    pass
def validar_disco(disco: str) -> bool:
    pass
def validar_marca_grafica(marca_grafica: str) -> bool:
    pass
def validar_grafica(grafica: str) -> bool:
    pass
def validar_dimension_pantalla(dimension_pantalla: int) -> bool:
    pass
def validar_precio(precio: int) -> bool:
    pass
def validar_stock(stock: int) -> bool:
    pass

def menu() -> None:
    """Shows main menu and calls functions."""
    while True:    
        print(f"== MENU ==\n1. Stock de Notebook por código\n2. Búsqueda de notebooks por rango de precio\n3. Actualizar precio de un Notebook\n4. Agregar nuevo Notebook\n5. Eliminar Notebook\n6. Salir del programa")
        opc = leer_opcion()
        if opc == 1:
            pass
        elif opc == 2:
            busqueda_precio(precio_min, precio_max, bodega, notebooks)
        elif opc == 3:
            pass
        elif opc == 4:
            pass
        elif opc == 5:
            codigo = leer_codigo()
            boleano = eliminar_notebook(codigo, notebooks, bodega)
            if boleano:
                print("Notebook eliminado exitosamente!")
                continue
            print("No se pudo completar la eliminacion...")
        elif opc == 6:
            print("Muchas gracias por usar el program")
            return None