Proceso menu
	
	Definir  opc, numero1, numero2, resultado Como Entero;
	//sumar, restar, mult, div
	opc = 0;
	
	Mientras opc <> 5 Hacer
		
		Escribir "(1) - Sumar";
		Escribir "(2) - Restar";
		Escribir "(3) - Dividir";
		Escribir "(4) - Multiplicar";
		Escribir "(5) - Salir";
		Escribir "ingrese una opcion: ";
		Leer opc;
		
		Si opc == 1 Entonces
			Escribir "Has seleccionado (1) - Suma";
			Escribir "Ingresa el primer valor a sumar: ";
			Leer numero1;
			Escribir "Ingresa el segundo valor a sumar: ";
			Leer numero2;
			resultado = numero1 + numero2;
			Escribir "El resultado de la suma es : ", numero1, " + ", numero2, " = ", resultado;
			SiNo Si opc == 2 Entonces
				Escribir "Has seleccionado (2) - Resta";
				Escribir "Ingresa el primer valor a restar: ";
				Leer numero1;
				Escribir "Ingresa el segundo valor a restar: ";
				Leer numero2;
				resultado = numero1 - numero2;
				Escribir "El resultado de la resta es : ", numero1, " - ", numero2, " = ", resultado;
				
				Sino Si opc == 3 Entonces
					Escribir "Has seleccionado (3) - Dividir";
					Escribir "Ingresa el primer valor a dividir: ";
					Leer numero1;
					Escribir "Ingresa el segundo valor a dividir: ";
					Leer numero2;
					resultado = numero1 / numero2;
					Escribir "El resultado de la division es : ", numero1, " / ", numero2, " = ", resultado;
					
					Sino Si opc == 4 Entonces
						Escribir "Has seleccionado (4) - Multiplicar";
						Escribir "Ingresa el primer valor a Multiplicar: ";
						Leer numero1;
						Escribir "Ingresa el segundo valor a Multiplicar: ";
						Leer numero2;
						resultado = numero1 * numero2;
						Escribir "El resultado de la Multiplicacion es : ", numero1, " * ", numero2, " = ", resultado;
					FinSi
				FinSi
			FinSi
		FinSi
	FinMientras
FinProceso
