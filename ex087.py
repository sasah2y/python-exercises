
#cria a matriz
matriz = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

numeros_pares = []
numeros_linha2 = []
numeros_coluna3 = []

for linha in range(3):
    for coluna in range(3):
        posicao = (linha, coluna)
        num = int(input(f'Digite um número para {posicao}: '))

        matriz[linha][coluna] = num
       #identifica valores pares 
 
        if num % 2 == 0:
            numeros_pares.append(num)

        if  linha == 1:
            numeros_linha2.append(num)
            
        if coluna == 2:
            numeros_coluna3.append(num)

       
soma_coluna3 = sum(numeros_coluna3)
soma_pares = sum(numeros_pares)
maior_linha2 = max(numeros_linha2)

print("Ficou assim a sua matriz:")

for lin in matriz:
    print(lin)

print(f"A soma dos valores pares é {soma_pares}.")
print(f"A soma dos valores da terceira coluna é {soma_coluna3}.")
print(f"O maior número da segunda coluna é {maior_linha2}")