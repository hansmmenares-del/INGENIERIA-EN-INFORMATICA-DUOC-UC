Proceso mayorDeEdad
	
	Definir edadIngresada, diferenciaDeEdad como Entero;
	
	Escribir "¿Qué edad tienes Pedro?: ";
	
	
	Repetir
		
		Leer edadIngresada;
		diferenciaDeEdad = 18 - edadIngresada;
		
		
		Si edadIngresada < 0 Entonces
			Escribir "Pedro, no es posible que aun no hallas nacido... Ingresa tu edad real: ";
		FinSi
		
		
		Si edadIngresada = 0 Entonces
			Escribir "Pedro, ¿acabas de nacer?... Ingresa tu edad real: ";
		FinSi
		
		
		Si edadIngresada < 18 y edadIngresada > 0 y diferenciaDeEdad = 1 Entonces
			Escribir "Lo siento mucho, Pedro. Tan solo debes esperar un año :D";
		FinSi
		
		
		Si edadIngresada < 18 y edadIngresada > 0 y diferenciaDeEdad <> 1 Entonces
			Escribir "Lo siento, Pedro. Quizas debas esperar unos ", diferenciaDeEdad, " años :)";
		FinSi
		
		
		Si edadIngresada > 18 Entonces
			Escribir "Pedro, eres mayor de edad. Felicitaciones";
		FinSi
	Hasta Que edadIngresada > 0
	
FinProceso