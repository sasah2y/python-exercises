numeros_gerais = []
numeros_pares = []
numeros_impares = []

resposta = "S"
while resposta == "S":
    numero = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N]: ')).upper()
    numeros_gerais.append(numero)

    if numero % 2 == 0:
       numeros_pares.append(numero)
    else:
       numeros_impares.append(numero)

    
    if resposta == "N":
        break

print(numeros_gerais)
print(numeros_pares)
print(numeros_impares)