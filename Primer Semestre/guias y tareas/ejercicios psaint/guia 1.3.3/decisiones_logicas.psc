Proceso decisiones_Logicas
	Definir hambre Como Caracter;
	Definir opc Como Entero; // opc será la opcion elegida por el usuario.
	
	Escribir "Tienes hambre? (s/n): ";
	
	Leer hambre;
	
	Si hambre == "s" Entonces
		
		Escribir "¿Qué quieres comer? Ingresa el numero del menu que deseas: ";
		Escribir "---Menu de hoy---";
		Escribir "(1) Pan con queso";
		Escribir "(2) Pan solo";
		
		Leer opc;
		
		Si opc == 1 Entonces
			Escribir "Has elegido Pan con queso";
		SiNo Si opc == 2 Entonces
				Escribir "Has Elegido Pan solo";
			FinSi
		FinSi
		
	SiNo Si hambre == "n" Entonces
			Escribir "Al parecer no tienes hambre todavia...";
		FinSi
		
	FinSi
	
FinProceso
