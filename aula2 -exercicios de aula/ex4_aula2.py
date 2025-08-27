""" Estudo de Caso 4 - Controle de Vendas em uma Loja de Eletrônicos
Contexto do Problema
Imagine que você trabalha em uma loja de eletrônicos que precisa organizar melhor o registro
diário de vendas. Até então, os vendedores anotavam em papel ou planilhas, mas o dono pediu
para criar um programa simples em Python para armazenar, analisar e gerar pequenos
relatórios sobre as vendas do dia.
O sistema precisa:
1. Guardar os produtos vendidos (nome e preço).
2. Mostrar o valor total arrecadado.
3. Identificar o produto mais caro e o mais barato do dia.
4. Permitir consultar se um produto específico foi vendido. """

produtos_vendidos = []




def guarda_valores (produtos_vendidos):
    while True:
       produto = input('''
--Tabela de preços--                     
Celular = 1000,00 (1)
Alexa = 300,00    (2)
Tablet = 500,00   (3) 
Mouse = 50,00     (4)
Teclado = 100,00  (5)
Escolha o produto pelo número(se não quiser comprar mais, digite 'sair'):''')
       if produto == 'sair':
          break
       if produto == '1':
        produtos_vendidos.append({'Nome':'Celular', 'preco':1000})
       elif produto == '2':
        produtos_vendidos.append({'Nome':'Alexa', 'preco':300})
       elif produto == '3':
        produtos_vendidos.append({'Nome':'Tablet','preco':500})
       elif produto == '4':
            produtos_vendidos.append({'Nome':'Mouse','preco':50})
       elif produto == '5':
            produtos_vendidos.append({'Nome':'Teclado', 'preco':100})

    return produtos_vendidos

def valor_total(lista_de_vendas):
   total = 0
   for venda in lista_de_vendas:
      total += venda['preco']
   return total

def maior_menor(produtos_vendidos):
   maior = max(produtos_vendidos, key=lambda item: item['preco'])
   menor = min(produtos_vendidos, key=lambda item: item['preco'])
   return maior, menor 

def procurar_produto(produtos_vendidos):
   produto = input('Insira o nome do produto que deseja verificar se foi vendido:')
   for produtos in produtos_vendidos:
      if produtos['Nome'] == produto:
         print(f'O produto foi vendido:{produto}')
   else:
    print(f'O produto {produto} não foi vendido:')
         
         








guarda_valores(produtos_vendidos)
print(produtos_vendidos)
Total = valor_total(produtos_vendidos)
print(f'O valor total é:{Total}')
maior, menor = maior_menor(produtos_vendidos)
print(f'O valor maior é {maior} e o menor é {menor}')
procurar_produto(produtos_vendidos)

   

       
    
    