from random import randint

numero = randint(0,10)

print('=-' *15)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('=-' *15)

quantidade = 0

while True:
    numUser = int(input('Diga um valor: '))
    chute = str(input('Par ou Ímpar? [P/I] ')).upper()
    
    while chute != "P" and chute != "I":
       chute = str(input('Par ou Ímpar? [P/I] ')).upper()
       
    print('-' *30)

    soma = numUser + numero
    if soma % 2 == 0:
        quantidade += 1
        print('-' *30)
        print('Você jogou {} e o computador {}. Total de {} DEU PAR!' .format(numUser, numero, soma))
        print('-' *30)
        print('''VOCÊ VENCEU
Vamos jogar novamente...''')
        print('-' *30)
    else:
        print('-' *30)
        print('Você jogou {} e o computador {}. Total de {} DEU ÍMPAR!' .format(numUser, numero, soma))
        print('-' *30)
        print('VOCÊ PERDEU!')
        print('GAME OVER! Você venceu {} vez(es)' .format(quantidade))
        break