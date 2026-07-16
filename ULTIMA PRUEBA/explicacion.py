def validar_int(msg_input:str,msg_error:str,lim_inf:int, lim_sup:int, hay_lim_inf:bool,hay_lim_sup:bool):
    try:
        opc = int(input(msg_input))
    except ValueError:
        print(msg_error)
    else:
        if hay_lim_inf:
            if opc < lim_inf:
                print(msg_error)
        elif hay_lim_inf and hay_lim_sup:
            if opc < lim_inf or opc > lim_sup:
                print(msg_error)
        elif hay_lim_sup:
            if opc > lim_sup:
                print(msg_error)
        else:
            pass
        return opc

def menu():
    opc = validar_int("MENU\n(1) primera opcion.\n(2) segunda opcion\n(3) tercera opcion","error",1,3,True,True)
    
    if opc == 1:
        pass
    if opc == 2:
        pass
    if opc == 3:
        pass





    
    