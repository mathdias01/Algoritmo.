
def sum(n1):
    formula = int(n1*(n1+1)/2)
    soma = 0 
    operacoes = 0 
    for i in range(1, n1+1):
     soma+=i
     operacoes+=1
    
    print(f'A soma dos numeros que antecedem o (n) é: {soma}, e comparando com a formula temos:{formula} ')
    print(f'A quantidade de + é:{operacoes}')
  





n= int(input('Insira seu numero:'))
sum(n)
