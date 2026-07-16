## PEAJE AUTOMATICO
### MENU
# Registro motocicleta (500), auto(1000), camion(2500), reporte y salir
#### Reporte final: Llevar registro de cuantos autos van pasando y el dinero acumulado por auto, por camion, moto, conjunto, etc.
## Cuantos autos quiere ingresar?
## Patente del vehiculo se registra
#https://github.com/guillermovillacuratorres
MOTOCICLETA=500
AUTO=1000
CAMION=2500
cont_moto=0
cont_auto=0
cont_camion=0
acum_moto=0
acum_auto=0
acum_camion=0
while True:
    print("1 - Registro de Motocicleta")
    print("2 - Registro de Automóvil")
    print("3 - Registro de Camión")
    print("4 - Registro de Motocicleta")
    while True:
        try:
            opc=int(input("Seleccione una opción:\n"))
        except ValueError:
            print("Inválido!. Debes ingresar el número de opción")
        if opc>=1 and opc<=4:
            break
        else:
            print("Inválido!. Las opciones son (1, 2, 3, 4)")
    if opc==1:
        print("Has seleccionado la opcion 1")
        while True:
            try:
                cantidad=int(input("Ingresa la cantidad de motos a registrar: \n"))
            except ValueError:
                print("Debes ingresar una cantidad mayor a 0")
            if cantidad<=0:
                print("Debes ingresar una cantidad mayor a 0")
            else:
                break
        while True:
            for i in range(cantidad):
                patente=input("Ingrese la patente:\n")
                if len(patente)!=5:
                    print("Inválido!. La patente debe tener solo 5 caracteres")
                else:
                    if i==cantidad:
                        break
    if opc==1:
        print("Has seleccionado la opcion 2")
    if opc==1:
        print("Has seleccionado la opcion 3")
    if opc==4:
        break





