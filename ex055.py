pesos = []
for i in range(1, 6):
    peso = input('Peso da pessoa {}:' .format(i))
    pesos.append(peso)


maior_peso = max(pesos)
menor_peso = min(pesos)

print('O maior peso é {}' .format(maior_peso))
print('O menor peso é {}' .format(menor_peso))