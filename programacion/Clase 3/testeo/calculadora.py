print("Bienvenido a la calculadora 1.0. Debe ingresar 2 numeros, luego la operación que desea hacer con ellos escribiendo sumar o s")
while True:    
    numero1 = float()
    numero2 = float()

    cuenta = str()

    operacion = str()
    respuesta = str()

    paso = int(1)
 
    if paso == 1:
        numero1 = input("Escriba el primer número: ")
        paso = paso + 1

    if paso == 2:
        numero2 = input("Escriba el segundo número: ")
        paso = paso + 1

    if paso == 3:
        print("Que operación quiere hacer?(sumar, restar, multiplicar, dividir)(s,r,m,d):")
        operacion = input(operacion)
        paso = paso + 1

    if paso == 4:
        if operacion == "sumar" or operacion == "s":
            cuenta = int(numero1) + int(numero2)
        elif operacion == "restar" or operacion == "r":
            cuenta = int(numero1) - int(numero2)
        elif operacion == "multiplicar" or operacion == "m":
            cuenta = int(numero1) * int(numero2)
        elif operacion == "dividir" or operacion == "d":
            cuenta = int(numero1) / int(numero2)
        else: 
            print("Operación no válida")
        print("El resultado es: " + str(cuenta))
        paso = paso + 1

    if paso == 5:
        print("Desea hacer otra operación? (s/n):")
        respuesta = input(respuesta)
        if respuesta == "s":
            paso = 1   
        else:  
            print("Gracias por usar la calculadora")
            break

        
input()