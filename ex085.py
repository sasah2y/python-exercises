numeros = [[],[]]

for cont in range(1, 8):
    numero = int(input(f"Digite o {cont}º número: "))
    numeros.append(numero)

    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
   
numeros[0].sort()
numeros[1].sort()

print(numeros[0])
print(numeros[1])