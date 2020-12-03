lista1 = [42,23,15,16,4,8]

def burbuja(lista):
    for i in range(len(lista)):
        for j in range(i)-1: 
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
        print(lista)

burbuja(lista1)
