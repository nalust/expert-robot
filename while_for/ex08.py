# a = float(input("Informe o primeiro número: "))
# b = float(input("Informe o segundo número: "))
# c = float(input("Informe o terceiro número: "))
# d = float(input("Informe o quarto número: "))
# e = float(input("Informe o quinto número: "))

# soma = a + b + c + d + e
# media = (a + b + c + d + e) / 5

# print("A soma dos números é", soma, ". A média dos números é", media, ".")

soma = 0
for numero in range(5):
    print("Informe o número", numero + 1)
    valor = float(input())
    soma = soma + valor

media = soma/5
print("A soma dos números é", soma, ". A média dos números é", media, ".")
