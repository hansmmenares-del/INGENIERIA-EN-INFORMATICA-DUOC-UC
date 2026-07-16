Proceso programa_inventario
	Definir opc_root, accion_invalida, accion_valida, slot_seleccionado, volver_a_main, cantidad_producto1, cantidad_producto2, cantidad_producto3, search_by_NameOrSlot, repetir_menu2, opc_menu3, ventas Como Entero;
	Definir nombre_producto1, nombre_producto2, nombre_producto3, xxxxxx Como Cadena;
	Limpiar Pantalla;
	accion_invalida <- 0;
	accion_valida <- 0;
	cantidad_producto1 <- 0;
	cantidad_producto2 <- 0;
	cantidad_producto3 <- 0;
	search_by_NameOrSlot <- 0;
	nombre_producto1 <- 'EMPTY_NAME';
	nombre_producto2 <- 'EMPTY_NAME';
	nombre_producto3 <- 'EMPTY_NAME';
	xxxxxx <- 'xxxxxx';
	opc_menu3 <- 0;
	Repetir
		// Main Menu
		Escribir '-------- MENU --------';
		Escribir ' (1) Registrar producto';
		Escribir ' (2) Cambiar stock de producto en inventario'; // Listo
		Escribir ' (3) Proceso de ventas';
		Escribir ' (4) Mostrar estado actual del Inventario'; // Listo
		Escribir ' (5) Reporte de ventas';
		Escribir ' (6) Salir del programa'; // Listo
		Escribir ' (7) Logs'; // Listo
		Leer opc_root; // Listo
		// opc_root invalido / opc_root valido //
		Si opc_root<1 O opc_root>7 Entonces
			Escribir 'Opción inválida!';
			accion_invalida <- accion_invalida+1;
			Esperar 1 Segundos;
			Limpiar Pantalla;
		SiNo
			Si opc_root==1 O opc_root==2 O opc_root==3 O opc_root==4 O opc_root==5 O opc_root==7 Entonces
				accion_valida <- accion_valida+1;
			FinSi
		FinSi
		// Registro de productos
		Si opc_root==1 Entonces
			Repetir
				Limpiar Pantalla;
				Escribir 'Vamos a registrar tus productos!';
				Esperar 1 Segundos;
				Limpiar Pantalla;
				Escribir 'Solo se pueden registrar 3 productos (3 Slots)';
				Escribir '';
				Escribir 'Selecciona el número del slot para registrar un producto: ';
				Escribir '';
				Escribir 'Slot 1';
				Escribir 'Slot 2';
				Escribir 'Slot 3';
				Leer slot_seleccionado;
				Limpiar Pantalla;
				// Accion invalida en menu 1 seleccion de slot
				Si slot_seleccionado<1 O slot_seleccionado>3 Entonces
					Escribir 'Slot inválido!';
					accion_invalida <- accion_invalida+1;
				SiNo
					Si slot_seleccionado==1 O slot_seleccionado==2 O slot_seleccionado==3 Entonces
						accion_valida <- accion_valida+1;
					FinSi
				FinSi
			Hasta Que slot_seleccionado>=1 Y slot_seleccionado<=3
			// Succsesful slot selection
			Si slot_seleccionado==1 Entonces
				Escribir 'Has selccionado el Slot 1';
			SiNo
				Si slot_seleccionado==2 Entonces
					Escribir 'Has selccionado el Slot 2';
				SiNo
					Si slot_seleccionado==3 Entonces
						Escribir 'Has selccionado el Slot 3';
					FinSi
				FinSi
			FinSi
			Esperar 1.5 Segundos;
			Limpiar Pantalla;
			// Naming Slot 1, 2 or 3. Asking to main or reName
			Si slot_seleccionado==1 Entonces
				Escribir 'Ingresa el nombre del producto para el Slot1', slot_seleccionado, ': ';
				Leer nombre_producto1;
				Escribir 'El nombre de Slot1 que asignaste al producto es: ', nombre_producto1;
			SiNo
				Si slot_seleccionado==2 Entonces
					Escribir 'Ingresa el nombre del producto para el Slot2', slot_seleccionado, ': ';
					Leer nombre_producto2;
					Escribir 'El nombre de Slot2 que asignaste al producto es: ', nombre_producto2;
				SiNo
					Si slot_seleccionado==3 Entonces
						Escribir 'Ingresa el nombre del producto para el Slot3', slot_seleccionado, ': ';
						Leer nombre_producto3;
						Escribir 'El nombre de Slot3 que asignaste al producto es: ', nombre_producto3;
					FinSi
				FinSi
			FinSi
			Limpiar Pantalla;
			Escribir 'El nombre de Slot 1 es: ', nombre_producto1;
			Escribir 'El nombre de Slot 2 es: ', nombre_producto2;
			Escribir 'El nombre de Slot 3 es: ', nombre_producto3;
			Escribir '';
			Escribir 'Presiona cualquier tecla para volver al menu principal...';
			Esperar Tecla;
			Limpiar Pantalla;
		FinSi
		// Stock number change
		Si opc_root==2 Entonces
			Repetir
				xxxxxx <- 'xxxxxx';
				Limpiar Pantalla;
				Escribir '--- Cambio de STOCK--- ';
				Escribir '';
				Escribir '(1) Encontrar producto por nombre';
				Escribir '(2) Encontrar producto por numero de slot';
				Leer search_by_NameOrSlot;
				Si search_by_NameOrSlot<1 Y search_by_NameOrSlot>2 Entonces
					Escribir 'Opción inválida!';
					accion_invalida <- accion_invalida+1;
				SiNo
					Si search_by_NameOrSlot>=1 Y search_by_NameOrSlot<=2 Entonces
						accion_valida <- accion_valida+1;
					FinSi
				FinSi
				Si search_by_NameOrSlot==1 Entonces
					Escribir 'Escribe el nombre del producto: ';
					Leer xxxxxx;
				FinSi
				Si xxxxxx==nombre_producto1 Entonces
					Escribir 'Cambiaras el STOCK de : ', nombre_producto1;
					Escribir '';
					Escribir 'El Stock actual de ', nombre_producto1, ' es: ', cantidad_producto1;
					Escribir '';
					Escribir 'Ingresa la cantidad de STOCK: ';
					Leer cantidad_producto1;
					Limpiar Pantalla;
					Escribir 'Has cambiado el STOCK de ', nombre_producto1, ' con éxito!';
					Escribir 'Se ha actualizado a : ', cantidad_producto1, ' unidades';
					Esperar 2 Segundos;
					Limpiar Pantalla;
				SiNo
					Si xxxxxx==nombre_producto2 Entonces
						Escribir 'Cambiaras el STOCK de : ', nombre_producto2;
						Escribir '';
						Escribir 'El Stock actual de ', nombre_producto2, ' es: ', cantidad_producto2;
						Escribir '';
						Escribir 'Ingresa la cantidad de STOCK: ';
						Leer cantidad_producto2;
						Limpiar Pantalla;
						Escribir 'Has cambiado el STOCK de ', nombre_producto2, ' con éxito!';
						Escribir 'Se ha actualizado a : ', cantidad_producto2, ' unidades';
						Esperar 2 Segundos;
						Limpiar Pantalla;
					SiNo
						Si xxxxxx==nombre_producto3 Entonces
							Escribir 'Cambiaras el STOCK de : ', nombre_producto3;
							Escribir '';
							Escribir 'El Stock actual de ', nombre_producto3, ' es: ', cantidad_producto3;
							Escribir '';
							Escribir 'Ingresa la cantidad de STOCK: ';
							Leer cantidad_producto3;
							Limpiar Pantalla;
							Escribir 'Has cambiado el STOCK de ', nombre_producto3, ' con éxito!';
							Escribir 'Se ha actualizado a : ', cantidad_producto3, ' unidades';
							Esperar 2 Segundos;
							Limpiar Pantalla;
						FinSi
					FinSi
				FinSi
				Si search_by_NameOrSlot==2 Entonces
					Escribir 'Escribe el numero de slot: ';
					Leer slot_seleccionado;
					Si slot_seleccionado==1 Entonces
						Escribir 'Cambiaras el STOCK de : ', nombre_producto1;
						Escribir '';
						Escribir 'El Stock actual de ', nombre_producto1, ' es: ', cantidad_producto1;
						Escribir '';
						Escribir 'Ingresa la cantidad de STOCK: ';
						Leer cantidad_producto1;
						Limpiar Pantalla;
						Escribir 'Has cambiado el STOCK de ', nombre_producto1, ' con éxito!';
						Escribir 'Se ha actualizado a : ', cantidad_producto1, ' unidades';
						Esperar 2 Segundos;
						Limpiar Pantalla;
					SiNo
						Si slot_seleccionado==2 Entonces
							Escribir 'Cambiaras el STOCK de : ', nombre_producto2;
							Escribir '';
							Escribir 'El Stock actual de ', nombre_producto2, ' es: ', cantidad_producto2;
							Escribir '';
							Escribir 'Ingresa la cantidad de STOCK: ';
							Leer cantidad_producto2;
							Limpiar Pantalla;
							Escribir 'Has cambiado el STOCK de ', nombre_producto2, ' con éxito!';
							Escribir 'Se ha actualizado a : ', cantidad_producto2, ' unidades';
							Esperar 2 Segundos;
							Limpiar Pantalla;
						SiNo
							Si slot_seleccionado==3 Entonces
								Escribir 'Cambiaras el STOCK de : ', nombre_producto3;
								Escribir '';
								Escribir 'El Stock actual de ', nombre_producto3, ' es: ', cantidad_producto3;
								Escribir '';
								Escribir 'Ingresa la cantidad de STOCK: ';
								Leer cantidad_producto3;
								Limpiar Pantalla;
								Escribir 'Has cambiado el STOCK de ', nombre_producto3, ' con éxito!';
								Escribir 'Se ha actualizado a : ', cantidad_producto3, ' unidades';
								Esperar 2 Segundos;
								Limpiar Pantalla;
							FinSi
						FinSi
					FinSi
				FinSi
				Escribir '';
				Escribir '(0) Cambiar otro STOCK';
				Escribir '(1) Volver al Menu principal';
				Leer repetir_menu2;
			Hasta Que repetir_menu2<>0
		FinSi
		Limpiar Pantalla;
		// Proceso de ventas
		Si opc_root==3 Entonces
			Repetir
				Repetir
					Si opc_menu3<>3 Entonces
						Limpiar Pantalla;
					FinSi
					Escribir "--------- Proceso de ventas ---------";
					Escribir "";
					Escribir "Aquí podrás seleccionar un producto para venderlo";
					Escribir "Los productos vendidos se descontarán automaticamente del Stock";
					Escribir "";
					Escribir "(1) Buscar producto por nombre";
					Escribir "(2) Buscar producto por Slot";
					Escribir "(3) Recordar nombres, Slots y STOCK de productos";
					Escribir "(4) Volver al menu principal";
					Escribir "";
					Leer opc_menu3;
					Si opc_menu3<1 Entonces
						Escribir "Opción inválida!";
						accion_invalida=accion_invalida+1;
						Esperar 1 Segundos;
					SiNo Si opc_menu3>4 Entonces
							Escribir "Opción inválida!";
							accion_invalida=accion_invalida+1;
							Esperar 1 Segundos;
						FinSi
					FinSi
				Hasta Que opc_menu3==1 o opc_menu3==2 o opc_menu3==3 o opc_menu3==4
				Si opc_menu3==1 Entonces
					Escribir "Ingresa el nombre del producto: ";
					Leer xxxxxx;
					Limpiar Pantalla;
					Si xxxxxx==nombre_producto1 Entonces
						Escribir "Has seleccionado el producto: ", nombre_producto1;
						Escribir "¿Cuántas unidades deseas comprar?";
						Leer ventas;
						cantidad_producto1 = cantidad_producto1-ventas;
						Si cantidad_producto1<=0 Entonces
							cantidad_producto1 = cantidad_producto1+ventas;
							Limpiar Pantalla;
							Escribir "No hay suficientes unidades disponibles, lo siento.";
							Esperar 2 Segundos;
							Limpiar Pantalla;
							Escribir "-----------------------------";
							Escribir "";
							Escribir "¡¡¡ AVISO URGENTE !!!";
							Escribir "REPONER STOCK DE: ", nombre_producto1;
							Escribir "";
							Escribir "-----------------------------";
							Escribir "";
							Escribir "";
							Escribir "";
							Escribir "Para volver al menu principal presiona cualquier tecla";
							Esperar Tecla;
							Limpiar Pantalla;
						FinSi
						Si cantidad_producto1>=0 y cantidad_producto2>=0 y cantidad_productos>=0 Entonces
							Escribir "¡Venta exitosa!";
							Escribir "Del Stock se han descontado ", ventas, " Unidades";
						FinSi
					SiNo Si xxxxxx==nombre_producto2 Entonces
							Escribir "Has seleccionado el producto: ", nombre_producto2;
							Escribir "¿Cuántas unidades deseas comprar?";
							Leer ventas;
							cantidad_producto2 = cantidad_producto2-ventas;
							Si cantidad_producto2<=0 Entonces
								cantidad_producto2 = cantidad_producto2+ventas;
								Limpiar Pantalla;
								Escribir "No hay suficientes unidades disponibles, lo siento.";
								Esperar 2 Segundos;
								Limpiar Pantalla;
								Escribir "-----------------------------";
								Escribir "";
								Escribir "¡¡¡ AVISO URGENTE !!!";
								Escribir "REPONER STOCK DE: ", nombre_producto2;
								Escribir "";
								Escribir "-----------------------------";
								Escribir "";
								Escribir "";
								Escribir "";
								Escribir "Para volver al menu principal presiona cualquier tecla";
								Esperar Tecla;
								Limpiar Pantalla;
							FinSi
							Si cantidad_producto1>=0 y cantidad_producto2>=0 y cantidad_producto3>=0 Entonces
								Escribir "¡Venta exitosa!";
								Escribir "Del Stock se han descontado ", ventas, " Unidades";
							FinSi
						SiNo Si xxxxxx==nombre_producto3 Entonces
								Escribir "Has seleccionado el producto: ", nombre_producto3;
								Escribir "¿Cuántas unidades deseas comprar?";
								Leer ventas;
								cantidad_producto3 = cantidad_producto3-ventas;
								Si cantidad_producto3<=0 Entonces
									cantidad_producto3 = cantidad_producto3+ventas;
									Limpiar Pantalla;
									Escribir "No hay suficientes unidades disponibles, lo siento.";
									Esperar 2 Segundos;
									Limpiar Pantalla;
									Escribir "-----------------------------";
									Escribir "";
									Escribir "¡¡¡ AVISO URGENTE !!!";
									Escribir "REPONER STOCK DE: ", nombre_producto3;
									Escribir "";
									Escribir "-----------------------------";
									Escribir "";
									Escribir "";
									Escribir "";
									Escribir "Para volver al menu principal presiona cualquier tecla";
									Esperar Tecla;
									Limpiar Pantalla;
								FinSi
								Si cantidad_producto1>=0 y cantidad_producto2>=0 y cantidad_producto3>=0 Entonces
									Escribir "¡Venta exitosa!";
									Escribir "Del Stock se han descontado ", ventas, " Unidades";
								FinSi
							FinSi
						FinSi
					FinSi
				SiNo Si opc_menu3==2 Entonces
						Repetir
							Escribir "Ingresa el numero de Slot: ";
							Leer slot_seleccionado;
							Si slot_seleccionado==1 Entonces
								Escribir "Has seleccionado el producto: ", nombre_producto1;
								Escribir "¿Cuántas unidades deseas comprar?";
								Leer ventas;
								cantidad_producto1 = cantidad_producto1-ventas;
								Si cantidad_producto1<=0 Entonces
									cantidad_producto1 = cantidad_producto1+ventas;
									Limpiar Pantalla;
									Escribir "No hay suficientes unidades disponibles, lo siento.";
									Esperar 2 Segundos;
									Limpiar Pantalla;
									Escribir "-----------------------------";
									Escribir "";
									Escribir "¡¡¡ AVISO URGENTE !!!";
									Escribir "REPONER STOCK DE: ", nombre_producto1;
									Escribir "";
									Escribir "-----------------------------";
									Escribir "";
									Escribir "";
									Escribir "";
									Escribir "Para volver al menu principal presiona cualquier tecla";
									Esperar Tecla;
									Limpiar Pantalla;
								FinSi
								Si cantidad_producto1>=0 y cantidad_producto2>=0 y cantidad_producto3>=0 Entonces
									Escribir "¡Venta exitosa!";
									Escribir "Del Stock se han descontado ", ventas, " Unidades";
								FinSi
							SiNo Si slot_seleccionado==2 Entonces
									Escribir "Has seleccionado el producto: ", nombre_producto2;
									Escribir "¿Cuántas unidades deseas comprar?";
									Leer ventas;
									cantidad_producto2 = cantidad_producto2-ventas;
									Si cantidad_producto2<=0 Entonces
										cantidad_producto2 = cantidad_producto2+ventas;
										Limpiar Pantalla;
										Escribir "No hay suficientes unidades disponibles, lo siento.";
										Esperar 2 Segundos;
										Limpiar Pantalla;
										Escribir "-----------------------------";
										Escribir "";
										Escribir "¡¡¡ AVISO URGENTE !!!";
										Escribir "REPONER STOCK DE: ", nombre_producto2;
										Escribir "";
										Escribir "-----------------------------";
										Escribir "";
										Escribir "";
										Escribir "";
										Escribir "Para volver al menu principal presiona cualquier tecla";
										Esperar Tecla;
										Limpiar Pantalla;
									FinSi
									Si cantidad_producto1>=0 y cantidad_producto2>=0 y cantidad_producto3>=0 Entonces
										Escribir "¡Venta exitosa!";
										Escribir "Del Stock se han descontado ", ventas, " Unidades";
									FinSi
								SiNo Si slot_seleccionado==3 Entonces
										Escribir "Has seleccionado el producto: ", nombre_producto3;
										Escribir "¿Cuántas unidades deseas comprar?";
										Leer ventas;
										cantidad_producto3 = cantidad_producto3-ventas;
										Si cantidad_producto3<=0 Entonces
											cantidad_producto3 = cantidad_producto3+ventas;
											Limpiar Pantalla;
											Escribir "No hay suficientes unidades disponibles, lo siento.";
											Esperar 2 Segundos;
											Limpiar Pantalla;
											Escribir "-----------------------------";
											Escribir "";
											Escribir "¡¡¡ AVISO URGENTE !!!";
											Escribir "REPONER STOCK DE: ", nombre_producto3;
											Escribir "";
											Escribir "-----------------------------";
											Escribir "";
											Escribir "";
											Escribir "";
											Escribir "Para volver al menu principal presiona cualquier tecla";
											Esperar Tecla;
											Limpiar Pantalla;
										FinSi
										Si cantidad_producto1>=0 y cantidad_producto2>=0 y cantidad_producto3>=0 Entonces
											Escribir "¡Venta exitosa!";
											Escribir "Del Stock se han descontado ", ventas, " Unidades";
										FinSi
									FinSi
								FinSi
							FinSi
							Si slot_seleccionado<1 Entonces
								accion_invalida=accion_invalida+1;
								Escribir "Opción inválida!";
							FinSi
							Si slot_seleccionado>3 Entonces
								accion_invalida=accion_invalida+1;
								Escribir "Opción inválida!";
							FinSi
						Hasta Que slot_seleccionado==1 o slot_seleccionado==2 o slot_seleccionado==3
					SiNo Si opc_menu3==3 Entonces
							Limpiar Pantalla;
							Escribir "";
							Escribir "Slot1: ", nombre_producto1, "    STOCK: ", cantidad_producto1;
							Escribir "Slot2: ", nombre_producto2, "    STOCK: ", cantidad_producto2;
							Escribir "Slot3: ", nombre_producto3, "    STOCK: ", cantidad_producto3;
							Escribir "";
						SiNo Si opc_menu3==4 Entonces
								Escribir "chao chao";
								Esperar 1 Segundos;
								Limpiar Pantalla;
							FinSi
						FinSi
					FinSi
				FinSi
			Hasta Que opc_menu3<>3
		FinSi
		// Mostrar estado actual del inventario
		Si opc_root==4 Entonces
			Limpiar Pantalla;
			Escribir '------- Estado del inventario -------';
			Escribir '';
			Escribir 'Stock de ', nombre_producto1, ' es: ', cantidad_producto1;
			Escribir '';
			Escribir 'Stock de ', nombre_producto2, ' es: ', cantidad_producto2;
			Escribir '';
			Escribir 'Stock de ', nombre_producto3, ' es: ', cantidad_producto3;
			Escribir '';
			Escribir 'Para volver al menu principal presiona cualquier tecla... ';
			Esperar Tecla;
			Limpiar Pantalla;
		FinSi
		Si opc_root==5 Entonces
			Limpiar Pantalla;
			Escribir "--------- Reporte de Ventas ---------";
			Escribir "
		FinSi
		// LOGS
		Si opc_root==7 Entonces
			Limpiar Pantalla;
			Escribir '---------------- Logs ----------------';
			Escribir '';
			Escribir 'Acciones válidas  : ', accion_valida;
			Escribir '';
			Escribir 'Acciones inválidas: ', accion_invalida;
			Escribir '';
			Escribir 'Para volver al menu principal presiona cualquier tecla...';
			Esperar Tecla;
			Limpiar Pantalla;
		FinSi
	Hasta Que opc_root==6
	Si opc_root==6 Entonces
		Escribir 'Hasta nunca loser...';
	FinSi
FinProceso
