""" Caso2: Distâncias em Km
1. Receba as distâncias percorridas em 6 viagens e armazene em uma lista.
2. Calcule a distância total percorrida.
3. Mostre a maior e a menor distância.
4. Calcule a média das distâncias arredondada para cima (use math.ceil). """
import math as mt
viagens = []

def distancia_viagens(viagens):
    for viagem in range(5):
        viagem = int(input('Insira a distancia da viagem:'))
        viagens.append(viagem)

def maior_menor(viagens):
    maior = max(viagens)
    menor = min(viagens)
    return maior, menor

def media(viagens):
    soma = sum(viagens)
    media = soma/len(viagens)
    media_arredondada = mt.ceil(media)
    return media_arredondada
    



distancia_viagens(viagens)
print(viagens)
maior, menor = maior_menor(viagens)
md = media(viagens)
print(f'A media das distancias é {md}')
print(f'A distancia maior foi de {maior}Km e a menor de {menor}Km.')
        
