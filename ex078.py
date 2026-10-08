lista = []

for i in range(5):
    lista.append(input('Digite um valor para a Posição {}:' .format(i)))

print('=-'*17)
print('Você digitou os valores: '.format(lista))

maior_valor = max(lista)
menor_valor = min(lista)

posicoes_maiores = []
for i, v in enumerate(lista):
    if v == maior_valor:
        posicoes_maiores.append(i)

posicoes_menores = []
for i, v in enumerate(lista):
    if v == maior_valor:
        posicoes_menores.append(i)

print(f"O maior valor digitado foi {maior_valor} nas posições {posicoes_maiores}")
print(f"O menor valor digitado foi {menor_valor} nas posições {posicoes_menores}")