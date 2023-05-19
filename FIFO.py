def initialize_cache(cache_size):
    cache = [-1] * cache_size
    return cache

def print_cache(cache):
    print("Cache:", cache)

def simulate_cache_access(memory, cache_size, set_size):
    cache_blocks = cache_size // set_size
    cache = initialize_cache(cache_size)  # Inicializa a cache com todas as posições como -1
    hits = 0
    misses = 0
    fifo_queue = []  # Fila para manter o controle dos blocos na ordem em que foram adicionados

    print("Cache Inicial:")
    print_cache(cache)
    print()

    for address in memory:
        set_index = address % (cache_size // set_size)  # Calcula o índice do conjunto para o endereço atual
        block_index = set_index * set_size  # Calcula o índice inicial do bloco correspondente ao conjunto

        if address in cache[block_index : block_index + set_size]:
            hits += 1
            print("Hit! O endereço", address, "está presente na cache.")
        else:
            misses += 1
            print("Miss! O endereço", address, "não está presente na cache.")

            if len(fifo_queue) == cache_blocks:
                removed_block_index = fifo_queue.pop(0)  # Remove o índice do bloco mais antigo da fila
                cache[removed_block_index] = -1  # Substitui o bloco mais antigo com -1 na cache

            cache[block_index] = address  # Adiciona o endereço atual ao bloco correspondente na cache
            fifo_queue.append(block_index)  # Adiciona o índice do bloco à fila

        print_cache(cache)
        print()

    print("Resumo:")
    print("Hits:", hits)
    print("Misses:", misses)

# Exemplo de uso
memory = [5, 7, 10, 12, 5, 15, 20, 10, 12, 25, 5, 30]
cache_size = 8  # Tamanho da cache
set_size = 4    # Tamanho do conjunto
simulate_cache_access(memory, cache_size, set_size)
