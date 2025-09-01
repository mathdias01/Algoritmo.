import math

""" Caso4: Análise de Vendas Mensais
Uma loja online registra o número de vendas de cada dia do mês em uma lista.
• Exemplo: [10, 15, 20, 5, 0, 8, ...]
O gerente precisa:
1. Calcular o total de vendas no mês.
2. Descobrir o dia com mais vendas e o dia com menos vendas.
3. Calcular a média de vendas por dia.
4. Listar os dias que tiveram vendas acima da média """



            

         







vendas_do_mes = [10, 15, 20, 5, 0, 8, 22, 21, 18, 17, 30, 28, 3, 7]




def calcular_total(lista_vendas):
    """Calcula o total de vendas no mês."""
    return sum(lista_vendas)

def encontrar_extremos(lista_vendas):
    """Encontra o dia com mais e com menos vendas."""
    dia_com_mais_vendas = max(lista_vendas)
    dia_com_menos_vendas = min(lista_vendas)
    return dia_com_mais_vendas, dia_com_menos_vendas

def calcular_media(lista_vendas):
    """Calcula a média de vendas por dia."""
    total_vendas = sum(lista_vendas)
    numero_de_dias = len(lista_vendas)
    media_exata = total_vendas / numero_de_dias
    return media_exata

def listar_dias_acima_media(lista_vendas, media_calculada):
    dias_acima = []
    for venda in lista_vendas:
        if venda > media_calculada:
            dias_acima.append(venda)
    return dias_acima



total_de_vendas = calcular_total(vendas_do_mes)
mais_vendas, menos_vendas = encontrar_extremos(vendas_do_mes)
media_de_vendas = calcular_media(vendas_do_mes)
dias_bons = listar_dias_acima_media(vendas_do_mes, media_de_vendas)


media_arredondada = math.ceil(media_de_vendas)


print("--- Relatório de Vendas Mensais ---")
print(f"Total de vendas no mês: {total_de_vendas} unidades.")
print(f"Dia com mais vendas: {mais_vendas} unidades.")
print(f"Dia com menos vendas: {menos_vendas} unidades.")
print(f"Média de vendas por dia: {media_de_vendas:.2f} unidades.")
print(f"Média arredondada para cima (para o gerente): {media_arredondada} unidades.")
print(f"Dias que tiveram vendas acima da média: {dias_bons}")