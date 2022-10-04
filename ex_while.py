n = int(input("Digite o valor de n: "))

numero = 2

while numero <= n:
    if (n % numero == 0):
        print(numero)
    numero = numero + 1