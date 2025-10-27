l = int(input('Insira o número de linhas: '))
c = int(input('Insira o número de colunas: '))

matriz = []
for i in range(l):
    linhas= []
    for j in range(c):
        quantidade = int(input(f'Insira quantidade do produto  [{i+1}][{j+1}]: '))
        linhas.append(quantidade)
    matriz.append(linhas)

def totalProduto(matriz):
    totais = [
    sum(matriz[0]),
    sum(matriz[1]),
    sum(matriz[2]),
    sum(matriz[3]),
    ]
    return totais

total = totalProduto(matriz)
print('\n=== TOTAL DOS PRODUTOS ===')
print(f'Produto 1 : {total[0]}')
print(f'Produto 2 : {total[1]}')
print(f'Produto 3 : {total[2]}')
print(f'Produto 4 : {total[3]}')

