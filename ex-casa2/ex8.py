import random as rd
import time as tm



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






print(f'o tempo de realização do algoritmo de busca binaria foi de {final - inicio:.9f} segundos')
print(f'a posiçao do numero é {busca}')







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





print(f'O tempo de processo que a busca sequencial demorou para realizar a busca foi de:{final-inicio:.9f} segundos.')
print(f'esta na posicao {busca}')




