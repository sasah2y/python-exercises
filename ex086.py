matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for linha in range(3):
    for coluna in range(3):
        posicao = (linha, coluna)
        num = int(input(f'Digite um número para a posição {posicao}: '))
        
        matriz[linha][coluna] = num

for lin in matriz:
    print(lin)