try:
    print('=== AREA DE TRANSFERENCIAS ===')
    saldo = int(input('Insira seu saldo atual: '))
    valorTransf = int(input('Insira o valor da transferencia: '))
    if valorTransf < saldo:
        print('Saldo suficiente, operação em andamento...')
    else:
        raise ValueError
except ValueError:
    print('Saldo insuficiente!')
else:
    print('transferência finalizada!')
finally: 
    print('fechando transferencia...')