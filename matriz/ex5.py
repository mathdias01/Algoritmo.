l = int(input('Insira o número de linhas: '))
c = int(input('Insira o número de colunas: '))

matriz = []
for i in range(l):
    linhas= []
    for j in range(c):
        pontos = int(input(f'Insira a pontuação do [{i+1}] no jogo [{j+1}]: '))
        linhas.append(pontos)
    matriz.append(linhas)
print('=== TIMES ===')
print(f'TIME 1 - {matriz[0]}')
print(f'TIME 2 - {matriz[1]}')
print(f'TIME 3 - {matriz[2]}')

def maior(matriz):
    totais = []
    totais.append(sum(matriz[0]))
    totais.append(sum(matriz[1]))
    totais.append(sum(matriz[2]))
    ganhador = max(totais)
    if ganhador == totais[0]:
        print(f'O GANHADOR É O TIME 1 COM {totais[0]}!')
    elif ganhador == totais[1]:
        print(f'O GANHADOR É O TIME 2 COM {totais[1]}!')
    elif ganhador == totais[2]:
        print(f'O GANHADOR É O TIME 3 COM {totais[2]}!')
    

maior(matriz)