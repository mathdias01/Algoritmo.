pessoas = [
{"nome": "Ana", "idade":25},
{'nome': 'joao', 'idade': 10},
{'nome':'Clara','idade':20}
]

chave = 'joaoa'
def buscaLinear(lista, chave):
    for pessoa in lista:     
        if pessoa['nome'] == chave:
            return pessoa
    return None

busca = buscaLinear(pessoas, chave)
if busca:
    print(f'O nome {busca['nome']} foi encontrado, e a idade dele é {busca['idade']}!')
else:
    print(f'A pessoa: {chave}, nao foi encontrada')
