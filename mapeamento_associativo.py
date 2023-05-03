
def inicializar_cache(tamanho_conjunto):
    cache = {}
    for i in range(2):
        cache[i] = {}
        for j in range(tamanho_conjunto):
            cache[i][j] = -1
    print("Cache inicializada: ")
    imprimir_cache(cache)
    return cache

def imprimir_cache(cache):
    print("-=-" * 10)
    print("Posição - Valor")
    for k, v in cache.items():
        print(k, v)
    print("-=-" * 10)

def mapeamento_assoc(politica_de_substituição, pos_memoria):

    cache = inicializar_cache(2)

    hits = 0
    miss = 0
    trocas = 0

    lru = [0, 0]

    for value in pos_memoria:
        pos_cache = value % len(cache)
        found = False

        for k, v in cache.items():
            for k2, v2 in v.items():
                if v2 == value:
                    hits += 1
                    print(f"Hit: Valor {value} no bloco {k2} do conjunto {k} do cache!")
                    found = True
                    imprimir_cache(cache)
                    break
        
        if not found:
            miss += 1
            if(cache[pos_cache][0] == -1):
                cache[pos_cache][0] = value
                print(f"Miss: Valor {value} foi armazenado no bloco 0 do conjunto {pos_cache} do cache!")
                imprimir_cache(cache)

            elif(cache[pos_cache][1] == -1):
                cache[pos_cache][1] = value
                print(f"Miss: Valor {value} foi armazenado no bloco 1 do conjunto {pos_cache} do cache!")
                imprimir_cache(cache)       
            else:
                trocas += 1
                if(politica_de_substituição == "LRU"):
                    valor_ant = cache[pos_cache][lru[pos_cache] % 2]
                    cache[pos_cache][lru[pos_cache] % 2] = value
                    lru[pos_cache] += 1
                    print(f"Miss: Valor {valor_ant} foi substituido por {value} no conjunto {pos_cache} do cache!")
                    print(lru)
                    imprimir_cache(cache)

mapeamento_assoc("LRU", [3, 8, 13, 18, 23, 11, 12, 13, 14, 15, 16, 17, 18, 19])
