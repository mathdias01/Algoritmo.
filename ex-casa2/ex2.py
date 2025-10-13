""" 2. Contar Ocorrências (Busca Linear)
o Conte quantas vezes um número aparece na lista usando busca sequencial. """

lista = [2,2,8,10,9,7,7,10]
chave = int(input('Insira o numero que deseja verificar a quantidade: '))
def buscaSequencial(lista, chave):
    quantidade = 0
    for  numero in lista:
        if numero == chave:
            quantidade += 1
    return quantidade

            

qtd = buscaSequencial(lista, chave)

if qtd > 0:
    print(f'O número {chave} aparece {qtd} vezes na lista.')
else:
    print('Número não encontrado.')

print(f'A quantidade de numeros presentes é {qtd} ')