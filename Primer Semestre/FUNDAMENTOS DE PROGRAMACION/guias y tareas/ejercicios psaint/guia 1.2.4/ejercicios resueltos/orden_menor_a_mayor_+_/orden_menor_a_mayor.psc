Proceso orden_menor_a_mayor
	Definir primernumero, segundonumero, tercernumero como Enteros;
	
	Repetir
		
		Escribir "Ingresa el primer numero: ";
		Leer primernumero;
		
		
		Si primernumero <= 0 Entonces
			Escribir "(primernumero), (segundonumero) y (tercernumero) deben ser numeros positivos";
			Escribir "Porfavor vuelve a ingresar el valor de (primernumero)...";
		FinSi
		
	Hasta Que primernumero >= 0
	
	
	Repetir
		
		Escribir "Ingresa el segundo numero: ";
		Leer segundonumero;
		
		Si segundonumero = primernumero Entonces
			Escribir "Los numeros ingresados no pueden ser iguales...";
		FinSi
		
		Si segundonumero <= 0 Entonces
			Escribir "(primernumero), (segundonumero) y (tercernumero) deben ser numeros positivos";
			Escribir "Porfavor vuelve a ingresar el valor de (segundonumero)";
		FinSi
		
	Hasta Que segundonumero <> primernumero y segundonumero >= 0
	
	
	Repetir
		
		Escribir "Ingresa el tercer numero: ";
		Leer tercernumero;
		Si tercernumero=primernumero o tercernumero=segundonumero Entonces
			Escribir "Los numeros ingresados no pueden ser iguales...";
		FinSi
		Si tercernumero <= 0 Entonces
			Escribir "(primernumero), (segundonumero) y (tercernumero) deben ser numeros positivos";
			Escribir "Porfavor vuelve a ingresar el valor de (tercernumero)";
		FinSi
		
	Hasta Que tercernumero<>primernumero y tercernumero<>segundonumero y tercernumero >= 0
	
	
	Si primernumero > segundonumero y primernumero > tercernumero y segundonumero > tercernumero Entonces
		Escribir "El orden de los numeros de menor a mayor es: ", tercernumero, " < ", segundonumero, " < ", primernumero;
	FinSi
	SI primernumero > tercernumero y primernumero > segundonumero y tercernumero > segundonumero Entonces
		Escribir "El orden de los numeros de menor a mayor es: ", segundonumero, " < ", tercernumero, " < ", primernumero;
	FinSi
	Si segundonumero > primernumero y segundonumero > tercernumero y primernumero > tercernumero Entonces
		Escribir "El orden de los numeros de menor a mayor es: ", tercernumero, " < ", primernumero, " < ", segundonumero;
	FinSi
	Si segundonumero > tercernumero y segundonumero > primernumero y tercernumero > primernumero Entonces
		Escribir "El orden de los numeros de menor a mayor es: ", primernumero, " < ", tercernumero, " < ", segundonumero;
	FinSi
	SI tercernumero > primernumero y tercernumero > segundonumero y primernumero > segundonumero Entonces
		Escribir "El orden de los numeros de menor a mayor es: ", segundonumero, " < ", primernumero, " < ", tercernumero;
	FinSi
	Si tercernumero > segundonumero y tercernumero > primernumero y segundonumero > primernumero Entonces
		Escribir "El orden de los numeros de menor a mayor es: ", primernumero, " < ", segundonumero, " < ", tercernumero;
	FinSi
	
FinProceso
