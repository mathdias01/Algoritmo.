def buscar_nome(nome_procurado, lista_nomes):
   for posicao, nome in enumerate(lista_nomes): 
     if nome == nome_procurado:
      return posicao
   
   return -1


nomes = ['Luiz','Matheus','Lucas','Julia']
busca = input('insira o nome que você busca:')
posicao_encontrada = buscar_nome(busca, nomes)

if posicao_encontrada != -1:
  print(f'O nome foi encontrado, e a posicao é {posicao_encontrada}!')
else:
  print('O nome nao foi encontrado!')
