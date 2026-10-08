from datetime import date

atual = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
    ano_nascimento = int(input('Em que ano a {} pessoa nasceu? '.format(i)))
    idade = atual - ano_nascimento
    if idade >= 18:
       maior += 1
    else:
       menor += 1

print('''Ao todo tivemos {} pessoas maiores de idade
E também tivemos {} pessoas menores de idade.''' .format(maior, menor))