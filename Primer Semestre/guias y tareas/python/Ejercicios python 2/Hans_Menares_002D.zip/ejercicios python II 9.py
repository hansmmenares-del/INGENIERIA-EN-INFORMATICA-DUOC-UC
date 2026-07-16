def calculadora():
    num1=float(input("Ingrese el primero numero:\n"))
    num2=float(input("Ingrese el segundo numero:\n"))
    operacion=str(input("Ingrese la operacion: (+ o -)\n"))
    if operacion == "+":
        resultado=num1+num2
    elif operacion == "-":
        resultado=num1-num2
    print(f"El resultado es: {resultado}")
calculadora()
    
    
    