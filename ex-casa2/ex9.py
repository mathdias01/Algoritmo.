lista = [1,1,1,2,3,3,4,4,5,5,6,6]


chave = 3


def buscaBinaria(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == chave:
             resultado = pos_meio
             pos_fim = pos_meio -1
        elif lista[pos_meio] < chave:
             pos_ini = pos_meio + 1
        else: 
            pos_ini = pos_meio -1
    return resultado


busca = buscaBinaria(lista, chave)

if busca != -1:
    print(f'O numero {chave} foi achado primeiramente no indice {busca}')

else:
    print(f'O numero {chave} nao foi encontrado')
    