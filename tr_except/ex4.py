class senhaInvalidaError(Exception):
    pass


def verificadorSenha():
    senha = input('Insira a senha de no minimo 8 digitos e pelo menos um numero: ')
    if len(senha) < 8:
        raise senhaInvalidaError('A senha deve ter no minimo 8 digitos!')
    if not any(char.isdigit() for char in senha):
        raise senhaInvalidaError('A senha deve ter ao minimo, um numero!')

    return senha



try:
    verificadorSenha()
except senhaInvalidaError as erro:
    print(f'Erro: {erro}')
else:
    print('Senha valida!')
finally:
    print('operação finalizada!')
    

