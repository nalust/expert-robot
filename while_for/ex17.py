fatorial = int(input("Informe o número que deseja saber o fatorial: "))

contador = 1
resultado = 1

while contador <= fatorial:
    resultado = resultado * contador
    contador = contador + 1
print(resultado) 