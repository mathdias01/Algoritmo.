
l = int(input('Insira o número de linhas: '))
c = int(input('Insira o número de colunas: '))

matriz = []
for i in range(l):
    temperaturas = []
    for j in range(c):
        temp = int(input(f'Insira a temperatura [{i+1}][{j+1}]: '))
        temperaturas.append(temp)
    matriz.append(temperaturas)




def calcularMedia(matriz):
    medias = []
    for t in matriz:
        media = sum(t)/ len(t)
        medias.append(media)
    return medias
    

md=calcularMedia(matriz)

print('\n=== MÉDIA DAS TEMPERATURAS ===')
for i, m in enumerate(md):
    print(f'{i+ 1} - {m:.1f}')
