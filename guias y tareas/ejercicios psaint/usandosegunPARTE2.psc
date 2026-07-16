Proceso usandosegun
	
	Definir opc_root como Entero;
	Leer opc_root;
	Segun opc_root Hacer
		1:
			Definir cateto1, cateto2, hipoC como Real;
			Escribir "ingresa el valor del cateto1: ";
			Leer cateto1;
			Escribir "ingresa el valor del cateto2: ";
			Leer cateto2;
			Escribir "El valor de la hipotenusa es : ", raiz(cateto1+cateto2);
		2:
			Definir opc_sueldo como Entero;
			Definir sueldoBruto como Entero;
			Definir gratificacion como Real;
			Definir desuentoAFP como Real;
			Definir descuentoSalud como Real;
			Definir descuentoSegCesantia como Real;
			Definir impuestos como Real;
			Definir bonoTransporte como Entero;
			Definir sueldoLiq como Real;
			gratificacion = 0.25;
			desuentoAFP = 0.109;
			descuentoSalud = 0.07;
			descuentoSegCesantia = 0.003;
			impuestos = 0.03;
			bonoTransporte = 40000;
			Repetir
				Escribir "Ingresa tu sueldo bruto en pesos: ";
				Leer sueldoBruto;
				sueldoLiq = sueldoBruto + (sueldoBruto*gratificacion) - (sueldoBruto*desuentoAFP) - (sueldoBruto*descuentoSalud) - (sueldoBruto*descuentoSegCesantia) - (sueldoBruto*impuestos) + (sueldoBruto*bonoTransporte);
				Escribir "¿Qué deseas ver? Selecciona tu opción: ";
				Escribir "(1) Suledo bruto más gratificación: ";
				Escribir "(2) Monto total de desceuntos: ";
				Escribir "(3) Sueldo líquido resultante";
				Escribir "(4) Sueldo líquido anual en dólares, asumiendo dolar a $976.95): ";
				Escribir "(5) Ingresar otro monto bruto";
				Escribir "(6) Salir del programa";
				Leer opc_sueldo;
			Hasta Que opc_sueldo <> 5;
			Segun opc_sueldo Hacer
				1: Escribir "$", sueldoBrut+gratificacion;
				2: Escribir "$", sueldoBruto*desuentoAFP + sueldoBrut*descuentoSalud + sueldoBruto*descuentoSegCesantia + sueldoBruto*impuestos;
				3: Escribir "$", sueldoLiq;
				4: Escribir "$", (sueldoLiq*12)/976.95;
			FinSegun
			
		3:
			Definir uva_A, uva_B como Real;
			
			
		4:
			
		De Otro Modo:
			Escribir "Estupido";
	FinSegun
FinProceso
