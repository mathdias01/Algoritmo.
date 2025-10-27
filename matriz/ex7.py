l = int(input('Insira o número de linhas: '))
c = int(input('Insira o número de colunas: '))

matriz = []
for i in range(l):
    linhas= []
    for j in range(c):
        produto = int(input(f'Insira o valor do produto [{i+1}] do dia [{j+1}]: '))
        linhas.append(produto)
    matriz.append(linhas)


def receitaTotal(matriz):
    total = []
    for produto in matriz:
        soma = sum(produto)
        total.append(soma)
    return total


receitaT = receitaTotal(matriz)
print(f'Produto 1 - {receitaT[0]}')
print(f'Produto 2 - {receitaT[1]}')
print(f'Produto 3 - {receitaT[2]}')
print(f'Produto 4 - {receitaT[3]}')
print(f'Produto 5 - {receitaT[4]}')

    
