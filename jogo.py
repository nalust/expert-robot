jogador1 = input("Jogador 1 digite pedra, papel ou tesoura: ")
jogador2 = input("Jogador 2 digite pedra, papel ou tesoura: ")

if jogador1 == jogador2:
    print("Empate! Ninguém ganhou.")
elif (jogador1 == "pedra" and jogador2 == "tesoura") or\
    (jogador1 == "tesoura" and jogador2 == "papel") or\
    (jogador1 == "papel" and jogador2 == "pedra"):
        print("Jogador 1 ganhou!")
else:
    print("Jogador 2 ganhou!")