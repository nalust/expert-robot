a = float(input("Informe o valor do maior lado do triângulo: "))
b = float(input("Informe o valor de outro lado do triângulo: "))
c = float(input("Informe o valor do último lado do triângulo: "))


if (a == 0) or (b == 0) or (c == 0) or\
    (a >= b + c) or (b >= a + c) or (c >= a + b) or\
    (a < 0) or (b < 0) or (c < 0):
        print("Valores inválidos na entrada.")
elif (a != b) and (a != c) and (b != c):
    print("Triângulo escaleno.")
    if (a ** 2) < (b ** 2) + (c ** 2):
        print("Triângulo acutângulo.")
    else:
        if (a ** 2) > (b ** 2) + (c ** 2):
            print("Triângulo obtusângulo.")
        else:
            (a ** 2) == (b ** 2) + (c ** 2)
            print("Triângulo retângulo.")
elif (a == b) and (a == c) and (b == c):
    print("Triângulo equilátero.")
    (a ** 2) < (b ** 2) + (c ** 2)
    print("Triângulo acutângulo.")
else:
    (a == b) or (a == c) or (b == c)
    print("Triângulo isósceles.")
    if (a ** 2) < (b ** 2) + (c ** 2):
        print("Triângulo acutângulo.")
    else:
        (a ** 2) > (b ** 2) + (c ** 2)
        print("Triângulo obtusângulo.")





















