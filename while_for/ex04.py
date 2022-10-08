a = 8000
b = 20000
ano = 0

while a < b:
    a = a + a * 0.03
    b = b + b * 0.015
    ano = ano + 1
print("A população A se iguala ou ultrapassa a população B em", ano, "anos.")