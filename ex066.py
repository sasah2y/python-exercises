parar = 999
contador = 0
caixa = 0
while True:
   num = int(input('Digite um valor (999 para parar): '))

   if num == parar:
       break
 
   contador += 1 
   caixa += num 
   print('A soma dos valores {} foi {}' .format(contador, caixa))