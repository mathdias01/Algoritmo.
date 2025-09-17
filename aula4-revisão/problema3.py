
musicas = [
    {
        'titulo':'Back in Black',
        'artista':'AC/DC',
        'downloads':6800,
        'avaliacoes':[5,4,5,5,4,5]
    },
    {
        'titulo':'Stairway to Heaven',
        'artista':'Led Zeppelin',
        'downloads':8900,
        'avaliacoes':[5,5,4,5,5,5]
    },
    {
        'titulo':'Enter Sandman',
        'artista':'Metallica',
        'downloads':8100,
        'avaliacoes':[5,5,5,4,4,5]
    }
]

def mediaAvaliacao(musicas):
    medias = {}
    for musica in musicas:
        music = musica['titulo']
        ava = musica['avaliacoes']
        media = sum(ava)/len(ava)
        medias[music] = media
    return medias

def maior_downloads(musicas):
    downloads = {}
    for musica in musicas:
        artista = musica['artista']
        downloadsMusica = musica['downloads']
        if artista in downloads:
            downloads[artista] += downloadsMusica
        else:
            downloads[artista] = downloadsMusica
        

    maior = max(downloads.items(), key = lambda download: download[1])
    return maior

def ranking_avaliacoes(musicas):
    medias = {}
    for musica in musicas:
        music = musica['titulo']
        ava = musica['avaliacoes']
        media = sum(ava)/len(ava)
        medias[music] = media
    ranking = sorted(medias.items(), key = lambda media:media[1], reverse=True)
    return ranking
        

        

medias=(mediaAvaliacao(musicas))
print(f'As medias das avaliações de cada musica foram:{medias}')
maiorTotal = (maior_downloads(musicas))
print(f'O maior numero de downloads foi{maiorTotal}')
rank = (ranking_avaliacoes(musicas))
print(f'Segue em ordem o rank dos mais bem avaliados: {rank}')