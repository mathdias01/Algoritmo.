""" Estudo de Caso 1  Temperaturas da Semana
Enunciado:
Crie um programa que:
1. Receba as temperaturas de 7 dias e armazene em uma lista.
2. Mostre a média das temperaturas da semana.
3. Informe o dia mais quente e o dia mais frio.
4. Mostre quantos dias ficaram acima da média. """





temperaturas= []

def temp(lista):
    for i in range(7):
      temper = int(input('Insira a temperatura do dia atual:'))
      lista.append(temper)

    
def mediaCalculo(lista):
   soma = int(sum(lista))
   media =int(soma/len(lista))
   return media


def acima_media(lista):
   temp_acimaMedia = 0
   soma = int(sum(lista))
   media =int(soma/len(lista))
   for i in lista:
     if i>media:
      temp_acimaMedia += 1
   return temp_acimaMedia


temp(temperaturas)
print(f'temperaturas: segunda({temperaturas[0]}), terça({temperaturas[1]}), quarta({temperaturas[2]}), quinta({temperaturas[3]}), sexta({temperaturas[4]}), sábado({temperaturas[5]}), domingo({temperaturas[6]})')
media = mediaCalculo(temperaturas)
print(f'A média das temperaturas é:{media}')


maior = max(temperaturas)
menor = min(temperaturas)

print(f'A temperatura maior é {maior} e a menor é {menor} ')
acimaMedia = acima_media(temperaturas)
print(f'A quantidade de temperaturas acima da média é {acimaMedia}')



