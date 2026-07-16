Proceso suma_de_dos_numeros
	
	Definir primernumero, segundonumero, resultadoSuma como Entero;
	
	
	Escribir "Ingresa el primer numero: ";
	Repetir
		Leer primernumero;
		Si primernumero < 0 Entonces
			Escribir "Porfavor el numero debe ser positivo :D : ";
		FinSi
	Hasta Que primernumero >= 0
		
	Escribir "Ingresa el otro numero";
	Repetir
		Leer segundonumero;
		Si segundonumero < 0 Entonces
			Escribir "Este numero tambien debe ser positivo... :";
		FinSi
	Hasta Que segundonumero >= 0
	
	resultadoSuma = primernumero + segundonumero;
	
	Escribir "El resultado de la suma es: ", resultadoSuma;
	
FinProceso
