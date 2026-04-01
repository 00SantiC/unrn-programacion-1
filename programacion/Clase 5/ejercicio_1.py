def pedir_comida():
    comida = ""
    while comida == "":
        comida = input("ingresa tu pedido: ")
    return comida


def obtener_precio(comida):
    if comida == "hamburguesa":
        print("hamburguesa 100$")
        return 100
    elif comida == "milanesa":
        print("milanesa 125$")
        return 125
    elif comida == "pizza":
        print("pizza 140$")
        return 140
    print("comida no valida")
    return 0

# print(f"Comida: {comida} - Precio: {precio}$")
    

obtener_precio(pedir_comida())