print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('O segmentos acima não podem formar um triângulo.')