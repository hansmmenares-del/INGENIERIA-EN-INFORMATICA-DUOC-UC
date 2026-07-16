Proceso Ejercicios_de_programacion_parte_1
	
	Definir opc_root como Entero;
	
	Repetir
		Escribir "Selecciona el numero de la actividad que quieres usar: ";
		Escribir "(1-12)";
		Leer opc_root;
	Hasta Que opc_root <= 12 y opc_root >= 1;
	// ACT1
	Si opc_root = 1 Entonces
		Escribir "ELEGISTE ACT1";
		Definir num1_ej1, num2_ej1, resultadosuma_ej1 como Enteros;
		Leer num1_ej1;
		Leer num2_ej1;
		resultadosuma_ej1 = num1_ej1 + num2_ej1;
		Escribir "Resultado de la suma entre ", num1_ej1, " + ", num2_ej1, " = ", resultadosuma_ej1;
		
	FinSi
	//ACT2
	Si opc_root = 2 Entonces
		Escribir "ELEGISTE ACT2";
		Escribir "Para saber el area de la circunferencia ingresa el radio: ";
		Definir radio como Real;
		Definir areacircunf como Real;
		Leer radio;
		areacircunf = radio * radio * 3.1416;
		Escribir "El area de la circunferencia de radio ", radio, " es: ", areacircunf;
	FinSi
	//ACT3
	Si opc_root = 3 Entonces
		Escribir "Elegiste ACT3";
		Definir opc_act3 como Entero;
		Escribir "Selecciona la operación que quieres hacer";
		Escribir "(1) Suma de dos numeros";
		Escribir "(2) Resta de dos numeros";
		Escribir "(3) Mult de dos numeros";
		Escribir "(4) Div de dos numeros";
		Leer opc_act3;
		
		Limpiar Pantalla;
		Definir num1_ej3 como Entero;
		Definir num2_ej3 como Entero;
		Definir resultado_ej3 como Real;
		
		Si opc_act3 = 1 Entonces
			Escribir "Has elegido suma";
			Escribir "Ingresa el primer numero";
			Leer num1_ej3;
			Escribir "Ingresa el segundo numero";
			Leer num2_ej3;
			resultado_ej3 = num1_ej3 + num2_ej3;
			Escribir "El resultado es: ", resultado_ej3;
		SiNo Si opc_act3 = 2 Entonces
				Escribir "Has elegido resta";
				Escribir "Ingresa el primer numero";
				Leer num1_ej3;
				Escribir "Ingresa el segundo numero";
				Leer num2_ej3;
				resultado_ej3 = num1_ej3 - num2_ej3;
				Escribir "El resultado es: ", resultado_ej3;
			SiNo Si opc_act3 = 3 Entonces
					Escribir "Has elegido mult";
					Escribir "Ingresa el primer numero";
					Leer num1_ej3;
					Escribir "Ingresa el segundo numero";
					Leer num2_ej3;
					resultado_ej3 = num1_ej3 * num2_ej3;
					Escribir "El resultado es: ", resultado_ej3;
				SiNo Si opc_act3 = 4 Entonces
						Escribir "Has elegido div";
						Escribir "Ingresa el primer numero";
						Leer num1_ej3;
						Escribir "Ingresa el segundo numero";
						Leer num2_ej3;
						resultado_ej3 = num1_ej3/num2_ej3;
						Escribir "El resultado es: ", resultado_ej3;
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	
	//ACT4
	Si opc_root = 4 Entonces
		Escribir "Seleccionaste ACT4";
		Definir sueldoPerHora como Entero;
		Definir horasTrabajas como Entero;
		Definir bruto como Entero;
		Escribir "Para saber tu sueldo bruto primero debemos saber...";
		Escribir "cuanto ganas por hora?: ";
		Leer sueldoPerHora;
		Escribir "cuantas horas trabajaste este mes?: ";
		Leer horasTrabajas;
		bruto = sueldoPerHora * horasTrabajas;
		Escribir "Tu sueldo bruto es : ", "$", bruto;
		
	FinSi
	
	//ACT5
	Si opc_root = 5 Entonces
		Escribir "Seleccionaste ACT5";
		Definir Celsius, Farenheit como Real;
		Definir opc_act5 como Entero;
		Escribir "¿Qué quieres transformar?";
		Escribir "(1) Farenheit -> Celsius";
		Escribir "(2) Celsius -> Farenheit";
		Leer opc_act5;
		
		Si opc_act5 == 1 Entonces
			Escribir "Ingresa el valor de Farenheit: ";
			Leer Farenheit;
			Celsius = ((Farenheit-32)*5)/9;
			Escribir Farenheit, " Farenheit son: ", Celsius, " Celsius";
		SiNo Si opc_act5 == 2 Entonces
				Escribir "ingresa valor de Celsius: ";
				Leer Celsius;
				Farenheit = ((9/5)*Celsius) + 32;
				Escribir Celsius, " Celsius son: ", Farenheit, " Farenheit";
			FinSi
		FinSi
	FinSi
	Si opc_root == 6 Entonces
		Definir num1_ej6, num2_ej6, num3_ej6, sum12, mult23, divcruz como Reales;
		Leer num1_ej6, num2_ej6, num3_ej6;
		sum12 = num1_ej6 + num2_ej6;
		mult23 = num2_ej6 * num3_ej6;
		divcruz = sum12/mult23;
		Escribir "La division final es: ", divcruz;
	FinSi
	
	
	
	
	
FinProceso
