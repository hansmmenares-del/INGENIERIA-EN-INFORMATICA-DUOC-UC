correo=str(input("Ingresa tu correo electronico:\n"))
# Debe tener solo un '@' y solo un '.' despues del '@'
if correo.count("@")==1:
    if correo.count(".")==1:
        if correo.find("@")<correo.find("."):
            print("Correo Ingresado Válido")
        else:
            print("El correo debe tener un punto despues del '@'\nCorreo Inválido")
    else:
        print("El correo debe contener solo un punto\nCorreo inválido")
else:
    print("El correo debe contener solo un '@'\nCorreo Inválido")