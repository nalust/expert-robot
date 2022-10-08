a = float(input("Informe o primeiro número: "))
b = float(input("Informe o segundo número: "))
c = float(input("Informe o terceiro número: "))
d = float(input("Informe o quarto número: "))
e = float(input("Informe o quinto número: "))

if (a > b) and (a > c) and (a > d) and (a > e):
    print("O maior número é", a)
elif (b > a) and (b > c) and (b > d) and (b > e):
    print("O maior número é", b)
elif (c > a) and (c > b) and (c > d) and (c > e):
    print("O maior número é", c)
elif (d > a) and (d > b) and (d > c) and (d > e):
    print("O maior número é", d)
else:
    print("O maior número é", e)