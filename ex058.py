import random

numeroSorteado = random.randint(0, 10)
numeroUser = int(input('''Tente adivinhar o número que eu escolhi...
Digite um número de 0 a 10:   '''))

while numeroUser != numeroSorteado:
    if numeroSorteado > numeroUser:
        numeroUser = int(input('O número que foi sorteado é maior, tente mais uma vez:  '))
    else:
        numeroUser = int(input('O número que foi sorteado é menor, tente mais uma vez:  '))

print('FINALMENTE!!!!!!! O número é {}' .format(numeroSorteado))