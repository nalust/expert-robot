"""numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite o terceiro e último número: "))

if(numero1 > numero2):
  if(numero1 > numero3):
    print("O maior número é", numero1)
else:
  if(numero2 > numero1 and numero2 > numero3):
    print("O maior número é", numero2)
  else:
    print("O maior número é", numero3) """


numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite o terceiro e último número: "))

if(numero1 > numero2 and numero1 > numero3) and (numero2 > numero3):
    print(numero1, numero2, numero3)
    if(numero3 > numero2):
        print(numero1, numero3, numero2)
if(numero2 > numero1 and numero2 > numero3) and (numero1 > numero3):
    print(numero2, numero1, numero3)
    if(numero3 > numero1):
        print(numero2, numero3, numero1)
if(numero3 > numero1 and numero3 > numero2) and (numero1 > numero2):
    print(numero3, numero1, numero2)
else:
    if (numero2 > numero1):
        print (numero3, numero2, numero1)
    
    
