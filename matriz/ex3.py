
l = int(input('Insira o número de linhas: '))
c = int(input('Insira o número de colunas: '))

matriz = []
for i in range(l):
    linhas= []
    for j in range(c):
        paciente = input(f'Insira o nome do paciente [{i+1}][{j+1}]: ')
        linhas.append(paciente)
    matriz.append(linhas)

print(matriz)


def exibirAgenda(matriz):
   print('\n=========================')
   print('   AGENDA DO CONSULTÓRIO')
   print('=========================')
   segunda = matriz[0]
   print('SEGUNDA-FEIRA')
   print(f'8:00 {segunda[0]}, 15:00 {segunda[1]}, 19:00 {segunda[2]}')
   terca = matriz[1]
   print(f'TERÇA-FEIRA')
   print(f'8:00 {terca[0]}, 15:00 {terca[1]}, 19:00 {terca[2]}')
   quarta = matriz[2]
   print(f'QUARTA-FEIRA')
   print(f'8:00 {quarta[0]}, 15:00 {quarta[1]}, {quarta[2]}')
   quinta = matriz[3]
   print(f'QUINTA-FEIRA')
   print(f'8:00 {quinta[0]}, 15:00 {quarta[1]}, {quarta[2]}')
   sexta = matriz[4]
   print('SEXTA-FEIRA')
   print(f'8:00 {sexta[0]}, 15:00 {sexta[1]}, {sexta[2]}')



exibirAgenda(matriz)


