
from random import randint

def iniciar_cache(num_conjunto, tamanho_conjunto, numero_palavras):
    cache = []
    palavras = []

    for i in range(numero_palavras):
        palavras.append(-1)

    for i in range(num_conjunto):
        cache.append([])
        for j in range(tamanho_conjunto):
            cache[i] = [-1, -1, palavras]

    return cache

def imprimir_cache(cache):
    print("-=-" * 10)
    print("DirtyBit - Tag - Valor")
    for i in range(len(cache)):
        for j in range(len(cache[i])):
            print(cache[i][j], end=" ")
        print()
    print("-=-" * 10)


def memoria_principal(pos_memoria):
    memoria = []
    for i in range(pos_memoria):
        memoria.append(randint(0, 100))

    return memoria

imprimir_cache(iniciar_cache(2, 2, 4))


        