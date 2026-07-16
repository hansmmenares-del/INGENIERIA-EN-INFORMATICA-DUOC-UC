# Diccionarios iniciales
prendas = {
    'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
    'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
    'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
    'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
    'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
    'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False]
}

bodega = {
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2]
}

# --- FUNCIONES DE ENTRADA Y VALIDACIÓN REUTILIZABLES ---

def validar_string(mensaje:str) -> str:
    while True:
        valor = input(mensaje) ##E Tambien puede ser "input().strip()". Así cualquier espacio en blanco y vacíos quedan como vacios. despues verificas que el input == "": inválido. Esa sería la unica condicional, luego return valor
        if len(valor) == 0:
            print ("El texto no puede estar vacío")
        elif valor.replace(" ","") == "":
            print ("El texto no puede ser espacios en blanco")
        else:
            return valor

def validar_numeros_enteros(mensaje:str) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor == 0:
                print ("El valor no puede ser igual a cero")
            elif valor < 0:
                print ("El valor no puede ser negativo")
            else:
                return valor
        except ValueError:
            print ("ERROR")
def validar_float(mensaje:str) -> float:
    while True:
        try:
            valor = float(input(mensaje))
            if valor == 0:
                print ("El valor no puede ser igual a cero")
            elif valor < 0:
                print ("El valor no puede ser negativo")
            else:
                return valor
        except ValueError:
            print ("ERROR")



# --- FUNCIONES DEL SISTEMA ---

def buscar_codigo(codigo, diccionario):
    for clave in diccionario:
        if clave.lower() == codigo.lower():
            return True
    return False ### SUPER

def unidades_categoria(categoria, dicc_prendas, dicc_bodega):
    contador_unidades = 0
    for codigo in dicc_prendas:
        if dicc_prendas[codigo][1].lower() == categoria.lower():
            contador_unidades += dicc_bodega[codigo][1]
    print(f"El total de unidades disponibles es: {contador_unidades}")

def busqueda_precio(p_min, p_max, dicc_prendas, dicc_bodega):
    resultados = []
    for codigo in dicc_bodega:
        precio = dicc_bodega[codigo][0]
        unidades = dicc_bodega[codigo][1]
        if p_min <= precio <= p_max and unidades != 0: ### Podría ser raro pal profe... sería mejor ' if p_min <= precio and p_max >= precio and unidades > 0:
            nombre = dicc_prendas[codigo][0]
            resultados.append(nombre + "--" + codigo)
            
    # Contar elementos para el ordenamiento
    contador_resultados = 0
    for i in resultados:
        contador_resultados += 1
        
    ### Paso absolutamente inecesario, puedes poner el contador donde haces "resultados.append(..)", luego le sumas uno al contador.
    
    ###      contador_resultados = 0
    ###      for codigo in dicc_bodega:
    ###           precio = dicc_bodega[codigo][0]
    ###           unidades = dicc_bodega[codigo][1]
    ###           if p_min <= precio and p_max >= precio and unidades > 0:
    ###                 nombre = dicc_prendas[codigo][0]
    ###                 resultados.append(nombre + "--" + codigo)
    ###                 contador_resultados += 1
        
    if contador_resultados == 0:
        print("No hay prendas en ese rango de precios.")
    else:
        # Reemplazo de .sort(): Ordenamiento de burbuja manual
        for i in range(contador_resultados):
            for j in range(0, contador_resultados - i - 1):
                if resultados[j] > resultados[j + 1]:
                    temp = resultados[j]
                    resultados[j] = resultados[j + 1]
                    resultados[j + 1] = temp
                    
        for i in resultados:
            print(i)

def actualizar_precio(codigo, nuevo_precio, dicc_bodega):
    if buscar_codigo(codigo, dicc_bodega):
        for clave in dicc_bodega:
            if clave.lower() == codigo.lower():
                dicc_bodega[clave][0] = nuevo_precio
                return True
    return False

def agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades, dicc_prendas, dicc_bodega):
    valor_bool_unisex = True if es_unisex.lower() == 's' else False
    dicc_prendas[codigo] = [nombre, categoria, talla, color, material, valor_bool_unisex]
    dicc_bodega[codigo] = [precio, unidades]
    return True

def eliminar_prenda(codigo, dicc_prendas, dicc_bodega):
    if buscar_codigo(codigo, dicc_prendas):
        clave_encontrada = ""
        for clave in dicc_prendas:
            if clave.lower() == codigo.lower():
                clave_encontrada = clave
        if clave_encontrada != "":
            dicc_prendas.pop(clave_encontrada)
            dicc_bodega.pop(clave_encontrada)
            return True
    return False

# --- BUCLE PRINCIPAL ---
while True:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoria")
    print("2. Búsqueda de prendas por rango de precio")
    print("3. Actualizar precio de prenda")
    print("4. Agregar prenda")
    print("5. Eliminar prenda")
    print("6. Salir")
    print("====================================")
    
    opcion_elegida = validar_numeros_enteros("Ingrese opción: ")
    
    if opcion_elegida > 6:
        print("Debe seleccionar una opción válida")
        continue
        
    if opcion_elegida == 1:
        cat = validar_string("Ingrese categoria a consultar: ")
        unidades_categoria(cat, prendas, bodega)
        
    elif opcion_elegida == 2:
        while True:
            minimo = validar_numeros_enteros("Ingrese precio mínimo: ", 0)
            maximo = validar_numeros_enteros("Ingrese precio máximo: ", 0)
            if maximo >= minimo:
                busqueda_precio(minimo, maximo, prendas, bodega)
                break
            else:
                print("El máximo debe ser mayor o igual al mínimo.")
                
    elif opcion_elegida == 3:
        while True:
            cod = validar_string("Ingrese código de la prenda: ")
            n_precio = validar_numeros_enteros("Ingrese el nuevo precio: ", 1)
            
            if actualizar_precio(cod, n_precio, bodega):
                print("Precio actualizado")
            else:
                print("El código no existe")
                
            continuar = validar_string("¿Desea actualizar otro precio (s/n)?: ")
            if continuar.lower() != 's':
                break

    elif opcion_elegida == 4:
        cod = validar_string("Ingrese código: ")
        if buscar_codigo(cod, prendas):
            print("El código ya existe")
        else:
            # Reutilizamos validar_string para todas las entradas de texto
            nom = validar_string("Ingrese nombre: ")
            cat = validar_string("Ingrese categoría: ")
            talla = validar_string("Ingrese talla: ")
            color = validar_string("Ingrese color: ")
            mat = validar_string("Ingrese material: ")
            
            while True:
                unisex = validar_string("Ingrese si es unisex (s/n): ")
                if unisex.lower() == 's' or unisex.lower() == 'n':
                    break
                print("Error: Debe ingresar 's' o 'n'.")
                
            # Reutilizamos validar_numeros_enteros para los números
            prec = validar_numeros_enteros("Ingrese precio: ", 1)
            unid = validar_numeros_enteros("Ingrese unidades: ", 0)
            
            agregar_prenda(cod, nom, cat, talla, color, mat, unisex, prec, unid, prendas, bodega)
            print("Prenda agregada")
            
    elif opcion_elegida == 5:
        cod = validar_string("Ingrese el código de la prenda que desea eliminar: ")
        if eliminar_prenda(cod, prendas, bodega):
            print("Prenda eliminada")
        else:
            print("El código no existe")
            
    elif opcion_elegida == 6:
        print("Programa finalizado.")
        break