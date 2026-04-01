salir = True
i = 0
while True:
    print(f"iteracion: {i}")
    i += 1
    if input("ir a la proxima iteracion? (s/n): ") == 's':
        #salir = False
        #break
        continue
    print(f"final de la iteracion: {i-1}")

#break solo finaliza el while
#exit() finaliza todo el programa