Proceso ejercicio_promedioPonderado
	
	// NOTAS Y PONDERACIONES //
	Definir nota1 como Real;
	Definir nota2 como Real;
	Definir nota3 como Real;
	Definir nota4 como Real;
	Definir pond1 como Real;
	Definir pond2 como Real;
	Definir pond3 como Real;
	Definir pond4 como Real;
	// NOTAS Y PONDERACIONES //
	
	
	// COMODINES //
	Definir opc_menu como Entero;
	Definir ponderado_final como Real;
	Definir aprobadoreprobado1 como Caracter;
	Definir aprobadoreprobado2 como Caracter;
	Definir aprobadoreprobado3 como Caracter;
	Definir aprobadoreprobado4 como Caracter;
	Definir mi100porc como Real;
	// COMODINES //
	
	
	// CONTADORES //
	Definir contadorAprobado como Entero;
	Definir contadorReprobado como Entero;
	contadorAprobado = 0;
	contadorReprobado = 0;
	// CONTADORES //
	
	
	Escribir "A continuacion deberas ingresar la nota como decimal con punto,";
	Escribir "junto a su ponderacion como decimal con punto... ";
	Escribir "";
	Escribir "Por ejemplo";
	Escribir "nota 1: 4.5 -> ENTER -> 0.3";
	Escribir "nota 2: 6.7 -> ENTER -> 0.4";
	Escribir "";
	
	// INPUT USUARIO: NOTAS //
	Repetir
		
		Escribir "Ingresa la primera nota con su ponderacion";
		Leer nota1, pond1;
		Escribir "Ingresa la segunda nota con su ponderacion";
		Leer nota2, pond2;
		Escribir "Ingresa la tercera nota con su ponderacion";
		Leer nota3, pond3;
		Escribir "Ingresa la cuarta nota con su ponderacion";
		Leer nota4, pond4;
		
		mi100porc = pond1 + pond2 + pond3 + pond4;
		
		Limpiar Pantalla;
		
		Si mi100porc <> 1 Entonces
			Escribir "Algo anda mal, revisa las ponderaciones";
			Escribir "Recuerda escribirlos como decimales con punto...";
			Escribir "";
		FinSi
		
	Hasta Que mi100porc == 1
	
	Limpiar Pantalla;
	
	Escribir "Ya ingresaste tus 4 notas y sus ponderaciones :D";
	Escribir "";
	
	// MENU
	Escribir "A continuacion se muestra el menu de opciones... ";
	Escribir "--------- MENU ---------";
	Escribir "(1) Mostrar promedio ponderado";
	Escribir "(2) Mostrar cantidad de aprobadas";
	Escribir "(3) Mostrar cantidad de reprobadas";
	Escribir "(4) Salir";
	Leer opc_menu;
	
	// ----------------- CALCULOS ----------------- //
	ponderado_final = (nota1*pond1)+(nota2*pond2)+(nota3*pond3)+(nota4*pond4);
	
	Si nota1 >= 4 Entonces
		//aprobadoreprobado1 = "Aprobado :D";
		contadorAprobado = contadorAprobado + 1;
	SiNo Si nota1 < 4 Entonces
			aprobadoreprobado1 = "Reprobado :(";
			contadorReprobado = contadorReprobado + 1;
		FinSi
	FinSi
	
	Si nota2 >= 4 Entonces
		aprobadoreprobado2 = "Aprobado :D";
		contadorAprobado = contadorAprobado + 1;
	SiNo Si nota2 < 4 Entonces
			aprobadoreprobado2 = "Reprobado :(";
			contadorReprobado = contadorReprobado + 1;
		FinSi
	FinSi
	
	Si nota3 >= 4 Entonces
		aprobadoreprobado3 = "Aprobado :D";
		contadorAprobado = contadorAprobado + 1;
	SiNo Si nota3 < 4 Entonces
			aprobadoreprobado3 = "Reprobado :(";
			contadorReprobado = contadorReprobado + 1;
		FinSi
	FinSi
	
	Si nota4 >= 4 Entonces
		aprobadoreprobado4 = "Aprobado :D";
		contadorAprobado = contadorAprobado + 1;
	SiNo Si nota4 < 4 Entonces
			aprobadoreprobado4 = "Reprobado :(";
			contadorReprobado = contadorReprobado + 1;
		FinSi
		
	FinSi
	// ----------------- CALCULOS ----------------- //
	
	
	// ____ OPCIONES ____ //
	Si opc_menu == 1 Entonces
		Escribir "Seleccionaste Mostrar promedio ponderado";
		Escribir "";
		
		ponderado_final = nota1 * pond1 + nota2 * pond2 + nota3 * pond3 + nota4 * pond4;
		
		Escribir "Tu promedio ponderado es: ", ponderado_final;
		
		
	SiNo Si opc_menu == 2 Entonces
			Escribir "Seleccionaste Mostrar cantidad de aprobadas";
			Escribir "";
			Escribir "Nota1 = ", nota1, " ---> ", aprobadoreprobado1;
			Escribir "Nota2 = ", nota2, " ---> ", aprobadoreprobado2;
			Escribir "Nota3 = ", nota3, " ---> ", aprobadoreprobado3;
			Escribir "Nota4 = ", nota4, " ---> ", aprobadoreprobado4;
			Escribir "";
			Escribir "Cantidad de notas aprobadas son : ", contadorAprobado;
			
			
		SiNo Si opc_menu == 3 Entonces
				Escribir "Mostrar cantidad de reprobadas";
				Escribir "";
				Escribir "Nota1 = ", nota1, " ---> ", aprobadoreprobado1;
				Escribir "Nota2 = ", nota2, " ---> ", aprobadoreprobado2;
				Escribir "Nota3 = ", nota3, " ---> ", aprobadoreprobado3;
				Escribir "Nota4 = ", nota4, " ---> ", aprobadoreprobado4;
				Escribir "";
				Escribir "Cantidad de notas reprobadas son : ", contadorReprobado;
				
				
			SiNo Si opc_menu == 4 Entonces
					Limpiar Pantalla;
					Escribir "Adiós";
				FinSi
			FinSi
		FinSi
	FinSi
	
	

	
	
	
	
	
FinProceso
