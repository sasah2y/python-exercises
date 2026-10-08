from math import sqrt

número = int(input('Digite um número inteiro:'))

if número <= 1 :
    print('{} não é um número primo.' .format(número))

i = 2
while i <= sqrt(número):
    i+=1
    if número % i == 0 :
        print('{} não é um número primo.' .format(número))
    else:
        print('{} é um número primo.' .format(número))
    
