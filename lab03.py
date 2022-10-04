tosse = input("Está tossindo? ")
febre = input("Teve ou está com febre? ")
falta_ar = input("Está com dificuldade para respirar? ")

tosse1 = tosse == "True"
temperatura = febre == "True"
respiracao = falta_ar == "True"

covid = tosse1 and temperatura and respiracao 

print("Tosse:", tosse1)
print("Febre:", temperatura)
print("Dificuldade para respirar", respiracao)
print("Provavelmente é covid-19:", covid)