""" Verificar Elemento (Busca Binária)
o Dada uma lista ordenada, implemente a busca binária para verificar se o
elemento existe. """

lista = [1,2,4,10,11,18,20]
chave = 18

def buscaBinaria(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1
    while pos_ini <= pos_fim:
        pos_mei = (pos_ini + pos_fim)//2
        if lista[pos_mei] == chave:
            return pos_mei
        if lista[pos_mei] > chave:
            pos_fim = pos_mei - 1
        if lista[pos_mei] < chave:
            pos_ini = pos_mei + 1
    return -1

busca = buscaBinaria(lista, chave)
print(f'O numero {chave} foi encontrado no indice {busca}')

        
