numero = 1

while numero <= 100:
    print(numero)
    numero = numero + 1

# estrutura vai ser>
# while condição:
    # comandos

#while a != a:
    #a = a + 1

# Se a condição for falsa, ele nunca entra no laço de repetição;
# Se for sempre verdadeira, ele entra no loop infinito.

# Ao final do while podemos usar else:

""" 
While condição:
    comando(s)
else:
    comando(s)
"""
# EXEMPLO:

n = int(input("Informe um número: "))

numero = 1

while numero <= n:
    print(numero)
    numero = numero + 1
else:
    print("Fim.")

# LISTAS:

lista1 = [10, 20, 30, 40]
lista2 = ["programação", "mc102", "python"]
lista3 = ["oi", 2.0, 5, [10, 20]]

print(lista3[0])