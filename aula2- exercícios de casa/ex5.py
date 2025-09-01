""" Caso5: Controle de Participação em um Evento
Os organizadores de um evento registraram os nomes dos participantes de cada atividade em
listas separadas.
• Exemplo:
o Palestra: ["Ana", "Carlos", "Marina"]
o Workshop: ["Carlos", "João", "Ana"]
o Mesa-redonda: ["Marina", "João", "Paula"]
Eles precisam:
1. Saber quem participou de todas as atividades.
2. Saber quem participou de apenas uma atividade.
3. Gerar uma lista com todos os nomes únicos dos participantes.
4. Contar quantos participantes distintos houve no evento. """

palestra = ['Ana', 'Carlos', 'Marina']
workshop =  ['Carlos', 'João', 'Ana']
mesa_redonda = ['João', 'Paula','Ana']
todas_atividades = [palestra, workshop, mesa_redonda]

def todas(todas_atividades):
    contagem = {}
    for lista_nomes in todas_atividades:
        for nome in lista_nomes:
            if nome in contagem:
                contagem[nome] += 1 
            else:
                contagem[nome] = 1
    return contagem


        
            


todasAtividades = todas(todas_atividades)
contagem_final = todasAtividades
numero_de_atividades = len(todas_atividades) 
presentes_em_todas = []
for nome, contagem in contagem_final.items():
   
    if contagem == numero_de_atividades:
        presentes_em_todas.append(nome)

print(f'Participantes presentes em todas as atividades: {presentes_em_todas}')
