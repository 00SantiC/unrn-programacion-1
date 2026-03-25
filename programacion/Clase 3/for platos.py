# for i in range(0,100):
#     i = int(i)
#     print(f"hola {i} veces")

# input()

platos = 7

juan = 0

pedro = 0

mateo = 0

for i in range(0,platos):
    if i == 1 or i == 4:
        input(f"juan lavo el plato {i}")
        juan += 1
    elif i == 2 or i == 5:
        input(f"pedro lavo el plato {i}")
        pedro += 1
    elif i == 3 or i == 6:
        input(f"mateo lavo el plato {i}")
        mateo += 1

input()