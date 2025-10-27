l = int(input('Insira o número de alunos: '))
c = int(input('Insira o número de exercicios: '))

matriz = []
for i in range(l):
    linhas= []
    for j in range(c):
        ex = int(input(f'Insira a quantidade de repetições do aluno [{i+1}] do [{j+1}]: '))
        linhas.append(ex)
    matriz.append(linhas)

def totalRepeticoes(matriz, num_linhas, num_colunas):
    totais = []
    for j in range(num_colunas):
        soma = 0
        for i in range(num_linhas):
            soma += matriz[i][j]
            totais.append(soma)
    return totais


total = totalRepeticoes(matriz, l, c)
print('=== EXERCÍCIOS ===')
for j in range(c):
    print(f'Exercício {j+1} - {total[j]}')


