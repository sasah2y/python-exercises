print('10 termos de uma PA')
print('-' *40)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

for i in range(10):
    termo = primeiro + i * razão
    print(termo, end=' → ')

print('Acabouu...')