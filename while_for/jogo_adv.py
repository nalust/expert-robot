import random

numero = random.randrange (1, 101)

palpites = 0
meu_palpite = int(input("Adivinhe meu número entre 1 e 100: "))

while meu_palpite != numero:
    if meu_palpite == 0:
        print("Ah, que pena! Você desistiu do jogo.")
        break
    else:
        palpites = palpites + 1
        if meu_palpite > numero:
            print(meu_palpite, "está acima.")
        elif meu_palpite < numero:
            print(meu_palpite, "está abaixo.")
        meu_palpite = int(input("Digite 0 para desistir ou tente novamente: "))
if meu_palpite != 0:
    print ("\nÓtimo, você acertou em", palpites, "tentativas!")

    
