# Todo en funciones, uso de Lista[{dic},{dic2},etc...], menu se repite hasta salir, no IDs repetidos, si tarea no existe se da el anuncio.
all_tareas = []
pendientes = []
en_proceso = []
completadas = []
_msg_ = "Inválido! Debes ingresar un valor numérico"
def conxetumare() -> int|None:
    if len(all_tareas) == 0:
        return None
def validar_int(msg_input: str, msg_error: str, msg_out_of_bounds: str, hay_lim_inf: bool, hay_lim_sup: bool, lim_inf: int, lim_sup: int) -> int:
    while True:
        try:
            num = int(input(msg_input))
        except ValueError:
            print(msg_error)
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
def validar_str(msg_input: str, msg_es_vacio: str, msg_es_num: str) -> str:
    while True:
        errores = False
        texto = input(msg_input).strip()
        if texto == "":
            print(msg_es_vacio)
            errores = True
        for i in texto:
            if i.isnumeric():
                print(msg_es_num)
                errores = True
                break
        if errores:
            continue
        return texto
def agregar_tarea() -> None:
    while True:
        errores = False
        id_tarea = validar_int("Ingrese el ID de la tarea: ", _msg_, "", True, False, 0, 0)
        for categoria in all_tareas:
            for tarea in categoria:
                if id_tarea == tarea["id_tarea"]:
                    print("Inváldio! El ID ingresado ya existe!")
                    errores = True
                    break
            if errores:
                break
        if errores:
            continue
        break
    titulo = validar_str("Ingrese el titulo de la tarea: ", "Inválido! El titulo no puede estar vacío", "Inválido! El titulo no puede contener números")
    responsable = validar_str(f"Ingrese el nombre de la persona responsable de la tarea '{titulo}': ", "Inválido! Debe asignar al responsable de la tarea", "Inválido!_msg_")
    estado = validar_int("Seleccione el estado de la tarea:\n(1) Pendiente\n(2) En proceso\n(3) Completada", _msg_, "Inválido! El rango de opciones es (1-3)", True, True, 1, 3)
    if estado == 1:
        destino = "Pendiente"
    elif estado == 2:
        destino = "En proceso"
    elif estado == 3:
        destino = "Completada"
    dic = {
        "id_tarea" : id_tarea,
        "titulo" : titulo,
        "responsable" : responsable,
        "estado" : destino
        }
    if estado == 1:
        all_tareas.append(pendientes.append(dic))
    elif estado == 2:
        all_tareas.append(en_proceso.append(dic))
    elif estado == 3:
        all_tareas.append(completadas.append(dic))
    return None
def buscar_tarea() -> dict[str, str|int] | None:
    while True:
        opc = validar_int("= BUSCAR TAREA =\n(1) Buscar.\n(2) Volver.\nSeleccione una opción: ", _msg_, "Inválido! El rango de opciones es (1-2)", True, True, 1, 2)
        if opc == 1:
            opc = validar_int("\n(1) Buscar por ID de tarea.\n(2) Buscar por titulo de tarea.\nSeleccione una opción: ", _msg_, "Inválido! El rango de opciones es (1-2)", True, True, 1, 2)
            if opc == 1:
                errores = False
                a_buscar = validar_int("Ingresa el ID a buscar: ", _msg_, "Inválido! No existen los ID menores que 0", True, False, 0, 0)
                for categoria in all_tareas:
                    for tarea in categoria:
                        if a_buscar == tarea["id_tarea"]:
                            print(f"¡ID ENCONTRADO!\n- ID tarea: {tarea["id_tarea"]}\n- Título: {tarea["titulo"]}\n- Responsable: {tarea["responsable"]}\n- Estado: {tarea["destino"]}")
                            errores = False
                            return tarea
                        else:
                            errores = True
                if errores:
                    print(f"No se encuentra el ID '{a_buscar}'")
                    return None
            elif opc == 2:
                errores = False
                a_buscar = validar_str("Ingresa el Titulo de la tarea: ", "Inválido!", "Inválido! La busqueda de titulo solo permite ingresar caracteres como letras")
                for categoria in all_tareas:
                    for tarea in categoria:
                        if a_buscar == tarea["titulo"]:
                            print(f"¡TÍTULO ENCONTRADO!\n- ID tarea: {tarea["id_tarea"]}\n- Título: {tarea["titulo"]}\n- Responsable: {tarea["responsable"]}\n- Estado: {tarea["destino"]}")
                            errores = False
                            return tarea
                        else:
                            errores = True
                if errores:
                    print(f"No se encuentra el titulo '{a_buscar}'")
                    return None
        elif opc == 2:
            return None
