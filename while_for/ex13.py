base = int(input("Informe a base: "))
expoente = int(input("Informe o expoente: "))

resultado = 1
variavel_auxiliar = False

if (expoente < 0):
    expoente = -1 * expoente
    variavel_auxiliar = True

for contador in range(expoente):
    resultado = resultado * base

if (variavel_auxiliar == True):
    print("Resultado:", 1/resultado)
else:
    print("Resultado:", resultado)

