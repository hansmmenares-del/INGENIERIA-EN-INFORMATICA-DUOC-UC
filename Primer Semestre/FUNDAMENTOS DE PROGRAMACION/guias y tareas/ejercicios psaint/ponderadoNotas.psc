Proceso ponderadoNotas
	
	Definir not1, not2, not3, not4, notFinalPond, pon1, pon2, pon3, pon4 como Real;
	Definir menu_root, menu_1, menu_2, menu_3, menu_4 como Entero;
	Definir aprob, reprob como Entero;
	Definir sumapond como Real;
	aprob = 0;
	reprob = 0;
	Escribir "Aqui podras ingresar tus notas y ponderaciones para saber tu promedio y ramos aprobados";
	Esperar 1 Segundos;
	Limpiar Pantalla;
	
	Repetir
		Escribir "Ingresa la primera nota: ";
		Repetir
			Leer not1;
			Si not1 < 1.0 o not1 > 7.0 Entonces
				Escribir "La nota no puede ser menor a 1.0 ni mayor a 7.0...";
				Escribir"Vuelve a ingresar la primera nota: ";
			FinSi
		Hasta Que not1 >= 1.0 y not1 <= 7.0
		Escribir "Ingresa la segunda nota: ";
		Repetir
			Leer not2;
			Si not2 < 1.0 o not2 > 7.0 Entonces
				Escribir "La nota no puede ser menor a 1.0 ni mayor a 7.0...";
				Escribir"Vuelve a ingresar la segunda nota: ";
			FinSi
		Hasta Que not2 >= 1.0 y not2 <= 7.0
		Escribir "Ingresa la tercera nota: ";
		Repetir
			Leer not3;
			Si not3 < 1.0 o not3 > 7.0 Entonces
				Escribir "La nota no puede ser menor a 1.0 ni mayor a 7.0...";
				Escribir"Vuelve a ingresar la tercera nota: ";
			FinSi
		Hasta Que not3 >= 1.0 y not3 <= 7.0
		Escribir "Ingresa la cuarta nota: ";
		Repetir
			Leer not4;
			Si not4 < 1.0 o not4 > 7.0 Entonces
				Escribir "La nota no puede ser menor a 1.0 ni mayor a 7.0...";
				Escribir"Vuelve a ingresar la primera nota: ";
			FinSi
		Hasta Que not4 >= 1.0 y not4 <= 7.0
		Escribir "Ingresa la ponderacion de la primera nota: ";
		Repetir
			Repetir
				Leer pon1;
				Si pon1 <= 0 o pon1 >= 1 Entonces
					Escribir "La ponderacion no puede ser menor que 0, ";
					Escribir "tampoco puede ser mayor que 1. Recuerda 100% = 1, 50% = 0.5";
					Escribir "Vuelve a ingresar la ponderacion de la primera nota: ";
				FinSi
			Hasta Que pon1 >= 0 y pon1 <= 1
			Escribir "Ingresa la ponderacion de la segunda nota: ";
			Repetir
				Leer pon2;
				Si pon2 <= 0 o pon2 >= 1 Entonces
					Escribir "La ponderacion no puede ser menor que 0, ";
					Escribir "tampoco puede ser mayor que 1. Recuerda 100% = 1, 50% = 0.5";
					Escribir "Vuelve a ingresar la ponderacion de la primera nota: ";
				FinSi
			Hasta Que pon2 >= 0 y pon2 <= 1
			Escribir "Ingresa la ponderacion de la tercera nota: ";
			Repetir
				Leer pon3;
				Si pon3 <= 0 o pon3 >= 1 Entonces
					Escribir "La ponderacion no puede ser menor que 0, ";
					Escribir "tampoco puede ser mayor que 1. Recuerda 100% = 1, 50% = 0.5";
					Escribir "Vuelve a ingresar la ponderacion de la primera nota: ";
				FinSi
			Hasta Que pon3 >= 0 y pon3 <= 1
			Escribir "Ingresa la ponderacion de la cuarta nota: ";
			Repetir
				Leer pon4;
				Si pon4 <= 0 o pon4 >= 1 Entonces
					Escribir "La ponderacion no puede ser menor que 0, ";
					Escribir "tampoco puede ser mayor que 1. Recuerda 100% = 1, 50% = 0.5";
					Escribir "Vuelve a ingresar la ponderacion de la primera nota: ";
				FinSi
			Hasta Que pon4 >= 0 y pon4 <= 1
			sumapond = pon1 + pon2 + pon3 + pon4;
			Si sumapond <> 1 Entonces
				Escribir "La suma de las ponderaciones debe ser 100%... ";
				Escribir "La suma de tus ponderaciones es: ", sumapond*100, "%";
				Escribir "Ingresa de nuevo las ponderaciones...";
				Escribir "Ingresa la ponderacion de la primera nota: ";
			FinSi
		Hasta Que sumapond == 1
		
		notFinalPond = (not1*pon1)+(not2*pon2)+(not3*pon3)+(not4*pon4);
		
		
		// APROBADOS REPROBADOS //
		Si not1 >= 4 Entonces
			aprob = aprob + 1;
		SiNo Si not1 < 4 Entonces
				reprob = reprob + 1;
			FinSi
		FinSi
		Si not2 >= 4 Entonces
			aprob = aprob + 1;
		SiNo Si not2 < 4 Entonces
				reprob = reprob + 1;
			FinSi
		FinSi
		Si not3 >= 4 Entonces
			aprob = aprob + 1;
		SiNo Si not3 < 4 Entonces
				reprob = reprob + 1;
			FinSi
		FinSi
		Si not4 >= 4 Entonces
			aprob = aprob + 1;
		SiNo Si not4 < 4 Entonces
				reprob = reprob + 1;
			FinSi
		FinSi
		// APROBADOS REPROBADOS //
		
		
		Escribir "(1) Promedio ponderado";
		Escribir "(2) Cantidad de aprobados";
		Escribir "(3) Cantida de reprobados";
		Escribir "(4) Cambiar todas las notas o ponderaciones";
		Escribir "(5) Salir";
		Leer menu_root;
		
		Si menu_root == 1 Entonces
			Escribir "Promedio ponderado: ", notFinalPond;
		SiNo Si menu_root = 2 Entonces
				Escribir "Cantidad de aprobados: ", aprob;
				
			SiNo Si menu_root = 3 Entonces
					Escribir "Cantidad de reprobados: ", reprob;
				SiNo Si menu_root = 4 Entonces
						Escribir "Seleccionaste cambiar todas las notas o ponderaciones";
					FinSi
				FinSi
			FinSi
		FinSi
		
	Hasta Que menu_root == 5
FinProceso
