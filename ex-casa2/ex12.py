import random

def jogo_adivinha():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("🎯 Tente adivinhar o número entre 1 e 100!")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
            break
        elif palpite < numero_secreto:
            print("🔼 O número secreto é MAIOR.")
        else:
            print("🔽 O número secreto é MENOR.")


jogo_adivinha()

