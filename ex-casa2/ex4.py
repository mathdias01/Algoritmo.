""" Menor Número (Busca Linear)
o Similar ao anterior, mas encontre o menor valor """

lista = [10,20,5,34,35,19]

def buscaSequencial(lista):
    menor_numero = lista[0]
    for numero in lista:
        if numero < menor_numero:
            menor_numero = numero
    return menor_numero


menor = buscaSequencial(lista)
print(f'o menor numero é: {menor}')
