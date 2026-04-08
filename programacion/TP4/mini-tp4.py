#mini TP 4: funciones y modulos

#1)
# def saludar(nombre):
#     print(f"hola {nombre} bienvenido!")


# saludar(input("ingresa tu nombre: "))

#2)
# def sumar(numero1, numero2):
#     return numero1 + numero2

# print("Sumar 2 numeros")

# numero1 = int(input("ingrese el primer numero: "))
# numero2 = int(input("ingrese el segundo numero: "))


# resultado = sumar(numero1, numero2)
# print("el resultado es: ", resultado)

#3)

# def es_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False

# numero = int(input("escribi un numero para saber si es par o no: "))

# if es_par(numero):
#     print(f"el numero {numero} es par")
# else:
#     print(f"el numero {numero} es inpar")

#4)

# def calcular_descuento(precio):
#     if precio > 10000:
#         precio -= (precio * 10)/100
#         #precio *= 0.9
#         return precio
#     else: 
#         return precio

# precio = int(input("escribi el precio, si es mayor que 10k se aplicara 10 porciento de descuento: "))
# print(f"el precio queda en: {calcular_descuento(precio)}$")

#5)

# def obtener_estado(nota):
#     if nota >= 8:
#         return "promociona"
#     elif nota < 8 and nota > 6:
#         return "aprueba"
#     elif nota < 6:
#         return "desaprueba"

# nota = int(input("escribi una nota para ver el estado: "))
# print(obtener_estado(nota))

#6)
# import conversores

# print(conversores.metros_a_centimetros(3))
# print(conversores.centimetros_a_milimetros(5))
# print(conversores.horas_a_minutos(7))

#7)
# import mensajes

# nombre = input("escribi tu nombre: ")
# print(mensajes.despedir(nombre))

#8)

# def pedir_comida():
#     comida = ""
#     while comida == "":
#         comida = input("ingresa tu pedido: ")
#     return comida


# def obtener_precio(comida):
#     if comida == "hamburguesa":
#         precio = 100
#     elif comida == "milanesa":
#         precio = 125
#     elif comida == "pizza":
#         precio = 140
#     else:
#         precio = 0

#     if precio > 0:
#         print(f"comida: {comida} - precio: {precio}$")
#     else:
#         print("comida no valida")
    

# obtener_precio(pedir_comida())