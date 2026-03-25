# Definir una variable mensaje con el valor "Hola mundo!" y mostrarla por pantalla.
# Definir las variables nombre y apellido y mostrar el mensaje: "Bienvenido [nombre] [apellido] al mundo Python".
# Crear un programa donde se defina una variable de cada uno de los siguientes tipos: str, int y float. Utilizar type() para imprimir, junto con su valor, el tipo de cada variable.
# Crear un programa donde se asigne un valor a una variable de tipo int y otra de tipo float, sumarlas y mostrar el resultado, indicando tambien el tipo de dato del resultado.
# Crear un programa que:
# Calcule cuantos meses viviste aproximadamente.
# Calcule tu edad dentro de 10 anios.
# Calcule el doble de tu altura.
# Imprima los resultados con mensajes descriptivos.
# Crear un programa que:
# Cree una variable saludo que diga: "Hola <tu nombre>".
# Cree otra variable que repita el saludo tres veces.
# Cuente cuantas letras tiene tu nombre usando len().

print("hola mundo!")

nombre = "santiago"
apellido = "c"

print(f"Bienvenido {nombre} {apellido} al mundo Python")

str_var = "pi"
int_var = 3
float_var = 3.14

print(f"valor: {str_var}, tipo: {type(str_var)}")
print(f"valor: {int_var}, tipo: {type(int_var)}")
print(f"valor: {float_var}, tipo: {type(float_var)}")


print("Sumar int y float")
entero = int(input("ingresar 1 numero entero: "))
flotante = float(input("ingresar un numero flotante: "))

suma = float(entero + flotante)

print(f"El resultado de la suma es: {suma} de tipo: {type(suma)}")

print("\nCalculadora de años a meses")
edad = int(input("ingresar tu edad: "))
meses = edad * 12
print(f"viviste aproximadamente {meses} meses")

print("\nCalculadora de edad dentro de 10 años")
edad_futura = edad + 10
print(f"tu edad dentro de 10 años sera: {edad_futura}")


print("ingresa tu altura:")
altura = float(input())
altura_doble = altura * 2
print(f"el doble de tu altura es: {altura_doble}")

for saludo in range(3):
    print(f"Hola {nombre}")
print(f"Tu nombre tiene {len(nombre)} letras")

input()


