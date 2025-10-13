lista = [10,20,30,40,50,70,23,14]
valor = 100
def meu_index(lista, valor):
    for (indice, numero) in enumerate(lista):
        if numero == valor:
            return indice
    return -1
        

busca = meu_index(lista, valor)
if busca != -1:
    print(f'O indice do numero {valor} é: {busca}')
else:
    print(f'O valor {valor} nao foi encontrado em nenhum indice.')