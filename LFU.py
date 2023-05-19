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

def criar_lfu(num_conjuntos, tamanho_bloco):

    numBlocosPermitidos = [2, 4, 8, 16]

    if(num_conjuntos not in numBlocosPermitidos):
        return False
    
    lfu = {}
    blocos = {}
    for i in range(num_conjuntos):
        for num_blo in range(tamanho_bloco):
            blocos[num_blo] = 0
        lfu[i] = blocos
    return lfu

    
def print_cache(cache):
    print("-=-" * 10)
    print("Posição - Valor")
    for k, v in cache.items():
        print(k,"-----","Palavras:",v)
        print("\n") 
    print("-=-" * 10)

def print_lfu(lfu):
    print("lfu:")
    print("Conjunto - Quantia de acessos:")
    for k, v in lfu.items():
        print(k,v)
        print("\n")
    print("-=-" * 10)

def mapeamento_assoc_lfu(num_conjuntos, tamanho_bloco, lista_dados_memoria):

    cache = criar_cache(num_conjuntos, tamanho_bloco)
    lfu = criar_lfu(num_conjuntos,tamanho_bloco)
    
    if(not cache or not lfu):
        print("Parametros invalidos!")
        return False
    
    print("Cache inicializada: ")
    print_cache(cache)
    print_lfu(lfu)

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
                        print_lfu(lfu)
                        pos_troca = lfu[conjunto] % tamanho_bloco
                        if(pos_troca == pos):
                            lfu[conjunto] += 1
                        break
                if(existeEmCache):
                    break
                
            if(not existeEmCache):
                misses += 1
                print(f'Miss: Valor {dado} não está no cache!')
                if(lfu[conjunto] == -1):
                    for pos, dado_cache in cache[conjunto].items():
                        if(dado_cache == -1):
                            cache[conjunto][pos] = dado
                            lfu[conjunto] += 1
                            print(f'Valor {dado} foi armazenado na posição {pos} do conjunto {conjunto} do cache!')
                            print_cache(cache)
                            print_lfu(lfu)
                            break
                else:
                    trocouAlgumNulo = False
                    for pos, dado_cache in cache[conjunto].items():
                        if(dado_cache == -1):
                            trocouAlgumNulo = True
                            cache[conjunto][pos] = dado
                            lfu[conjunto] += 1
                            print(f'Valor {dado} foi armazenado na posição {pos} do conjunto {conjunto} do cache!')
                            print_cache(cache)
                            print_lfu(lfu)
                            break
                    if(not trocouAlgumNulo):
                        pos_troca = lfu[conjunto] % tamanho_bloco
                        cache[conjunto][pos_troca] = dado
                        lfu[conjunto] += 1
                        trocas += 1
                        print(f'Valor {dado} foi armazenado na posição {pos_troca} do conjunto {conjunto} do cache!')
                        print_cache(cache)
                        print_lfu(lfu)
                        
    print(f'Hits: {hits}')                     
    print(f'Misses: {misses}')
    print(f'Trocas: {trocas}')
            

    
#input int num_conjuntos, int tamanho_bloco, list lista_dados_memoria
mapeamento_assoc_lfu(2, 2, 
                     [{0: 78}, 
                      {0: 79},
                       
                      {1: 24}, 
                      {1: 21}, 
                      
                      {0: 78}, 
                      {0: 150}, 
                      
                      {1: 150}, 
                      {1: 152}])