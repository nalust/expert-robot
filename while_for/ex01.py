nota = float(input("Informe sua nota (0 a 10): "))

while (nota > 10) or (nota < 0):
    nota = float(input("Valor inválido. Por favor, informe um valor entre 0 e 10: "))