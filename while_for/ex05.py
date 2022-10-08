a = float(input("Informe o tamanho da população A: "))
taxa = float(input("Informe a taxa de crescimento da população A: "))

b = float(input("Informe o tamanho da população B: "))
taxa1 = float(input("Informe a taxa de crescimento da população B: "))

ano = 0

while a < b:
    a = a + (a * taxa)
    b = b + (b * taxa1)
    ano = ano + 1
print("A população A se iguala ou ultrapassa a população B em", ano, "anos.")