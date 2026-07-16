# codigo unico de notebook como clave, para ambos diccionarios
# Programa inicia con dos diccionarios
# los dict creados deben ser siempre argumentos en funciones
# no globals/global
#Notebooks = {
#     'PC1': ['Asus Rog Zephyrus', '16gb ram ddr5', '1tb disco', 'NVIDIA', 'rtx 4060', 14],
#     'PC2': ['Lenovo Legion 5', '16gb ram ddr4', '512gb disco', 'NVIDIA', 'rtx 3060', 15.6],
#     'PC3': ['Hp Victus', '8gb ram ddr4', '256gb disco', 'NVIDIA', 'rtx 3050', 15.6],
#     'PC4': ['Acer Nitro 5', '16gb ram ddr4', '1tb disco', 'NVIDIA', 'rtx 3050ti', 14],
#     'PC5': ['Asus Tuf Gaming', '16gb ram ddr4', '512gb disco', 'NVIDIA', 'rtx 3050ti', 15.6],
#     'PC6': ['Asus Rog Strix', '32gb ram ddr5', '1tb disco', 'NVIDIA', 'rtx 4070', 15.6],
# }

# bodega = {
#     'PC1': [1899990, 8],
#     'PC2': [699990, 15],
#     'PC3': [599990, 12],
#     'PC4': [599990, 6],
#     'PC5': [699990, 10],
#     'PC6': [1499990, 3],
#     ...
# }
# 
Notebooks = {
    'PC1': ['Asus Rog Zephyrus', '16gb ram ddr5', '1tb disco', 'NVIDIA', 'rtx 4060', 14],
    'PC2': ['Lenovo Legion 5', '16gb ram ddr4', '512gb disco', 'NVIDIA', 'rtx 3060', 15.6],
    'PC3': ['Hp Victus', '8gb ram ddr4', '256gb disco', 'NVIDIA', 'rtx 3050', 15.6],
    'PC4': ['Acer Nitro 5', '16gb ram ddr4', '1tb disco', 'NVIDIA', 'rtx 3050ti', 14],
    'PC5': ['Asus Tuf Gaming', '16gb ram ddr4', '512gb disco', 'NVIDIA', 'rtx 3050ti', 15.6],
    'PC6': ['Asus Rog Strix', '32gb ram ddr5', '1tb disco', 'NVIDIA', 'rtx 4070', 15.6],
    }
bodega = {
    'PC1': [1899990, 8],
    'PC2': [699990, 15],
    'PC3': [599990, 12],
    'PC4': [599990, 6],
    'PC5': [699990, 10],
    'PC6': [1499990, 3]
    }


def detalle_notebook(codigo) -> None:
    """Returns price and stock given a code """
    return None
    

def  busqueda_precio(precio_min, precio_max, bodega, notebooks) -> None:
    # Pedir max, min-> recorrer bodega-> Construir lista con notebooks: a)rango de precio pedido b) stock sobre 0. c) formato: codigo: x, modelo: y, precio: z, stock: W. d) no es necesario ordenar de menor a mayor, solo como se ingresan en la lista. e) en caso de estár vacío indicar: No se encontraron notebooks disponibles en el rango de precio ingresado.
    # PERMITE DECIMALES FLOAT
    pass


def leer_opcion() -> int:
    while True:
        try:
            opc = int(input("Seleccione una opción: "))
        except ValueError:
            print("Inváldio! Debe ingresar un valor numérico")
            continue
        else:
            if opc > 6 or opc < 1:
                print("Inválido! El rango de opciones es (1-6)")
                continue
            return opc

def buscar_codigo(codigo) -> bool:
    # buscar_codigo() nos dice si existe el codigo o no.
    
    # Solicitar codigo a usuario y nuevo precio a asignar. si el codigo existe en bodega el sistema actualiza el precio, de lo contrario se informa el error. Debe pedir confirmacion con string "s" o "n" para actualizar.
    pass

def actualizar_precio():
    buscar_codigo(codigo)
    # actualizar o irse
    # Confirmar
    pass

####

def validar_codigo(codigo) -> bool:
    while True:
        codigo = input("Ingrese el codigo").strip().upper
        if codigo == "":
            print("Inválido! No puedes dejar vacío este campo")
            continue
        return True
def validar_modelo(modelo) -> bool:
    while True:
        modelo = input("Ingrese el modelo").strip().upper
        if modelo == "":
            print("Inválido! No puedes dejar vacío este campo")
            continue
        return True
def validar_ram(ram) -> bool:
    while True:
        ram = input("Ingrese el ram").strip().upper
        if ram == "":
            print("Inválido! No puedes dejar vacío este campo")
            continue
        return True
def validar_disco(disco) -> bool:
    while True:
        disco = input("Ingrese el disco").strip().upper
        if disco == "":
            print("Inválido! No puedes dejar vacío este campo")
            continue
        return True
def validar_marca_grafica(marca_grafica) -> bool:
    while True:
        marca_grafica = input("Ingrese el marca_grafica").strip().upper
        if marca_grafica == "":
            print("Inválido! No puedes dejar vacío este campo")
            continue
        return True
def validar_grafica(grafica) -> bool:
    while True:
        grafica = input("Ingrese el grafica").strip().upper
        if grafica == "":
            print("Inválido! No puedes dejar vacío este campo")
            continue
        return True
def validar_dimension_pantalla(dimension_pantalla) -> bool:
    while True:
        dimension_pantalla = input("Ingrese el dimension_pantalla").strip().upper
        if dimension_pantalla == "":
            print("Inválido! No puedes dejar vacío este campo")
            continue
        return True
def validar_precio(precio) -> bool:
    while True:
        precio = input("Ingrese el precio").strip().upper
        if precio == "":
            print("Inválido! No puedes dejar vacío este campo")
            continue
        return True
def validar_stock(stock) -> bool:
    while True:
        stock = input("Ingrese el stock").strip().upper
        if stock == "":
            print("Inválido! No puedes dejar vacío este campo")
            continue
        return True

def agregar_notebook(codigo, modelo, ram, disco, marca_grafica, grafica, dimension_pantalla, precio, stock, notebooks, bodega):
####

###
# ELIMINAR NOTEBOOK
def eliminar_notebook(codigo) -> bool:
    # retorna bool para saber si existe o no el codigo, si se elimina == true, de lo contrario == false.
    buscar_codigo(codigo)
    

def menu() -> None:
    """Funcion menu principal: Incluye todas las funciones y terminio del menu"""
    
    while True:    
        print(f"== MENU ==\n1. Stock de Notebook por código\n2. Búsqueda de Notebooks por rango de precio\n3. Actualizar precio de un Notebook\n4. Agregar nuevo Notebook\n5. Eliminar Notebook\n6. Salir del programa")
        
        opc = leer_opcion()
        
        if opc == 1:
            pass
        elif opc == 2:
            pass
        elif opc == 3:
            pass
        elif opc == 4:
            pass
        elif opc == 5:
            pass
        elif opc == 6:
            print("Muchas gracias por usar el program")
            return None