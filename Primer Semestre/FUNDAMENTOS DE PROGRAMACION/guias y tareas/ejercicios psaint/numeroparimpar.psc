Proceso numeroparimpar
	Definir opciones1234 como entero;
	definir num1, resultado, num2, lado1, lado2, lado3 como entero;

	Escribir "Qué proceso quieres ingresar?";
	leer opciones1234;
	Si opciones1234 == 1 Entonces
		
		// se pide ingresar el valor de numero1
		Escribir "(RESTO) Ingrese un numero: ";
		leer num1;
		resultado = num1 mod 2;
		
		Escribir "El resto de ", num1, " usando 2 como divisor es: ", resultado;
		Si resultado == 0 Entonces
			Escribir "Por lo tanto el numero es par";
		SiNo Escribir "Por lo tanto el numero es impar";
		FinSi
		
		
	FinSI
	Si opciones1234 == 2 Entonces
		
		Escribir "(>10) Ingresa un numero (num2)";
		Leer num2;
		
		Si num2 > 10 Entonces
			Escribir "Tu numero es mayor que 10";
		Sino Si num2 < 10 Entonces
				Escribir "Tu numero es menor que 10";
			Sino Si num2 = 10 Entonces
					Escribir "Tu numero es 10";
				FinSi
			FinSI
		FinSi
		
	FinSi
	Si opciones1234 == 3 Entonces
		
		Escribir "(1er metodo, -si- separados) ingresa la medida en cm del lado1: ";
		leer lado1;
		Repetir
			Si lado1 <= 0 Entonces
				Escribir "El valor no puede ser negativo ni 0, ingresa otro valor positivo: ";
				Leer lado1;
			FinSi
		Hasta Que lado1 > 0;
		
		Escribir "ingresa la medida en cm del lado2: ";
		leer lado2;
		Repetir
			Si lado2 <= 0 Entonces
				Escribir "El valor no puede ser negativo ni 0, ingresa otro valor positivo: ";
				Leer lado2;
			FinSi
		Hasta Que lado2 > 0;
		
		Escribir "ingresa la medida en cm del lado3: ";
		Repetir
			leer lado3;
			Si lado3 <= 0 Entonces
				Escribir "El valor no puede ser negativo ni 0, ingresa otro valor positivo: ";
			FinSi
		Hasta Que lado3 > 0;
		
		Si lado1 == lado2 y lado1 == lado3 Entonces
			Escribir "Tu triangulo es equilatero";
		FinSi
		Si (lado1 <> lado2 y lado2 == lado3) o (lado2 <> lado3 y lado1 == lado2 ) Entonces
			Escribir "Tu triangulo es isoseles";
		FinSi
		Si lado1<>lado2  y lado2 <> lado3 Entonces
			Escribir "Tu triangulo es escaleno";
		FinSi
		
	FinSi
	
	
	Si opciones1234 == 4 Entonces
		Escribir "FORMA ANIDADA";
		Escribir "Ingresa de forma ordenada los valores de lado1, lado2 y lado3: ";
		
		leer lado1, lado2, lado3;
		Repetir
			Si lado1 <=0 o lado2 <= 0 o lado3 <= 0 Entonces
				Escribir "vuelva a ingresar los valores: ";
				Leer lado1, lado2, lado3;
			FinSi
		Hasta que lado1 > 0 y lado2 > 0 y lado3 > 0;
		si lado1 == lado2 y lado2 == lado3 Entonces
			Escribir "equilatero";
		sino si lado1 <> lado2 y lado2 == lado3 Entonces
				Escribir "isoseles";
			sino si lado1 == lado2 y lado2 <> lado3 Entonces
					Escribir "isoseles";
				sino si lado1 <> lado2 y lado2 <> lado3 Entonces
						Escribir "escaleno";
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	
FinProceso
