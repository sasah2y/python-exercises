import random

numeroSorteado = random.randint(0, 5)
numeroUser = int(input('Digite um número entre 0 e 5: '))

if numeroUser == numeroSorteado:
    print('Parabéns, você acertou no jogo do número secreto!')
else:
    print('Poxa, você errou o número secreto! O número sorteado foi {}' .format(numeroSorteado))