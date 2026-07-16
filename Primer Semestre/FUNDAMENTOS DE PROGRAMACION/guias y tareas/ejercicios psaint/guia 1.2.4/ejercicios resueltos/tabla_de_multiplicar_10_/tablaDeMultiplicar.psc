Proceso tablaDeMultiplicar
	
	
	Definir numeroIngresado, multiplo como Entero;
	
	Escribir "Ingresa el numero el cual quieres saber su tabla de multiplicacion: ";
	
	Leer numeroIngresado;
	multiplo = 1;
	
	
	Repetir
		
		Si numeroIngresado = 0 Entonces
			Escribir "¿No te sabes la tabla del 0?... Ingresa un numero positivo: ";
			Leer numeroIngresado;
		FinSi
		Si numeroIngresado < 0 Entonces
			Escribir "El numero ingresado debe ser positivo";
			Leer numeroIngresado;
		FinSi
		
	Hasta Que numeroIngresado >= 1
	
	Escribir "Aqui esta tu tabla querido :D";
	
	Mientras multiplo <= 10 Hacer
		
		Escribir numeroIngresado, " * ", multiplo, " = ", numeroIngresado * multiplo;
		multiplo = multiplo + 1;
		
	FinMientras
	
FinProceso