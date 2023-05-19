def criar_cache(num_conjuntos, tamanho_bloco):
    tamanhos_permitidos_bloco = [1, 2, 4, 8, 16]
    numerosConjuntosPermitidos = [2, 4, 8, 16]
    if tamanho_bloco not in tamanhos_permitidos_bloco or num_conjuntos not in numerosConjuntosPermitidos:
        return False
    
    cache = {}
    for i in range(num_conjuntos):
        cache[i] = [-1] * tamanho_bloco
    return cache

def criar_FIFO(num_conjuntos):
    numBlocosPermitidos = [2, 4, 8, 16]
    if num_conjuntos not in numBlocosPermitidos:
        return False
    
    fifo = {}
    for i in range(num_conjuntos):
        fifo[i] = []
    return fifo

def print_cache(cache):
    print("-=-" * 10)
    print("Posição - Valor")
    for k, v in cache.items():
        print(k, v)
    print("-=-" * 10)

def print_fifo(fifo):
    print("FIFO:")
    print("Conjunto - Ordem de Chegada")
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
        for conjunto, dado in dict.items():
            if any(dado in bloco for bloco in cache.values()):
                hits += 1
                print(f'Hit! Dado {dado} encontrado no conjunto {conjunto}')
                print_cache(cache)
                print_fifo(fifo)
            else:
                misses += 1
                print(f'Miss! Dado {dado} não encontrado no conjunto {conjunto}')
                if len(fifo[conjunto]) < tamanho_bloco:
                    pos = len(fifo[conjunto])
                    cache[conjunto][pos] = dado
                    fifo[conjunto].append(pos)
                    print(f'Valor {dado} foi armazenado na posição {pos} do conjunto {conjunto} da cache!')
                    print_cache(cache)
                    print_fifo(fifo)
                else:
                    pos_troca = fifo[conjunto][0]
                    cache[conjunto][pos_troca] = dado
                    fifo[conjunto] = fifo[conjunto][1:] + [pos_troca]
                    print(f'Valor {dado} foi armazenado na posição {pos_troca} do conjunto {conjunto} da cache!')
                    print_cache(cache)
                    print_fifo(fifo)
    
    print(f'Hits: {hits}')
    print(f'Misses: {misses}')
    print(f'Taxa de acerto: {hits / (hits + misses)}')



mapeamento_assoc_FIFO(2, 4, [{0: 78}, {0: 29}, {0: 24}, {0: 21}, {0: 71}, {1: 70}, {1: 71}])