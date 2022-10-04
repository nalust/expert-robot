a = float(input("Informe o valor do maior lado do triângulo: "))
b = float(input("Informe o valor de outro lado do triângulo: "))
c = float(input("Informe o valor do último lado do triângulo: "))

# É possivel ordernar a entrada para dar match com o exemplo do SuSy

if (a <= 0) or (b <= 0) or (c <= 0) or\
    (a >= b + c) or (b >= a + c) or (c >= a + b):
    print("Valores inválidos na entrada.")
else:
    # Classificacao Quanto aos Angulos
    classificacao_angulo = ""
    if (a ** 2) < (b ** 2) + (c ** 2):
        classificacao_angulo = "acutangulo"
    elif (a ** 2) == (b ** 2) + (c ** 2):
        classificacao_angulo = "retangulo"
    elif (a ** 2) > (b ** 2) + (c ** 2):
        classificacao_angulo = "obtusangulo"
    
    # Classificacao Quanto aos Lados
    if (a == b) and (b == c) and (a == c):
        print("Triângulo equilátero.")
        print("Triângulo", classificacao_angulo)
    elif (a == b) or (b == c) or (a == c):
        print("Triângulo isósceles.")
        print("Triângulo", classificacao_angulo)
    else:
        print("Triângulo escaleno.")
        print("Triângulo", classificacao_angulo)
    