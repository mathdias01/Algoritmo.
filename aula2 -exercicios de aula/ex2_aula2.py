""" Estudo de Caso 2  Lista de compras interativa
Enunciado:
Faça um programa que:
1. Permita ao usuário adicionar itens a uma lista de compras.
2. Caso o usuário digite "sair", o programa encerra.
3. Mostre a lista final de compras organizada em ordem alfabética. """

compras = []

def add_itens(lista):
   item = input('Insira seu item:')
   while item != 'sair':
      item = input('Insira seu item:')
      lista.append(item)
   return lista

lista_compras = add_itens(compras)

compras.sort()
compras.remove('sair')
print(f'Suas compras em ordem alfabética:{compras}')

    