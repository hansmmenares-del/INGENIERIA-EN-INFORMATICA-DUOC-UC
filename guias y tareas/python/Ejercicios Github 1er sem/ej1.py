import os
amount_of_motocicletas = 0
amount_of_autos = 0
amount_of_camiones = 0
total_amount_of_motocicletas = 0
total_amount_of_autos = 0
total_amount_of_camiones = 0
total_vehic = 0
VALUE_OF_EACH_MOTOCICLETA = 500
VALUE_OF_EACH_AUTO = 1000
VALUE_OF_EACH_CAMION = 2500
total_recaudado = 0
total_recaudado_motocicletas = 0
total_recaudado_autos = 0
total_recaudado_camiones = 0
registro_patente_motocicletas = []
registro_patente_autos = []
registro_patente_camiones = []
def clear():
    os.system("cls")
clear()
while True:
    print("---- MENU PEAJE ----\n\n(1) Registrar Motocicletas\n(2) Registrar Autos\n(3) Registrar Camiones\n(4) Salir y mostrar reporte\n\n")
    try:
        opc = int(input("Selecciona una opción:\n"))
        if opc not in [1,2,3,4]:
            clear()
            print("¡Inválido! Debes seleccionar una opción (1, 2, 3, 4)")
    except ValueError:
        clear()
        print("¡Inválido! Debes seleccionar una opción (1, 2, 3, 4)")
    else:
        if opc == 1:
            clear()
            while True:
                try:
                    amount_of_motocicletas = int(input("Ingresa la cantidad de motocicletas a ingresar:\n"))
                except ValueError:
                    clear()
                    print("¡Inválido! Si quieres volver al menu ingresa el número '0'...")
                else:    
                    if amount_of_motocicletas < 0:
                        clear()
                        print("¡Inválido! Solo se pueden ingresar cantidades positivas.\nSi quieres volver al menu ingresa el número 0")
                    elif amount_of_motocicletas == 0:
                        clear()
                        break
                    else:
                        contador_comodin = 0
                        for i in range(amount_of_motocicletas):
                            while True:
                                patente = input("Ingresa la patente de la moto (ej, abc12):\n")
                                patente = patente.strip().upper()
                                if len(patente) != 5:
                                    clear()
                                    print("¡Patente inválida! Solo puede tener 5 caracteres")
                                elif not patente[:3].isalpha():
                                    clear()
                                    print("¡Patente inválida! Los primeros 3 caracteres deben ser letras")
                                elif not patente[3:].isnumeric():
                                    clear()
                                    print("¡Patente inválida! Los últimos 2 caracteres deben ser números entre 0-9")
                                else:
                                    contador_comodin+=1
                                    clear()
                                    print(f"Patentes ingresadas: {contador_comodin}\nFaltan: {amount_of_motocicletas-contador_comodin}")
                                    break
                            total_amount_of_motocicletas+=1
                            registro_patente_motocicletas.append(patente)
                            total_recaudado_motocicletas+=VALUE_OF_EACH_MOTOCICLETA
                        clear()
                        print("¡Operación realizada con éxito!")
                        break
        elif opc==2:
            clear()
            while True:
                try:
                    amount_of_autos = int(input("Ingresa la cantidad de autos a ingresar:\n"))
                except ValueError:
                    clear()
                    print("Inválido! Si quieres volver al menu ingresa el número '0'...")
                else:
                    if amount_of_autos < 0:
                        clear()
                        print("Inválido! Solo se pueden ingresar cantidades positivas.\nSi quieres volver al menu ingresa el número 0")
                    elif amount_of_autos == 0:
                        clear()
                        break
                    else:
                        contador_comodin = 0
                        for i in range(amount_of_autos):
                            while True:
                                patente=input("Ingresa la patente del auto (ej, abcd12):\n")
                                patente=patente.strip().upper()
                                if len(patente)!=6:
                                    clear()
                                    print("Patente inválida! Solo puede tener 6 caracteres")
                                elif not patente[:4].isalpha():
                                    clear()
                                    print("Patente inválida! Los primeros 4 caracteres deben ser letras...")
                                elif not patente[4:].isnumeric():
                                    clear()
                                    print("Patente inválida! Los últimos 2 caracteres deben ser números entre 0-9")
                                else:
                                    contador_comodin+=1
                                    clear()
                                    print(f"Patentes ingresadas: {contador_comodin}\nFaltan: {amount_of_autos-contador_comodin}")
                                    break
                            total_amount_of_autos+=1
                            registro_patente_autos.append(patente)
                            total_recaudado_autos+=VALUE_OF_EACH_AUTO   
                        clear()
                        print("¡Operación realizada con éxito!")
                        break
        elif opc==3:
            clear()
            while True:
                try:
                    amount_of_camiones = int(input("Ingresa la cantidad de camiones a ingresar:\n"))
                except ValueError:
                    clear()
                    print("Inválido! Si quieres volver al menu ingresa el número '0'...")
                else:
                    if amount_of_camiones < 0:
                        clear()
                        print("Inválido! Solo se pueden ingresar cantidades positivas.\nSi quieres volver al menu ingresa el número 0")
                    elif amount_of_camiones == 0:
                        clear()
                        break
                    else:
                        contador_comodin=0
                        for i in range(amount_of_camiones):
                            while True:
                                patente=input("Ingresa la patente del camión (ej, abcd12):\n")
                                patente=patente.strip().upper()
                                if len(patente)!=6:
                                    clear()
                                    print("Patente inválida! Solo puede tener 6 caracteres")
                                elif not patente[:4].isalpha():
                                    clear()
                                    print("Patente inválida! Los primeros 4 caracteres deben ser letras...")
                                elif not patente[4:].isnumeric():
                                    clear()
                                    print("Patente inválida! Los últimos 2 caracteres deben ser números entre 0-9")
                                else:
                                    contador_comodin+=1
                                    clear()
                                    print(f"Patentes ingresadas: {contador_comodin}\nFaltan: {amount_of_camiones-contador_comodin}")
                                    break
                            total_amount_of_camiones+=1
                            registro_patente_camiones.append(patente)
                            total_recaudado_camiones+=VALUE_OF_EACH_CAMION 
                        clear()
                        print("¡Operación realizada con éxito!")
                        break                
        elif opc==4:
            clear()
            break
