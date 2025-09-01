""" Caso1: Controle de Presença em Sala de Aula
Uma professora precisa registrar a presença dos alunos durante a semana.
• Cada dia da semana terá uma lista com os nomes dos presentes.
• No final, ela precisa:
1. Saber quais alunos estiveram presentes todos os dias.
2. Saber quais alunos faltaram em pelo menos um dia.
3. Saber o número total de presenças por aluno. """


segunda = ["Ana", "Bia", "Carlos"]
terca = ["Ana", "Carlos"]
quarta = ['Bia', "Carlos", "Ana"]
quinta = ['Ana', 'Carlos']
sexta = ['Bia', 'Ana']
presencas_semana = [segunda, terca, quarta, quinta, sexta]
todos_alunos = ["Ana", "Bia", "Carlos", "Daniel"]


contagem_presencas = {}


for aluno in todos_alunos:
    contagem_presencas[aluno] = 0

for lista_dia in presencas_semana:
    for nome_presente in lista_dia:
        contagem_presencas[nome_presente] += 1 
        if contagem_presencas[nome_presente] == len(presencas_semana):
            print(f'O aluno(a) {nome_presente} esteve presente todos os dias!')
print(contagem_presencas)