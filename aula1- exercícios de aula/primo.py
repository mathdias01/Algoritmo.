def primo(n1):
    if n1 == 1:
      print('Não é primo!')
      return
    for div in range (2, n1):
     if n1%div== 0:
       print('Não é primo!')
       break
    else:
     print('É primo!')


n = int(input('Insira seu numero:'))
primo(n)
    
        
        