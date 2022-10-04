import math

a = int(input("Insira o primeiro número da equação: "))
b = int(input("Insira o segundo número da equação: "))
c = int(input("Insira o terceiro e último número da equação: "))

delta = b ** 2 -4 * a * c

if delta < 0:
  print("Essa equação não possui raízes reais.")
else:
  x1 = (-b + math.sqrt(delta)) / (2 * a)


if delta == 0:
  print("A única raiz é:", x1)
else:
  x2 = (-b - math.sqrt(delta)) / (2 * a)
  print("A primeira raiz é: ", x1)
  print("A segunda raiz é: ", x2)



