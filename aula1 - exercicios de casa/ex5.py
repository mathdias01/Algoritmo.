def verify_num(cpf):
    if cpf.isdigit() and len(cpf) == 11:
        return True
    else:
      return False 
    
        





num = input('Insira seu cpf(11 digitos/apenas os numeros):')
if verify_num(num) :
    print('CPF Valido!')
else:
    print('CPF Invalido!')