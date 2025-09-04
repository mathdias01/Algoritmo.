import math

""" Caso4: Análise de Vendas Mensais
Uma loja online registra o número de vendas de cada dia do mês em uma lista.
• Exemplo: [10, 15, 20, 5, 0, 8, ...]
O gerente precisa:
1. Calcular o total de vendas no mês.
2. Descobrir o dia com mais vendas e o dia com menos vendas.
3. Calcular a média de vendas por dia.
4. Listar os dias que tiveram vendas acima da média """

dias = {
    'dia1': 10, 'dia2': 15, 'dia3': 20, 'dia4': 5, 'dia5': 0,
    'dia6': 8, 'dia7': 22, 'dia8': 21, 'dia9': 18, 'dia10': 17,
    'dia11': 30, 'dia12': 28, 'dia13': 3, 'dia14': 7
}

def total(dias):
    total_vendas = sum(dias.values())
    return total_vendas

def mais_menos(dias):
    mais = max(dias.values())
    menos = min(dias.values())
    return mais, menos

def media_dia(dias):
    media = sum(dias.values())/len(dias.values())
    media_arredondada = math.ceil(media)
    return media_arredondada

def acima_media(dias):
    dias_acima = {}
    media = sum(dias.values())/len(dias)
    for dia, venda in dias.items():
        if venda > media:
            dias_acima[dia] = venda
    return dias_acima


total_vendas = total(dias)
print(f'O total de vendas foi {total_vendas}')
mais, menos = mais_menos(dias)
print(f'O dia com mais vendas foi {mais}, e o com menos foi {menos}.')
media = media_dia(dias)
print(f'A media de vendas por dia é {media}')
acima_da_media = acima_media(dias)
print(f'Os dias acima da média foram:{acima_da_media}')
            
      