total_vehic = total_amount_of_motocicletas + total_amount_of_autos + total_amount_of_camiones

total_recaudado = total_recaudado_motocicletas + total_recaudado_autos + total_recaudado_camiones

print(f"---- REPORTE FINAL ----\n--- Recaudado:\nMotos -> {total_recaudado_motocicletas}\nAutos -> {total_recaudado_autos}\nCamiones -> {total_recaudado_camiones}")
print(f"Total recaudado = {total_recaudado}")
print(f"--- Cantidad de vehículos: Motos -> {total_amount_of_motocicletas}\nAutos -> {total_amount_of_autos}\nCamiones -> {total_amount_of_camiones}")
total_vehic = total_amount_of_motocicletas + total_amount_of_autos + total_amount_of_camiones
print(f"Total vehículos ingresados = {total_vehic}")
while True:
    try:
        opc = int(input("¿Mostrar lista de patentes?\n(1) Mostrar y salir\n(0) Solo salir\n"))
        if opc not in [1,0]:
            clear()
            print("Ingresa 1 o 0...")
    except ValueError:
        clear()
        print("Ingresa 1 o 0...")
    else:
        if opc == 1:
            clear()
            print(f"Patentes de motocicletas: {registro_patente_motocicletas}\nPatentes de autos: {registro_patente_autos}\nPatentes de camiones: {registro_patente_camiones}")
            break
print("Whatever you say...!!!")