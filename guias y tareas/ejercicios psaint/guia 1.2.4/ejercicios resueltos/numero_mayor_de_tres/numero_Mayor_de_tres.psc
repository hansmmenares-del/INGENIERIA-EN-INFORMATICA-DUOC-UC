Proceso numero_Mayor_de_tres
	
	Definir primernumero, segundonumero, tercernumero como Entero;
	
	Escribir "Ingresa el valor del primer numero: ";
	Leer primernumero;
	
	Escribir "Ingresa el valor del segundo numero: ";
	Leer segundonumero;
	
	Repetir
		
		Si primernumero = segundonumero Entonces
			Escribir "Sería mejor si (primernumero) y (segundonumero) no son iguales. Ingresa otro numero: ";
			Leer segundonumero;
		FinSi
		
	Hasta Que segundonumero <> primernumero
	
	Escribir "Ingresa el valor del tercer numero: ";
	Leer tercernumero;
	
	Repetir
		
		Si tercernumero = primernumero Entonces
			Escribir "Sería mejor si (tercernumero) y (primernumero) no son iguales. Ingresa otro numero: ";
			Leer tercernumero;
		FinSi
		Si tercernumero = segundonumero Entonces
			Escribir "Sería mejor si tercernumero y segundonumero no son iguales. Ingresa otro numero: ";
			Leer tercernumero;
		FinSi
		
	Hasta Que tercernumero <> primernumero y tercernumero <> segundonumero
	
	Si primernumero > segundonumero y primernumero > tercernumero Entonces
		Escribir "El número mayor entre ", primernumero, ", ", segundonumero, " y ", tercernumero, " es: ", primernumero;
		FinSi
	Si segundonumero > primernumero y segundonumero > tercernumero Entonces
		Escribir "El número mayor entre ", primernumero, ", ", segundonumero, " y ", tercernumero, " es: ", segundonumero;
		FinSI
	Si tercernumero > primernumero y tercernumero > segundonumero Entonces
		Escribir "El número mayor entre ", primernumero, ", ", segundonumero, " y ", tercernumero, " es: ", tercernumero;
	FinSi
	
FinProceso
