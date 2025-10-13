import random as rd
import time as tm
import tracemalloc as trc

trc.start()

lista = [rd.randint(1, 100) for i in range(1000000)]

def buscaBinaria(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == chave:
            return pos_meio
        if lista[pos_meio] > chave:
             pos_fim = pos_meio - 1
        if lista[pos_meio] < chave:
            pos_ini = pos_meio + 1
    return -1

lista.sort()

inicio = tm.time()

busca = buscaBinaria(lista,10)

final = tm.time()



memoria_atual, memoria_pico = trc.get_traced_memory()


print(f'o tempo de realização do algoritmo de busca binaria foi de {final - inicio:.9f} segundos')
print(f'A memoria atual é de {memoria_atual:.3f}')
print(f'A memoria no pico é de {memoria_pico:.3f}')
print(f'a posiçao do numero é {busca}')
trc.stop()
#print(lista)