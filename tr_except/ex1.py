try:
    numero1 = int(input('Insira o numero(1): '))
    numero2 = int(input('Insira o numero(1): '))
    divisao = numero1/numero2
    print(divisao)
except ZeroDivisionError:
    print('Erro de divisão por zero!')
except ValueError:
    print('Insira apenas numeros!')
finally:
    print('operação finalizada!')
    



    