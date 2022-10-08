from re import I


a = int(input("Informe um número: "))
b = int(input("Informe outro número: "))

for i in range (a + 1, b):
    print(i)

for i in range (a, b + 1):
    print(i)
print("A soma dos números é", i + i)