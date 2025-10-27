l = int(input('Insira o número de linhas: '))
c = int(input('Insira o número de colunas: '))

matriz = []
for i in range(l):
    linhas= []
    for j in range(c):
        horarios = (input(f'Insira o horario [{i+1}][{j+1}]: '))
        linhas.append(horarios)
    matriz.append(linhas)

def buscarHorarios(matriz):
    print('=== BUSCADOR DE HORÁRIOS ===')
    print('Busque pelo indice')
    print('Linha 1 - (1)')
    print('Linha 2 - (2)')
    print('Linha 3 - (3)')
    print('Linha 4 - (4)')
    buscar = int(input('Escolha: '))
    if buscar == 1:
        print(matriz[0])
    elif buscar == 2:
        print(matriz[1])
    elif buscar == 3:
        print(matriz[2])
    elif buscar == 4:
        print(matriz[3])


buscarHorarios(matriz)