def eliminar_tarea() -> None:
    print("= BORRAR TAREA =")
    a_eliminar = buscar_tarea()
    if a_eliminar != None:
        opc = validar_int("¿Desea borrar la tarea buscada?\n(1) Sí, borrar.\n(2) No, volver al menu.\nSeleccione una opción: ", _msg_, "Inválido! El rango de opciones es (1-2)", True, True, 1, 2)
        if opc == 1:
            for categoria in all_tareas:
                for tarea in categoria:
                    if a_eliminar == tarea:
                        print(f"Se eliminó con exito la siguiente tarea:\n- ID tarea: {tarea["id_tarea"]}\n- Título: {tarea["title"]}\n- Responsable: {tarea["responsable"]}\n- Estado: {tarea["Estado"]}")
                        categoria: list[dict[str, str|int]]
                        categoria.remove(tarea)
                        return None
        else:
            pass
    else:
        print("\nBorrar tarea se canceló\n")
        return None
def actualizar_estado_de_tarea() -> None:
    if conxetumare() == None:
        return None
    print("== ACTUALIZAR ==")
    a_actualizar = buscar_tarea()
    if a_actualizar != None:
        opc = validar_int("= MODIFICAR =\n(1) ID.\n(2) Título.\n(3) Responsable.\n(4) Estado de tarea.\n(5) Nada, volver", _msg_, "Inválido! El rango de opciones es (1-5)", True, True, 1, 5)
        if opc == 1:
            while True:
                errores = False
                a_actualizar = validar_int("Ingrese el nuevo ID: ", _msg_, "Inválido! El valor debe ser mayor o igual que 0", True, False, 0, 0)
                for categoria in all_tareas:
                    for tarea in categoria:
                        if a_actualizar == tarea["id_tarea"]:
                            print("Inválido! Ya existe ese ID, elige otro")
                            errores = True
                            break
                    if errores:
                        break
                if errores:
                    continue
                else:
                    tarea["id_tarea"] = a_actualizar
                    break
        elif opc == 2:
            while True:
                errores = False
                a_actualizar = validar_str("Ingrese el nuevo título: ", "Inválido! No puede dejar el campo vacío", "Inválido! No puede tener números el nuevo título")
                for categoria in all_tareas:
                    for tarea in categoria:
                        if a_actualizar == tarea["titulo"]:
                            print("Inválido! Ya existe ese título, elige otro")
                            errores = True
                            break
                    if errores:
                        break
                if errores:
                    continue
                else:
                    tarea["titulo"] = a_actualizar
                    print("Cambio se logró con exito!")
                    break
        elif opc == 3:
            a_actualizar = validar_str("Ingrese el nuevo responsable: ", "Inválido! No puede dejar el campo vacío", "Inválido! No puede tener números el nuevo responsable")
            all_tareas["responsable"] = a_actualizar
            print("Cambio se logró con exito!")
        elif opc == 4:
            opc = validar_int("(1) Pendiente\n(2) En proceso\n(3) Completada\nSeleccione una opción:", _msg_, "Inválido! El rango de opciones es (1-3)", True, True, 1, 3)
            all_tareas: list[list[dict[str, str|int]]]
            if opc == 1:
                if a_actualizar in all_tareas[pendientes]:
            elif opc == 2:
                pass
            elif opc == 3:
                pass
        elif opc == 5:
            return None
    else:
        print("Actualización cancelada")
        return None
def mostrar_tareas():
    for categoria in all_tareas:
        for tarea in categoria:
            print(f"{tarea["id_tarea"]}, ")
def menu() -> None:
    while True:
        opc = validar_int("=== MENU PRINCIPAL ===\n1. Agregar tarea\n2. Buscar tarea\n3. Eliminar tarea\n4. Actualizar estado de tarea\n5. Mostrar tareas\n6. Salir.\nSeleccione una opción: ", _msg_, "Inválido! El rango de opciones es (1-6)", True, True, 1, 6)
        if opc == 1:
            agregar_tarea()
        elif opc == 2:
            buscar_tarea()
        elif opc == 3:
            eliminar_tarea()
        elif opc == 4:
            actualizar_estado_de_tarea()
        elif opc == 5:
            mostrar_tareas()
        elif opc == 6:
            break
menu()