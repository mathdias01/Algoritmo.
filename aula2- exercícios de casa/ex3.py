""" Caso3: Supermercado  Controle de Estoque
Um supermercado mantém uma lista de produtos e seus preços.
• Cada item será representado como [nome, quantidade, preco_unitario].
• O sistema deve:
1. Calcular o valor total em estoque.
2. Encontrar o produto de maior valor total (quantidade x preço).
3. Gerar uma lista apenas com os nomes dos produtos com estoque abaixo de 5
unidades.
4. Permitir buscar um produto pelo nome e retornar seus dados. """

estoque = [
{'nome':'Arroz','qtd':10, 'preco':20},
{'nome':'Feijão','qtd':15,'preco':15},
{'nome': 'Óleo de Soja', 'qtd': 24, 'preco': 7},
{'nome': 'Sal', 'qtd': 3, 'preco': 3.50},     
{'nome': 'Macarrão', 'qtd': 4, 'preco': 4.75}    
]

estoque_5 = []

def total(estoque):
    valorTotal = 0
    for produto in estoque:
     valorTotal += produto['qtd']*produto['preco']
      
    return valorTotal

def maior_produto(estoque):
   maior = max(estoque, key=lambda produto: produto['qtd']*produto['preco'])
   return maior

def estoque_cinco(estoque_5, estoque):
   for i in estoque:
      if i['qtd']<5:
         estoque_5.append(i)
   return estoque_5

def busca(estoque):
   buscar = input('Insira o produto que procura:')
   for i in estoque:
     if buscar == i['nome']:
       return i
    
   return -1

valor_total = total(estoque)
print(f'O valor total é {valor_total:.2f}')
maior = maior_produto(estoque)
print(f'O produto de maior valor total é {maior}')
mnr_5 =estoque_cinco(estoque_5, estoque)
print(f'Menores que cinco unidades no estoque:{mnr_5}')
buscar = busca(estoque)
if buscar == -1:
   print('Produto não encontrado')
else:
    print(f'produto encontrado! {buscar}')


   
      


