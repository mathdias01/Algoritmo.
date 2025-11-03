try:
    numero = int(input('Numero:'))
    if numero > 10:
        print('O numero é valido')
    elif numero < 10:
        print('Numero invalido!')
except ValueError:
    print('Insira apenas numeros')
else:
    print('Programa executado com sucesso!')
finally:
    print('Programa encerrado')