ultimo = 1
penultimo = 0

print(penultimo)
print(ultimo)

contador = 3
while contador <= 500:
    termo = ultimo + penultimo
    penultimo = ultimo 
    ultimo = termo
    contador = contador + 1
    print(termo)