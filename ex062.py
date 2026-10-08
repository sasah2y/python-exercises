print('Gerador de PA')

primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão da PA:'))

contador = 0
i = 0

while i < 10:
    termo = primeiro + i * razão
    print(termo, end=' → ')
    i += 1
    
print('PAUSA...')

res = int(input('Quantos termos você quer mostrar a mais? '))

if res != 0:
    total = i + res
    i = 0
    while i < total:
        termo = primeiro + i * razão
        print(termo, end=' → ')
        i += 1
        contador += 1

print('PAUSA')