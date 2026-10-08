parar = 999
contador = 0
caixa = 0 
num = 0

while num != parar:
   num = int(input('Digite um número 999 para parar: '))
   contador += 1
   if num != parar:
     caixa += num
   

print('Você digitou {} números e a soma deles foi {}.' .format(contador,caixa))