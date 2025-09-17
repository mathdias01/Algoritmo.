filmes = [
    {
        'titulo':'Inception',
        'diretor':'Cristopher Nolan',
        'bilheteria':830,
        'avaliacoes':[9,10,8,9,10]
    },
    {
        'titulo':'Avengers: Endgame',
        'diretor':'Anthony Russo',
        'bilheteria':2797,
        'avaliacoes':[9,9,10,10,9]
    },
    {
        'titulo':'The Dark Knight',
        'diretor':'Cristopher Nolan',
        'bilheteria':1005,
        'avaliacoes':[10,10,9,10,10]
    },
    {
        'titulo':'Jurassic Park',
        'diretor':'Steven Spielberg',
        'bilheteria':1029,
        'avaliacoes':[8,9,9,8,9]
    }
]

def top_bilheteria(filmes):
    filme_bilheteria = {}
    for filme in filmes:
        nome = filme['titulo']
        filme_bilheteria[nome]= filme['bilheteria']
    rank = sorted(filme_bilheteria.items(), key= lambda filme: filme[1], reverse = True)
    rank_3 = rank[:3]
    return rank_3

def top_avaliacao(filmes):
    filmes_media = {}
    for filme in filmes:
        nome = filme['titulo']
        avaliacao= filme['avaliacoes']
        media = sum(avaliacao)/len(avaliacao)
        filmes_media[nome]= media
    ranking = sorted(filmes_media.items(), key= lambda filme: filme[1], reverse = True)
    rank_3 = ranking[:3]
    return rank_3

def bilheteria_por_diretor(filmes):
    diretor_totalDaBilheteria = {}
    for filme in filmes:
        diretor = filme['diretor']
        bilheteria = filme['bilheteria']
        if diretor in diretor_totalDaBilheteria:
            diretor_totalDaBilheteria[diretor] += bilheteria
        else:
            diretor_totalDaBilheteria[diretor] = bilheteria
    return diretor_totalDaBilheteria

def campeao(filmes):
     filme_campeao = max(filmes, key=lambda filme: filme['bilheteria'] * (sum(filme['avaliacoes']) / len(filme['avaliacoes'])))
     return filme_campeao
    
        


rank_bilheteria = (top_bilheteria(filmes))
print(f'O rank dos 3 filmes com maior bilheteria esta em ordem decrescente a seguir:{rank_bilheteria}')
rank_avaliacao = (top_avaliacao(filmes))
print(f'O rank dos 3 mais bem avaliados esta em ordem decrescente a seguir:{rank_avaliacao}')
bilheteria = bilheteria_por_diretor(filmes)
print(f'Total de bilheteria por diretor:{bilheteria}')
filme_campeao = (campeao(filmes))
print(f'O filme campeao é:{filme_campeao}')