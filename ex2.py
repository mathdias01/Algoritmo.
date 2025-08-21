
def password():
   senhaC = 'senha123'
   tentativas = 0
   senha = input('Insira sua senha:')


   while senha!= senhaC:
        tentativas+=1
        if tentativas == 3:
         print('Acesso bloqueado!')
         return
        senha = input('Insira sua senha:')
        
   
   else:
    print('Acesso liberado, Bem vindo!')
         
    

password()
