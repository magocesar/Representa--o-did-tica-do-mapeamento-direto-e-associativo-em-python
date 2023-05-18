
def criar_cache_lru(tamanho_bloco):
    
    #Tamanhos permitidos para o bloco
    tamanhos_permitidos = [1, 2, 4, 8, 16]
    if(tamanho_bloco not in tamanhos_permitidos):
        return False
    
    #2 Conjuntos na Cache, "tamanho_bloco" linhas por conjunto
    cache = {}
    cache[0] = {}
    cache[1] = {}
    for i in range(tamanho_bloco):
        cache[0][i] = -1
        cache[1][i] = -1
    
    lru = {}
    lru[0] = -1
    lru[1] = -1

    return cache, lru
    
def print_cache(cache):
    print("-=-" * 10)
    print("Posição - Valor")
    for k, v in cache.items():
        print(k, v)
    print("-=-" * 10)

def mapeamento_assoc_LRU(tamanho_bloco, lista_dados_memoria):

    cache, lru = criar_cache_lru(tamanho_bloco)
    
    if(not cache):
        print("Tamanho de bloco inválido!")
        return False
    
    print("Cache inicializada: ")
    print_cache(cache)
    print(lru)

    hits = 0
    misses = 0
    trocas = 0

    for dict in lista_dados_memoria:
        for key, value in dict.items():
            conjunto = key
            dado = value

            if(dado in cache[0].values() or dado in cache[1].values()):
                hits += 1
                print(f"Hit: Valor {dado} no conjunto {conjunto} do cache!")
                print_cache(cache)
                print(lru)

            else:
                misses += 1
                print(f'Miss: Valor {dado} não está no cache!')
                if(lru[conjunto] == -1):
                    for pos, dado_cache in cache[conjunto].items():
                        if(dado_cache == -1):
                            cache[conjunto][pos] = dado
                            lru[conjunto] = pos + 1
                            print(f'Valor {dado} foi armazenado na posição {pos} do conjunto {conjunto} do cache!')
                            print_cache(cache)
                            print(lru)
                            break
                else:
                    pos_troca = lru[conjunto] % tamanho_bloco
                    flag = False
                    for pos, dado_cache in cache[conjunto].items():
                        if(dado_cache == -1):
                            flag = True
                            cache[conjunto][pos] = dado
                            lru[conjunto] += 1
                            print(f'Valor {dado} foi armazenado na posição {pos} do conjunto {conjunto} do cache!')
                            print_cache(cache)
                            print(lru)
                            break
                    if(not flag):
                        cache[conjunto][pos_troca] = dado
                        lru[conjunto] += 1
                        print(f'Valor {dado} foi armazenado na posição {pos_troca} do conjunto {conjunto} do cache!')
                        print_cache(cache)
                        print(lru)
                        trocas += 1

            

    

mapeamento_assoc_LRU(8, [{0: 78}, {0: 29}, {0: 24}, {0: 21}, {0: 71}, {0: 150}, {0: 151}])
