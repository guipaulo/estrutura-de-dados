import random

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j -= 1

        lista[j+1] = chave

    return lista

minha_lista100 = [random.randint(0, 100) for _ in range(101)]
minha_lista1000 = [random.randint(0, 100) for _ in range(1001)]

print(insertion_sort(minha_lista100))
print(insertion_sort(minha_lista1000))
