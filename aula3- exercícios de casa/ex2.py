""" Caso6: Sistema de Biblioteca
Uma biblioteca mantém uma lista de livros emprestados, onde cada item é representado por
[titulo, usuario, dias_emprestado].
Exemplo:
[
 ["Dom Casmurro", "Ana", 5],
 ["1984", "Carlos", 12],
 ["O Hobbit", "Marina", 3]
]
O sistema precisa:
1. Listar apenas os livros que estão emprestados há mais de 7 dias.
2. Encontrar o livro emprestado há mais tempo.
3. Gerar uma lista apenas com os nomes dos usuários que têm livros emprestados.
4. Calcular a média de dias de empréstimo. """

livros = [
{'titulo':'Flash','usuario':'Tucson','dias_emprestado':5},
{'titulo':'A cabana','usuario':'Dias','dias_emprestado':7},
{'titulo':'batman','usuario':'Brunin','dias_emprestado':10},
{'titulo':'Superman','usuario':'Leozin','dias_emprestado':13}
]

def mais_7_dias(livros):
    livros_mais7 = []
    for livro in livros:
        if livro['dias_emprestado'] > 7:
            livros_mais7.append(livro)
    return livros_mais7


def mais_tempo(livros):
    Mais_tempo = max(livros, key = lambda livro: livro['dias_emprestado'])
    return Mais_tempo

def livros_emprestados(livros):
    livros_emp = []
    for livro in livros:
        if livro['dias_emprestado'] > 0:
            livros_emp.append(livro['usuario'])
    return livros_emp

def media(livros):
    lista_de_dias = []
    for livro in livros:
        lista_de_dias.append(livro['dias_emprestado'])
    Media = sum(lista_de_dias)/len(lista_de_dias)
    return Media    
    

mais_7 = mais_7_dias(livros)
print(f'Livros que estão emprestados a mais de 7 dias {mais_7}')
maistempo = mais_tempo(livros)
print(f'O livro que esta emprestado a mais tempo é {maistempo}')
livros_emprest = livros_emprestados(livros)
print(f'usuarios que possuem livros emprestados{livros_emprest}')
media_emp = media(livros)
print(f'A media de dias de emprestimo é {media_emp}')
