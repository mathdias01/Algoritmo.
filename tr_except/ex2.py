try:
    cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}
    cor = input('Insira a cor que deseja ver o valor em RGB: ')
    rgb = cores.get(cor)

    if rgb:
        print(f'Valor em RGB de {cor}: {rgb}')
    else:
        print('Cor não existente!')
except KeyError:
    print('Cor não existente!')