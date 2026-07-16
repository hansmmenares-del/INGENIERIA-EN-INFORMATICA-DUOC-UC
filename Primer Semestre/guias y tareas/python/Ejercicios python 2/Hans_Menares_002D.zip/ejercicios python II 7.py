def descuento_compra():
    monto=float(input("Ingresa el monto:\n"))
    if monto>100:
        preciofinal_con_descuento=monto-((monto*10)/100)
        print(f"Descuento de {preciofinal_con_descuento}")
    else:
        print(f"No hubo descuento. Precio final {monto}")
descuento_compra()