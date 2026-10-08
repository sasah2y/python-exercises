print('Gerador de PA')

primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão da PA:'))

i = 0
while i < 10:
    termo = primeiro + i * razão
    print(termo, end=' → ')
    i += 1
    
print('Acabouu...')