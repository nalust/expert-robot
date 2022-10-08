nome = input("Informe seu nome: ")

while (len(nome) <= 3):
    nome = input("O nome não pode conter 3 ou menos caracteres. Informe seu nome: ")

idade = int(input("Informe sua idade: "))

while (idade <= 0) or (idade >= 150):
    idade = int(input("Idade inválida. Por favor, informe sua idade: "))

salario = float(input("Informe seu salário: "))

while salario <= 0: 
    salario = float(input("Valor inválido. Por favor, informe seu salário: "))

sexo = input("Informe a inicial do seu sexo: ")

while (sexo != "f") and (sexo != "m"):
    sexo = input\
        ("Informação inválida.Por favor, informe a inicial do seu sexo (m ou f): ")

estado_civil = input("Informe a inicial do seu estado civil: ")

while (estado_civil != "s") and (estado_civil != "c") and\
     (estado_civil != "v") and (estado_civil != "d"):
     estado_civil = input\
        ("Informação inválida. Por favor, informe a inicial do seu estado civil: ")