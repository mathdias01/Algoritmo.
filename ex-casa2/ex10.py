def busca_primeira_ocorrencia(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            resultado = meio
            fim = meio - 1  # continua buscando à esquerda
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1

    return resultado


def busca_ultima_ocorrencia(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            resultado = meio
            inicio = meio + 1  # continua buscando à direita
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1

    return resultado


def localizar_intervalo(lista, chave):
    primeiro = busca_primeira_ocorrencia(lista, chave)
    ultimo = busca_ultima_ocorrencia(lista, chave)

    if primeiro == -1:
        return None  # chave não encontrada
    return (primeiro, ultimo)


# Exemplo de uso
lista = [1, 2, 2, 2, 3, 4]
chave = 2

intervalo = localizar_intervalo(lista, chave)

if intervalo:
    print(f"O número {chave} aparece do índice {intervalo[0]} até {intervalo[1]}.")
else:
    print(f"O número {chave} não foi encontrado.")