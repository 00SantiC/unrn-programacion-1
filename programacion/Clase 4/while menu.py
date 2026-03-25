opcion = ""

precio_total = 0

metodo_pago = ""
metodo_pago_valido = False

print("selecciona comida para llevar menu:" \
      "\npizza $25" \
      "\nhamburguesa $18" \
      "\npapas fritas $10" \
      "\nensalada $5" \
      "\npara finalizar tu pedido escribi 'terminar pedido'\n")

while opcion != "terminar pedido":
    opcion = input("escribi la comida que quieras agregar al pedido: ").lower()
    if opcion == "pizza":
        precio_total += 25
        print("agregaste pizza al pedido")
    elif opcion == "hamburguesa":
        precio_total += 18
        print("agregaste hamburguesa al pedido")
    elif opcion == "papas fritas":
        precio_total += 10
        print("agregaste papas fritas al pedido")
    elif opcion == "ensalada":
        precio_total += 5
        print("agregaste ensalada al pedido")
    elif opcion == "terminar pedido":
        print("\nterminaste tu pedido\n")
        while precio_total > 0 and (metodo_pago == "" or metodo_pago_valido == False):
            metodo_pago = input("como desea abonar? escriba 'efectivo', 'tarjeta' o 'transferencia': ")

            if metodo_pago == "efectivo":
                print("elegiste pagar con efectivo")
                metodo_pago_valido = True
            elif metodo_pago == "tarjeta":
                print("elegiste pagar con tarjeta")
                metodo_pago_valido = True
            elif metodo_pago == "transferencia":
                print("elegiste pagar con transferencia")
                metodo_pago_valido = True
            else:
                print("\nopcion no valida, por favor selecciona un metodo de pago valido\n")
                metodo_pago = ""
                metodo_pago_valido = False
    else:
        print("\nopcion no valida, por favor selecciona una comida del menu o escribi 'terminar pedido' para finalizar\n")
        precio_total = 0
    

if precio_total > 0 and opcion == "terminar pedido" and metodo_pago_valido == True:
    input(f"\npedido finalizado, gracias por elegirnos. el total es: ${precio_total} a abonar con {metodo_pago}")
else:
    input()