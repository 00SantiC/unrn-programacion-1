test = "primer numero"
testt = "segundo numero"

numero1 = int()
numero2 = int()

paso = int(1)

if paso == 1:
    print(test)
    numero1 = input(numero1)
    paso = paso + 1

if paso == 2:
    print(testt)
    numero2 = input(numero2)
    paso = paso + 1

if paso == 3:
    cuenta = int(numero1) + int(numero2)
    print("la suma de los numeros es: " + str(cuenta))   
    paso = 3
    
input()