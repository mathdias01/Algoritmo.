atletas = [
    {
        'nome':'Lucas',
        'idade':20,
        'modalidades':['Natação','Corrida'],
        'treinos':{'Natação':12,'Corrida':8}
    },
    {
        'nome': 'Mariana',
        'idade':25,
        'modalidades':['Musculação','Yoga','Pilates'],
        'treinos':{'Natação':15,'Yoga':10,'Pilates':5}
    },
    {
        'nome':'João',
        'idade':22,
        'modalidades':['Corrida','Ciclismo'],
        'treinos':{'Corrida':20,'Ciclismo':18}
    }
]


def mediaIdade(atletas):
    esporte = input('Insira o esporte para ver a media de idade dele:')
    idades = []
    for atleta in atletas:
         if esporte in atleta['modalidades']:
            idades.append(atleta['idade'])
    else:
        print('atleta nao encontrado!')
    
    if len(idades)> 0:
     media = sum(idades)/len(idades)
    return media
    

def esporte_mais_treinado(atletas):
   esportista = input('Escolha o atleta para ver qual esporte ele mais treinou:')
   for atleta in atletas:
      if esportista == atleta['nome']:
         maisTreinado = max(atleta['treinos'], key = atleta['treinos'].get  )
   return maisTreinado

def mais_de_2(atletas):
   mais2 = []
   for atleta in atletas:
      if len(atleta['modalidades']) > 2:
         mais2.append(atleta['nome'])
   return mais2

media = (mediaIdade(atletas))
print(f'A media de idades neste esporte é:{media}')
esporte_mais =(esporte_mais_treinado(atletas))
print(f'O esporte mais treinado pelo atleta selecionado é:{esporte_mais}')
mais_de2 = mais_de_2(atletas)
print(f'Lista de atletas que praticam mais de 2 esportes:{mais_de2}')
