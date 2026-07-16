Proceso lectordecodigos
	
	Definir cantidad_de_trabajos, i Como Entero;
	Definir lectura_usuario Como Entero;
	Definir total Como Entero;
	
	Definir precio_corona_sobre_implante, precio_emax, precio_provisorio Como Entero;
	
	precio_corona_sobre_implante = 10000;
	precio_emax = 20000;
	precio_provisorio = 12000;
	
	total = 0;
	
	Repetir
		Escribir "Cuantos trabajos desea ingresar? (maximo 5)";
		Leer cantidad_de_trabajos;
	Hasta Que cantidad_de_trabajos > 0 Y cantidad_de_trabajos <= 5
	
	Para i = 1 Hasta cantidad_de_trabajos Hacer
		
		Escribir "Ingrese el codigo del trabajo (0,1,2): ";
		Leer lectura_usuario;
		
		Segun lectura_usuario Hacer
			
			0:
				Escribir "Corona sobre implante: $", precio_corona_sobre_implante;
				total = total + precio_corona_sobre_implante;
				
			1:
				Escribir "Emax: $", precio_emax;
				total = total + precio_emax;
				
			2:
				Escribir "Provisorio: $", precio_provisorio;
				total = total + precio_provisorio;
				
			De Otro Modo:
				Escribir "Codigo invalido";
				
		FinSegun
		
	FinPara
	
	Escribir "El total es: $", total;
	
FinProceso
