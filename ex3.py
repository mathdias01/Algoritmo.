notas = [9,8,7,6,8]
soma = 0 
media_minima = 7
aprovados = 0 
for i in notas:
    soma += i
media = soma/len(notas)
print(f'A media das notas é :{media}')

maior = max(notas)
menor = min(notas)
print(f'A nota maior é {maior} e a menor é {menor}')

for p in notas:
    if p>=media_minima:
        aprovados+=1
percentual = aprovados/len(notas)*100
print(f'O percentual é %{percentual}')


