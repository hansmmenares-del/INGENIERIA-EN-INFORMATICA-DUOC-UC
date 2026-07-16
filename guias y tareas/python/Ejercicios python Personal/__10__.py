correo_ingresado=str(input("Ingresa tu correo electronico:\n"))
for i in correo_ingresado:
    
if correo_ingresado.count("@")!=1:
    print("El correo electronico ingresado no es valido.")
elif correo_ingresado.count(".")!=1:
    print("El correo electronico ingresado no es valido.")
elif 