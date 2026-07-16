Proceso MenuDePractica
	Definir opc_root Como Entero;
	Definir co_modin, co_modin2 Como Entero;
	Definir result Como Entero;
	Definir num1, num2, num3, num4, num5 como Enteros;
	
	Escribir "--- Estos son los Menu de practica para la prueba de Fundamentos de Programacion 2026 1er sem ---";
	Esperar 2 Segundos;
	Limpiar Pantalla;
	
	Escribir "Selecciona el menu que quieres acceder";
	Repetir
		Escribir "(1) Menu de Calculadora +,-,*,/,!";
		Escribir "(2) Menu de Conversion de unidades";
		Escribir "(3) Menu de Cargar combustible";
		Escribir "(4) Menu de Calculo de promedio";
		Escribir "(5) Menu de (xxxxx)";
		Escribir "(6) Terminar Programa...";
		Leer opc_root;
		Si opc_root <> 1 y opc_root <> 2 y opc_root <> 3 y opc_root <> 4 y opc_root <> 5 y opc_root <> 6 Entonces
			Limpiar Pantalla;
			Escribir "Inténtalo denuevo, debes selecionar una opcion... ";
			Escribir "Si quieres terminar el programa selecciona (6)... ";
			Escribir "";
			Esperar 1 Segundos;
		FinSi
	Hasta Que opc_root == 1 o opc_root == 2 o opc_root == 3 o opc_root == 4 o opc_root == 5 o opc_root == 6
	
	Limpiar Pantalla;
	
	// Menu Calculadora
	Si opc_root == 1 Entonces
		Escribir "Seleccionaste el menu de calculadora";
		Esperar 2 Segundos;
		Limpiar Pantalla;
		
		// Seleccion de operacion
		Repetir 
			Limpiar Pantalla;
			Escribir "Selecciona la operación que deseas hacer: ";
			Escribir "(1) Suma";
			Escribir "(2) Resta";
			Escribir "(3) Multiplicación";
			Escribir "(4) División";
			Escribir "(5) Factorial";
			Leer opc_menu;
			// Error de seleccion de operacion
			Si opc_menu <> 1 y opc_menu <> 2 y opc_menu <> 3 y opc_menu <> 4 y opc_menu <> 5 y opc_menu <> 6 Entonces
				Escribir "Inténtalo denuevo, tu seleccion es inválida... ";
				Escribir "";
				Esperar 1 Segundos;
			SiNo Si opc_menu == 1 Entonces
					Limpiar Pantalla;
					Escribir "Seleccionaste Suma";
					Esperar 1 Segundo;
					Limpiar Pantalla;
				SiNo Si opc_menu == 2 Entonces
						Limpiar Pantalla;
						Escribir "Seleccionaste Resta";
						Esperar 1 Segundo;
						Limpiar Pantalla;
					SiNo Si opc_menu == 3 Entonces
							Limpiar Pantalla;
							Escribir "Seleccionaste Multiplicación";
							Esperar 1 Segundo;
							Limpiar Pantalla;
						Sino Si opc_menu == 4 Entonces
								Limpiar Pantalla;
								Escribir "Seleccionaste División";
								Esperar 1 Segundo;
								Limpiar Pantalla;
							Sino Si opc_menu == 5 Entonces
									Limpiar Pantalla;
									Escribir "Seleccionaste Factorial";
									Esperar 1 Segundo;
									Limpiar Pantalla;
								FinSi
							FinSi
						FinSi
					FinSi
				Finsi
			FinSi
		Hasta Que opc_menu == 1 o opc_menu == 2 o opc_menu == 3 o opc_menu == 4 o opc_menu == 5
		Si opc_menu == 1 Entonces
			Repetir
				Escribir "Ingresa la cantidad de números que quieres sumar:";
				Escribir "(Solo hasta cinco números y deben haber mínimo dos números)";
				Escribir "Por ej: 4";
				Leer co_modin;
				Si co_modin == 5 Entonces
					Escribir "Entrega los valores uno a uno de los cinco números a sumar: ";
					Escribir "Primer número: ";
					Leer num1;
					Escribir "Segundo número: ";
					Leer num2;
					Escribir "Tercer número: ";
					Leer num3;
					Escribir "Cuarto número: ";
					Leer num4;
					Escribir "Quinto número: ";
					Leer num5;
					result = num1 + num2 + num3 + num4 + num5;
					Escribir "El resultado de ", num1, " + ", num2," + ", num3, " + ", num4, " + ", num5, " = ", result;
				SiNo Si co_modin == 4 Entonces
						Escribir "Entrega los valores uno a uno de los cuatro números a sumar: ";
						Escribir "Primer número: ";
						Leer num1;
						Escribir "Segundo número: ";
						Leer num2;
						Escribir "Tercer número: ";
						Leer num3;
						Escribir "Cuarto número: ";
						Leer num4;
						result = num1 + num2 + num3 + num4;
						Escribir "El resultado de ", num1, " + ", num2," + ", num3, " + ", num4, " = ", result;
					SiNo Si co_modin == 3 Entonces
							Escribir "Entrega los valores uno a uno de los tres números a sumar: ";
							Escribir "Primer número: ";
							Leer num1;
							Escribir "Segundo número: ";
							Leer num2;
							Escribir "Tercer número: ";
							Leer num3;
							result = num1 + num2 + num3;
							Escribir "El resultado de ", num1, " + ", num2," + ", num3, " = ", result;
						SiNo Si co_modin == 2 Entonces
								Escribir "Entrega los valores uno a uno de los tres números a sumar: ";
								Escribir "Primer número: ";
								Leer num1;
								Escribir "Segundo número: ";
								Leer num2;
								Escribir "Tercer número: ";
								Leer num3;
								result = num1 + num2;
								Escribir "El resultado de ", num1, " + ", num2, " = ", result;
							Sino Si co_modin <> 2 y co_modin <> 3 y co_modin <> 4 y co_modin <> 5 Entonces
									co_modin = 0;
									Escribir "Opción no válida... ";
									Esperar 1 Segundos;
									Limpiar Pantalla;
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			Hasta Que co_modin = 2 o co_modin = 3 o co_modin = 4 o co_modin = 5
		SiNo Si opc_menu == 2 Entonces
				// Resta
				Repetir
					Escribir "Ingresa la cantidad de números que quieres restar:";
					Escribir "(Solo hasta cinco números y deben haber mínimo dos números)";
					Escribir "Por ej: 4";
					Leer co_modin;
					Si co_modin == 5 Entonces
						Escribir "Entrega los valores uno a uno de los cinco números a restar: ";
						Escribir "Primer número: ";
						Leer num1;
						Escribir "Segundo número: ";
						Leer num2;
						Escribir "Tercer número: ";
						Leer num3;
						Escribir "Cuarto número: ";
						Leer num4;
						Escribir "Quinto número: ";
						Leer num5;
						result = num1 - num2 - num3 - num4 - num5;
						Escribir "El resultado de ", num1, " - ", num2," - ", num3, " - ", num4, " - ", num5, " = ", result;
					SiNo Si co_modin == 4 Entonces
							Escribir "Entrega los valores uno a uno de los cuatro números a restar: ";
							Escribir "Primer número: ";
							Leer num1;
							Escribir "Segundo número: ";
							Leer num2;
							Escribir "Tercer número: ";
							Leer num3;
							Escribir "Cuarto número: ";
							Leer num4;
							result = num1 - num2 - num3 - num4;
							Escribir "El resultado de ", num1, " - ", num2," - ", num3, " - ", num4, " = ", result;
						SiNo Si co_modin == 3 Entonces
								Escribir "Entrega los valores uno a uno de los tres números a restar: ";
								Escribir "Primer número: ";
								Leer num1;
								Escribir "Segundo número: ";
								Leer num2;
								Escribir "Tercer número: ";
								Leer num3;
								result = num1 - num2 - num3;
								Escribir "El resultado de ", num1, " - ", num2," - ", num3, " = ", result;
							SiNo Si co_modin == 2 Entonces
									Escribir "Entrega los valores uno a uno de los tres números a sumar: ";
									Escribir "Primer número: ";
									Leer num1;
									Escribir "Segundo número: ";
									Leer num2;
									Escribir "Tercer número: ";
									Leer num3;
									result = num1 - num2 - num3;
									Escribir "El resultado de ", num1, " - ", num2," - ", num3, " = ", result;
								Sino Si co_modin <> 2 y co_modin <> 3 y co_modin <> 4 y co_modin <> 5 Entonces
										co_modin = 0;
										Escribir "Opción no válida... ";
										Esperar 1 Segundos;
										Limpiar Pantalla;
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				Hasta Que co_modin = 2 o co_modin = 3 o co_modin = 4 o co_modin = 5
				//
			FinSi
		FinSi
	FinSi
	Si opc_menu == 2 Entonces
		Escribir "Seleccionaste el menu de Conversión de Unidades... Esto continuará";
	FinSi
	
	
FinProceso
