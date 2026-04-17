import random

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

minha_lista100 = [random.randint(0, 100) for _ in range(101)]
minha_lista1000 = [random.randint(0, 100) for _ in range(1001)]

print(minha_lista1000)
print(bubble_sort(minha_lista100))
print(bubble_sort(minha_lista1000))