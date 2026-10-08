import random

numero_sorteado = random.randint(1, 100) 

chute = int(input('Digite um número entre 1 e 100:'))

if chute == numero_sorteado:
   print('🎉 Parabéns! Você acertou o número secreto!')
else:
   print('❌ Errou! O número secreto era {}' .format(numero_sorteado))