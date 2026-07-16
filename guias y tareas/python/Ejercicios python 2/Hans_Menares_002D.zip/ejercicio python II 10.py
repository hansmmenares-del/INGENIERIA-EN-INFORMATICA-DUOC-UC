def validar_password():
    contraseña=str(input("Ingresa la contraseña:\n"))
    if contraseña=="python123":
        print("Acceso concebido")
    else:
        print("Acceso denegado")
validar_password()