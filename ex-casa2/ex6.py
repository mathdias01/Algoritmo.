lista = ['lula','celso','robinho','alves']

chave = input('Insira o nome que deseja verificar: ')

def buscaLinear(lista, chave):
    for nome in lista:
        if nome == chave:
            return 1
    return -1


busca = buscaLinear(lista, chave)
if busca == 1:
    print(f'A pessoa {chave} foi encontrada!')
else:
    print(f'A pessoa {chave} nao foi encontrada! ')