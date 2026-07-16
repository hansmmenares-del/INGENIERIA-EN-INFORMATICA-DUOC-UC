Proceso Estacion_de_servicio
	
	Definir nivelBencina, tipoBencina como Entero;
	
	Escribir "---  ¡Bienvenido a la Estación de Servicio!  ---";
	
	Escribir "--- ¿Cuántos litros de bencina tiene tu auto? ---";
	
	Escribir "Ingresa la cantidad de litros: ";
	
	Leer nivelBencina;
	Si nivelBencina < 10 Entonces
		
		Escribir "Tu nivel de bencina está bajo...";
		Escribir "¡Te sugerimos cargar bencina!";
		Escribir "Selecciona un tipo de bencina (1, 2 o 3): ";
		Escribir " (1) 93 octanos ";
		Escribir " (2) 95 octanos ";
		Escribir " (3) 97 octanos ";
		
		Leer tipoBencina;
		
		Si tipoBencina == 1 Entonces
			Escribir "Estas cargando bencina 93 octanos Regular";
			Esperar 1 Segundos;
			Escribir "Ahora tu tanque está lleno";
			SiNo Si tipoBencina == 2 Entonces
				Escribir "Estas cargando bencina 95 octanos Plus";
				Esperar 1 Segundos;
				Escribir "Ahora tu tanque está lleno";
				SiNo Si tipoBencina == 3 Entonces
					Escribir "Estas cargando bencina 97 octanos Premium";
					Esperar 1 Segundos;
					Escribir "Ahora tu tanque está lleno";
					SiNo Si tipoBencina <> 1 y tipoBencina <> 2 y tipoBencina <> 3 Entonces
						Escribir "Opcion no valida, se cerrará el programa";
					FinSi
				FinSi
			FinSi
		FinSi
		SiNo Si nivelBencina >= 10 Entonces
			Escribir "No es necesario cargar más bencina";
		FinSi
	FinSi
	Escribir "¡Vuelva Pronto!";
FinProceso
