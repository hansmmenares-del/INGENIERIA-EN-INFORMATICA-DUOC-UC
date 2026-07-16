Proceso PROMEDIODENOTAS
	
	Definir nota1, nota2, nota3, nota4 como Real;
	Definir contadorAprobado, contadorReprobado como Entero;
	Definir promedio_de_notas, suma_de_notas como Real;
	Definir opc_menu1, opc_menu2 como Entero;
	
	Escribir "___--- MENU ---___";
	Escribir "";
	Escribir "(1) Ingresar las notas";
	Escribir "(2) Salir del programa";
	Leer opc_menu1;
	
	Si opc_menu1 = 1 Entonces
		
		Escribir "Ingresa tu primera nota:";
		Leer nota1;
		Escribir "Ingresa tu segunda nota:";
		Leer nota2;
		Escribir "Ingresa tu tercera nota:";
		Leer nota3;
		Escribir "Ingresa tu cuarta nota:";
		Leer nota4;
		
		promedio_de_notas = (nota1 + nota2 + nota3 + nota4)/4;
		suma_de_notas = nota1 + nota2 + nota3 + nota4;
		
		Leer opc_menu2;
		Si opc_menu2 = 1 Entonces
			Escribir "Mostrar suma de notas";
		SiNo Si opc_menu2 = 2 Entonces
				Escribir "";
			SiNo Si opc_menu2 = 3 Entonces
					Escribir "";
				SiNo Si opc_menu2 = 4 Entonces
						Escribir "";
					FinSi
				FinSi
			FinSi
		FinSi
		
		
	SiNo Si opc_menu1 = 2 Entonces
			Escribir "XAO XAO";
		FinSi
	FinSi
	
	
	
	
	
	
	
FinProceso
