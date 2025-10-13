""" Maior Número (Busca Linear)
o Use busca sequencial para encontrar o maior número em uma lista.
 """
lista = [1,10,29,8,80,20]

def buscaSequencial(lista):
    maior_numero = lista[0]  
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero
   

maior = buscaSequencial(lista)
print(f'O maior numero da lista é {maior}')
