arboles = int(input("Ingresa numero de arboles: "))

for i in range(arboles):
    altura = 1
    ciclos = int(input(f'Ingresa el numero de ciclos para el arbol {i}: '))
    for j in range(ciclos):
        if j%2!=0:
            altura*=2
        else:
            altura+=1
    print(f'La altura para el arbol {i} es: {j} ')