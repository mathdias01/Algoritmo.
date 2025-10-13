produtos = [
{'produto':'arroz','preco':20},
{'produto':'feijao','preco':15},
{'produto':'sal','preco':12},
{'produto':'tomate','preco':20}    
]
valor = float(input('Insira o valor que deseja verificar dos produtos: '))
def buscaPreco(lista, chave):
    encontrados = []
    for produto in lista:
        if produto['preco'] == chave:
            encontrados.append(produto)
    return encontrados
    

busca = buscaPreco(produtos, valor)
if busca:
    print(f'Os produtos deste valor(R${valor:.2f}), foram encontrados!')
    for p in busca:
        print(f" - {p['produto']}")
else:
    print(f'Nao existem produtos com este valor, R${valor:.2f}')

            