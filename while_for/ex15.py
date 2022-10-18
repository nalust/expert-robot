n = int(input("Informe o termo que deseja encontrar: "))

ultimo = 1
penultimo = 1

if (n == 1) or (n == 2):
    print("1")
else:
    contador = 3
    while contador <= n:
        termo = ultimo + penultimo
        penultimo = ultimo 
        ultimo = termo
        contador = contador + 1
    print(termo)