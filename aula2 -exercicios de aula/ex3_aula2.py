""" Estudo de Caso 3  Analisando números pares e ímpares
Enunciado:
Escreva um programa que:
1. Receba 10 números inteiros digitados pelo usuário.
2. Separe-os em duas listas: pares e ímpares.
3. Exiba quantos números pares e ímpares foram digitados. """

par = []
impar = []

def par_impar(par, impar):
    for numeros in range(10):
     numeros = int(input('insira seu numero:'))
     if numeros % 2 == 0:
        par.append(numeros)
     else:
       impar.append(numeros)
    return par, impar 
    
    
    
par_impar(par, impar)
print(f'A lista de numeros par é {par} e a lista de números ímpar é {impar}. ')
       


