
def iniciar_cache(tamanho_cache):
    cache = {}
    for i in range(tamanho_cache):
        cache[i] = -1
    print("Cache inicializada: ")
    print("Valor da cache: ", tamanho_cache)
    return cache

def imprimir_cache(cache):

    print("-=-" * 10)
    print("Posição - Valor")
    for k, v in cache.items():
        print(k, v)
    print("-=-" * 10)

def mapeamento_direto(tamanho_cache, pos_memoria):
    
    cache = iniciar_cache(tamanho_cache)

    imprimir_cache(cache)

    hits = 0
    misses = 0
    trocas = 0;

    for value in pos_memoria:

        index = value % len(cache)
        found = False

        for k, v in cache.items():
            if v == value:
                hits += 1
                print(f"Hit: Valor {value} na posição {k} do cache!")
                found = True
                imprimir_cache(cache)
                break
        
        if not found:
            if cache[index] != -1:
                trocas += 1
                print(f"Miss: Valor {cache[index]} foi substituido por {value} na posição {index} do cache!")
            else:
                print(f"Miss: Valor {value} foi armazenado na posição {index} do cache!")

            cache[index] = value
            misses += 1
            imprimir_cache(cache)

    print(f"Total de hits: {hits}")
    print(f"Total de misses: {misses}")
    print(f"Total de trocas: {trocas}")
    print(f"Taxa de acerto: {hits / (hits + misses)}")

    print("Cache finalizada: ")
    imprimir_cache(cache)

mapeamento_direto(5, [3, 8, 13, 18, 23])


