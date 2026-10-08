import random 

numeros_tupla = tuple(random.randint(1, 100) for _ in range(5))

menor_numero = min(numeros_tupla)
maior_numero = max(numeros_tupla)

print('Os números sorteados são: {}'.format(numeros_tupla))
print('O maior dentre eles é {}' .format(maior_numero))
print('O menor dentre eles é {}' .format(menor_numero))