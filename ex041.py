from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite seu ano de nascimento:'))

idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Você é mirim.')
elif idade <= 14:
    print('Você é infantil.')
elif idade <= 19:
    print('Você é Junior.')
elif idade <= 25:
    print('Você é senior')
else:
    print('Você é master.') 