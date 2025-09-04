""" 1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "curso".
Em seguida, exiba apenas o nome do aluno. """
""" 2. Adicione uma nova chave "nota" com valor 9.5 ao dicionário aluno.
Depois, remova a chave "idade" """
""" 4. Dado o dicionário aluno, verifique se existe a chave "curso". """


aluno = {'nome':'Temer','idade':12,'curso':'ed.fisica'}
print(aluno['nome'])

aluno.update({'nota': 9.5})
print(aluno)
aluno.pop('idade')
print(aluno)
if 'curso' in aluno:
    print('Curso esta presente em dicionario aluno')
else:
    print('Nao esta presente')
