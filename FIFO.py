def criar_cache(num_conjuntos, tamanho_bloco):
    
    
    tamanhos_permitidos_bloco = [1, 2, 4, 8, 16]
    numerosConjuntosPermitidos = [2, 4, 8, 16]
    if(tamanho_bloco not in tamanhos_permitidos_bloco or num_conjuntos not in numerosConjuntosPermitidos):
        return False
    
    cache = {}
    for i in range(num_conjuntos):
        cache[i] = {}
        for j in range(tamanho_bloco):
            cache[i][j] = -1
    return cache

def criar_FIFO(num_conjuntos):

    numBlocosPermitidos = [2, 4, 8, 16]

    if(num_conjuntos not in numBlocosPermitidos):
        return False
    
    fifo = {}
    for i in range(num_conjuntos):
        fifo[i] = -1
    return fifo


def print_cache(cache):
    print("-=-" * 10)
    print("Posição - Valor")
    for k, v in cache.items():
        print(k, v)
    print("-=-" * 10)

def print_fifo(fifo):
    print("LRU:")
    print("Conjunto - Posição LRU")
    for k, v in fifo.items():
        print(f'[{k}, {v}]')
    print("-=-" * 10)

def mapeamento_assoc_FIFO(num_conjuntos, tamanho_bloco, lista_dados_memoria):
    cache = criar_cache(num_conjuntos, tamanho_bloco)
    fifo = criar_FIFO(num_conjuntos)  # Inicializa a cache com todas as posições como -1

    hits = 0
    misses = 0

    print("Cache Inicial:")
    print_cache(cache)
    print()

    for dict in lista_dados_memoria:
        for key, value in dict.items():
            conjunto = key
            dado = value

            for i in range(num_conjuntos):
                if(dado in cache[i].values()):
                    hits += 1 
                    print(f'Hit! Dado {dado} encontrado no conjunto {conjunto}')
                    print_cache(cache)
                    print_fifo(fifo)
                    break
                else:
                    misses+=1
                    print(f'Miss! Dado {dado} não encontrado no conjunto {conjunto}')
                    if (fifo[conjunto] == -1):
                        for pos, dado_cache in cache[conjunto].items():
                            if(dado_cache == -1):
                                cache[conjunto][pos] = dado
                                fifo[conjunto] = pos + 1
                                print(f'Valor {dado} foi armazenado na posição {pos} do conjunto {conjunto} da cache!')
                                print_cache(cache)
                                print_fifo(fifo)
                                break
                    else:
                        flag = False
                        for pos, dado_cache in cache[conjunto].items(): 
                            if(dado_cache == -1):
                                flag = True
                                cache[conjunto][pos] = dado
                                fifo[conjunto] += 1
                                print(f'Valor {dado} foi armazenado na posição {pos} do conjunto {conjunto} da cache!')
                                print_cache(cache)
                                print_fifo(fifo)
                                break
                        if(not flag): 
                            pos_troca = fifo[conjunto] 
                            cache[conjunto][pos_troca] = dado
                            fifo[conjunto] = (pos_troca + 1) % tamanho_bloco
                            print(f'Valor {dado} foi armazenado na posição {pos_troca} do conjunto {conjunto} da cache!')
                            print_cache(cache)
                            print_fifo(fifo)
    print(f'Hits: {hits}')
    print(f'Misses: {misses}')
    print(f'Taxa de acerto: {hits/(hits+misses)}')

mapeamento_assoc_FIFO(2, 4, [{0: 78}, {0: 29}, {0: 24}, {0: 21}, {0: 71}, {0: 150}, {0: 151}, {1: 152}, {1: 152}, {1: 152}, {1: 152}, {1: 152}, {1: 152}, {1: 152}, {1: 152}, {1: 152}])