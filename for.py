lista_numeros = [1, 2, 3, 4, 5]

for numero in lista_numeros:
    print(numero)

numero = 1

"""
while numero < 100:
    numero = numero + 1
    print(numero)
"""

for numero in range (1, 101):
    print(numero)

for numero in range (0, 13, 2): # espaço entre um e outro elemento
    print(numero)

# for é utilizado quando se tem o número máximo de iterações que se precisa executar;
# while: enquanto uma condição for verdadeira (condição indefinida).

# VARIÁVEL ACUMULADORA

"""
n = int(input("Digite o valor de n: "))

acumuladora = 0


for numero in range (n):
    aux = int(input())
    acumuladora = acumuladora + aux
print("A soma é", acumuladora)
"""

# BREAK: termina a execução de um laço, passando para o próximo comando depois do final
# do laço.

for numero in range (1, 11):
    if (numero >= 5):
        break
    print(numero)
print("Terminou o laço.")

# CONTINUE: faz com que a execução de um laço seja alterada para o final do laço.

numero = 1

while numero <= 10:
    if (numero == 5):
        numero = numero + 1
        continue
    print(numero)
    numero = numero + 1
print("Terminou o laço.")