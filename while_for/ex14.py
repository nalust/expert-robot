pares = 0
impares = 0

for numero in range(1, 11):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print("Pares:", pares, "\nÍmpares:", impares)