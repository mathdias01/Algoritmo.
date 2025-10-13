""" . Busca Linear Simples
o Dado um vetor de números inteiros e um número alvo, use busca sequencial para
verificar se o número está presente.
o Extra: informe o índice se encontrar. """


meu_vetor = [45, 22, 18, 9, 76, 53, 31]
numero_alvo = 9

def buscaSequencial(lista, chave):
    for (indice, numero) in enumerate(lista):
        if numero == chave:
            return indice
    return -1

print('Procuarando elemento...' )
busca = buscaSequencial(meu_vetor, numero_alvo)
print(f'O numero foi encontrado! e esta no indice: {busca}')

