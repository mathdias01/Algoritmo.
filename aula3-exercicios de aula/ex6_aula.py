""" 6. Crie um dicionário representando um carro com as chaves: marca, modelo e ano.
a. Adicione ao dicionário do carro a chave 'cor'.
b. Crie um dicionário de notas de 3 alunos (nome como chave, nota como
valor).
c. Acesse a nota de um dos alunos e exiba.
d. Remova um aluno do dicionário de notas. """  

carro = {'marca':'Fiat','modelo':'Palio','ano':2000}
carro.update({'cor':'preto'})

alunos = {'Luiz':10,'Cornoncio':9,'Fadigado':8}
print(alunos['Luiz'])
alunos.pop('Fadigado')
print(alunos)