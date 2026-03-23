while True:

    documento = str()
    tienedocumento = bool()
    edad = int()
    mayor = bool()

    edad = input("Escriba su edad: ")

    if edad < "18":
        input("No puede entrar")
        break
        

    documento = input("¿Tiene documento? (s/n): ")
    if documento == "s":
        tienedocumento = True
    else:
        tienedocumento = False
        input("No puede entrar")
        break

    if edad >= "18" and tienedocumento == True:
        print("Puede entrar")
    else:
        print("No puede entrar")


