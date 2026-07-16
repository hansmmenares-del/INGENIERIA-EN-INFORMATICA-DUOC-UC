all_tareas = []
# Validacion enteros
def validar_int(msg_input:str,msg_error:str,out_of_bounds:str,hay_lim_inf:bool,hay_lim_sup:bool,lim_inf:int,lim_sup:int):
    while True:
        try:
            num = int(input(msg_input))
        except ValueError:
            print(msg_error)
        else:
            if hay_lim_inf:
                if num < lim_inf:
                    print(out_of_bounds)
                    continue
            elif hay_lim_inf and hay_lim_sup:
                if num < lim_inf or num > lim_sup:
                    print(out_of_bounds)
                    continue
            elif hay_lim_sup:
                if num > lim_sup:
                    print(out_of_bounds)
                    continue
            return num
# Validacion strings (solo que no este vacío y sin numeros)
def validar_str(msg_input, msg_es_vacio, msg_es_numeric) -> str:
    while True:
        errores = False
        texto = input(msg_input).strip().title()
        if texto == "":
            print(msg_es_vacio)
            continue
        for i in texto:
            if i.isnumeric():
                print(msg_es_numeric)
                errores = True
                break
        if errores:
            continue
        return texto
# Agregar diccionario de tareas
def agregar_tarea(lista_para_agregar_dic:list):
    estado = "pendiente"
    _id_, titulo, responsable = preguntar_por_datos()
    dic_datos_tarea = {
    "id" : _id_,
    "titulo" : titulo,
    "responsable" : responsable,
    "estado" : estado
}
    lista_para_agregar_dic.append(dic_datos_tarea)
def preguntar_por_datos():
    _id_input_de_usuario = validar_int("Ingrese el id: ", "Inválido!", "Inválido! Te sales de  los limites", True, False, 0, 0)
    titulo_input_usuario = validar_str("Ingresa el titulo: ", "Inválido! Vacío", "Inválido! no puede ser numero")
    responsable_input_usuario = validar_str("Ingresa el nombre del responsable: ", "Inválido! Vacío", "Inválido! no puede ser numero")
    return _id_input_de_usuario, titulo_input_usuario, responsable_input_usuario
def buscar_tarea():
    opc = validar_int("(1) Por id.\n(2) Por titulo.\n(3) Por responsable.\nSeleccione una opción: ", "Inválido! solo numeros", "Inválido! Te sales de los limites", True, True, 1, 3)
    if opc == 1:
        buscar_por_id()
    elif opc == 2:
        buscar_por_titulo()
    elif opc == 3:
        mostrar_key_tarea()
        buscar_por_responsable()
def ver_todas_las_tareas(lista_a_mostrar:list):
    print(lista_a_mostrar[])
def borrar_tarea():
    pass
def menu() -> None:
    while True:
        print("== MENU ==\n(1) Add.\n(2) Search.\n(3) See all.\n(4) Erase.\n(5) Quit.")
        opc = validar_int("Seleccione una opcion: ", "Inválido! solo numeros", "Inváldio! Te sales de los limites", True, True, 1, 5)
        if opc == 1:
            agregar_tarea(all_tareas)
        elif opc == 2:
            buscar_tarea()
        elif opc == 3:
            ver_todas_las_tareas()
        elif opc == 4:
            borrar_tarea()
        elif opc == 5:
            break




# git fetch [link repo a clonar]
# git pull
# git add .
# git commit -m "lll"
# git push