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

def criar_lru(num_conjuntos):

    numBlocosPermitidos = [2, 4, 8, 16]

    if(num_conjuntos not in numBlocosPermitidos):
        return False
    
    lru = {}
    for i in range(num_conjuntos):
        lru[i] = -1
    return lru

    
def print_cache(cache):
    print("-=-" * 10)
    print("Posição - Valor")
    for k, v in cache.items():
        print(k, v)
    print("-=-" * 10)

def print_lru(lru):
    print("LRU:")
    print("Conjunto - Posição LRU")
    for k, v in lru.items():
        print(f'{k}, {v}')
    print("-=-" * 10)

def mapeamento_assoc_LRU(num_conjuntos, tamanho_bloco, lista_dados_memoria):

    cache = criar_cache(num_conjuntos, tamanho_bloco)
    lru = criar_lru(num_conjuntos)
    
    if(not cache or not lru):
        print("Parametros invalidos!")
        return False
    
    print("Cache inicializada: ")
    print_cache(cache)
    print_lru(lru)

    hits = 0
    misses = 0
    trocas = 0

    for dict in lista_dados_memoria:
        for key, value in dict.items():
            conjunto = key
            dado = value

            existeEmCache = False

            for i in range(num_conjuntos):
                for pos, dado_cache in cache[i].items():
                    if(dado_cache == dado):
                        existeEmCache = True
                        hits += 1
                        print(f'Hit: Valor {dado} na posição {pos} do conjunto {i} do cache!')
                        print_cache(cache)
                        print_lru(lru)
                        pos_troca = lru[conjunto] % tamanho_bloco
                        if(pos_troca == pos):
                            lru[conjunto] += 1
                        break
                if(existeEmCache):
                    break

    
            if(not existeEmCache):
                misses += 1
                print(f'Miss: Valor {dado} não está no cache!')
                if(lru[conjunto] == -1):
                    for pos, dado_cache in cache[conjunto].items():
                        if(dado_cache == -1):
                            cache[conjunto][pos] = dado
                            lru[conjunto] = pos + 1
                            print(f'Valor {dado} foi armazenado na posição {pos} do conjunto {conjunto} do cache!')
                            print_cache(cache)
                            print_lru(lru)
                            break
                else:
                    trocouAlgumNulo = False
                    for pos, dado_cache in cache[conjunto].items():
                        if(dado_cache == -1):
                            trocouAlgumNulo = True
                            cache[conjunto][pos] = dado
                            lru[conjunto] += 1
                            print(f'Valor {dado} foi armazenado na posição {pos} do conjunto {conjunto} do cache!')
                            print_cache(cache)
                            print_lru(lru)
                            break
                    if(not trocouAlgumNulo):
                        pos_troca = lru[conjunto] % tamanho_bloco
                        cache[conjunto][pos_troca] = dado
                        lru[conjunto] += 1
                        trocas += 1
                        print(f'Valor {dado} foi armazenado na posição {pos_troca} do conjunto {conjunto} do cache!')
                        print_cache(cache)
                        print_lru(lru)
    print(f'Hits: {hits}')
    print(f'Misses: {misses}')
    print(f'Trocas: {trocas}')
            

    
#input int num_conjuntos, int tamanho_bloco, list lista_dados_memoria
mapeamento_assoc_LRU(2, 2, [{0 : 0}, {0 : 1}, {0 : 2}, {0 : 3}, {0 : 4}, {0 : 5}])