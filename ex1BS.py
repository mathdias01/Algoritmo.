import random as rd
import time as tm
import tracemalloc as trc
trc.start()




lista = [rd.randint(1, 100) for i in range(1000000)]
#print(lista)

def buscaSequencial(lista, chave):
    for (índice, número) in enumerate(lista):
        if número == chave:
            return índice
    return -1





inicio = tm.time()

busca = (buscaSequencial(lista,10))

final = tm.time()

memoria_atual, memoria_pico = trc.get_traced_memory()

trc.stop()

print(f'O tempo de processo que a busca sequencial demorou para realizar a busca foi de:{final-inicio:.9f} segundos.')
print(f'esta na posicao {busca}')
print(f'a memoria atual é {memoria_atual/1024:.3f} KB')
print(f'a memoria  no pico da execução é {memoria_pico/1024:.3f} KB')

