Proceso corredor_obstaculos
	
	// La unica variable será la respuesta del corredor (respuesta_de_corredor) y se define como caracter, iguamente podría ser una variable logica
	Definir respuesta_de_corredor como caracter;
	
	// COMIENZA LA CARRERA: 
	// Se le pregunta al corredor por el primer obstaculo. La respuesta debe ser "si" o "no", de lo contrario no avanza el programa y se repite la pregunta
	Escribir "¡Comienza la carrera!";
	Repetir
		Escribir "Corredor, ¿has encontrado una valla? (si/no): ";
		Leer respuesta_de_corredor;
		Si respuesta_de_corredor == "SI" o respuesta_de_corredor == "Si" o respuesta_de_corredor == "si" o respuesta_de_corredor == "sI" Entonces
			Limpiar Pantalla;
			Escribir "SALTA LA VALLA!";
			Esperar 1 Segundos;
			SiNO Si respuesta_de_corredor = "NO" o respuesta_de_corredor == "No" o respuesta_de_corredor == "no" o respuesta_de_corredor == "nO" Entonces
				Limpiar Pantalla;	
				Escribir "Continua corriendo!...";
				Esperar 1 Segundos;
				SiNo Si respuesta_de_corredor <> "SI" o respuesta_de_corredor <> "Si" o respuesta_de_corredor <> "si" o respuesta_de_corredor <> "sI" o respuesta_de_corredor <> "NO" o respuesta_de_corredor <> "No" o respuesta_de_corredor <> "no" o respuesta_de_corredor <> "nO" Entonces
					Limpiar Pantalla;
					Escribir "Porfavor responde si o no, corredor!...";
					Esperar 1 Segundos;
					Limpiar Pantalla;
				FinSi
			FinSi
		FinSi
	Hasta Que respuesta_de_corredor == "SI" o respuesta_de_corredor == "Si" o respuesta_de_corredor == "si" o respuesta_de_corredor == "sI" o respuesta_de_corredor = "NO" o respuesta_de_corredor == "No" o respuesta_de_corredor == "no" o respuesta_de_corredor == "nO"
	
	// Se le pregunta al corredor por el segundo obstaculo. La respuesta debe ser "si" o "no", de lo contrario no avanza el programa y se repite la pregunta
	
	Limpiar Pantalla;
	Repetir
		Escribir "Corredor, ¿has encontrado un tunel? (si/no) ";
		Leer respuesta_de_corredor;
		Si respuesta_de_corredor == "SI" o respuesta_de_corredor == "Si" o respuesta_de_corredor == "si" o respuesta_de_corredor == "sI" Entonces
			Limpiar Pantalla;
			Escribir "Atravieza el tunel!";
			Esperar 1 Segundos;
			SiNO Si respuesta_de_corredor = "NO" o respuesta_de_corredor == "No" o respuesta_de_corredor == "no" o respuesta_de_corredor == "nO" Entonces
				Limpiar Pantalla;	
				Escribir "Continua corriendo!...";
				Esperar 1 Segundos;
				SiNo Si respuesta_de_corredor <> "SI" o respuesta_de_corredor <> "Si" o respuesta_de_corredor <> "si" o respuesta_de_corredor <> "sI" o respuesta_de_corredor <> "NO" o respuesta_de_corredor <> "No" o respuesta_de_corredor <> "no" o respuesta_de_corredor <> "nO" Entonces
					Limpiar Pantalla;	
					Escribir "Porfavor responde si o no, corredor!...";
					Esperar 1 Segundos;
					Limpiar Pantalla;
				FinSi
			FinSi
		FinSi
	Hasta Que respuesta_de_corredor == "SI" o respuesta_de_corredor == "Si" o respuesta_de_corredor == "si" o respuesta_de_corredor == "sI" o respuesta_de_corredor = "NO" o respuesta_de_corredor == "No" o respuesta_de_corredor == "no" o respuesta_de_corredor == "nO"
	
	// Se le pregunta al corredor por el tercer obstaculo. La respuesta debe ser "si" o "no", de lo contrario no avanza el programa y se repite la pregunta
	
	Limpiar Pantalla;
	Repetir
		Escribir "Corredor, ¿Has encontrado una laguna? (si/no): ";
		Leer respuesta_de_corredor;
		Si respuesta_de_corredor == "SI" o respuesta_de_corredor == "Si" o respuesta_de_corredor == "si" o respuesta_de_corredor == "sI" Entonces
			Limpiar Pantalla;
			Escribir "Empieza a nadar corredor. Si te cansas y te devuelves perderas la carrera";
			Esperar 1 Segundos;
			Escribir "...(El corredor se cansa y se devuelve)...";
			Esperar 1 Segundos;
			Escribir "Has perdido la carrera, corredor...";
			SiNO Si respuesta_de_corredor = "NO" o respuesta_de_corredor == "No" o respuesta_de_corredor == "no" o respuesta_de_corredor == "nO" Entonces
				Limpiar Pantalla;
				Escribir "Si continuas corriendo ganaras...";
				Esperar 1 Segundos;
				Escribir "Felicitaciones corredor, Has llegado a la meta con exito!";
				SiNo Si respuesta_de_corredor <> "SI" o respuesta_de_corredor <> "Si" o respuesta_de_corredor <> "si" o respuesta_de_corredor <> "sI" o respuesta_de_corredor <> "NO" o respuesta_de_corredor <> "No" o respuesta_de_corredor <> "no" o respuesta_de_corredor <> "nO" Entonces
					Limpiar Pantalla;
					Escribir "Porfavor responde si o no, corredor!...";
					Esperar 1 Segundos;
					Limpiar Pantalla;
				FinSi
			FinSi
		FinSi
	Hasta Que respuesta_de_corredor == "SI" o respuesta_de_corredor == "Si" o respuesta_de_corredor == "si" o respuesta_de_corredor == "sI" o respuesta_de_corredor = "NO" o respuesta_de_corredor == "No" o respuesta_de_corredor == "no" o respuesta_de_corredor == "nO"
	
	Escribir "FIN DEL PROGRAMA";
	
FinProceso
