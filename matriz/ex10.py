dias = 7
cidades = 3
matriz = []
for i in range(cidades):
    linhas = []
    for j in range(dias):
        linhas.append(int(input(f'Insira os valores de chuva da cidade {i+1} do dia {j+1} da semana: ')))
    matriz.append(linhas)


def maisChuva(matriz):
    cidades = []
    for cidade in matriz:
        soma = sum(cidade)
        cidades.append(soma)
    return cidades


totais = maisChuva(matriz)

for i in range(len(totais)):
    print(f'Total de chuva da cidade {i+1}: {totais[i]} mm')

indice_maior = totais.index(max(totais))
print(f'\nA cidade que mais choveu na semana foi a cidade {indice_maior + 1} com {max(totais)} mm de chuva.')