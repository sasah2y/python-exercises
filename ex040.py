nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))

media = (nota1 + nota2) / 2

if 7 > media >= 5:
    print('Você foi recuperação')
elif media < 5:
    print('Você foi reprovado')
else:
    print('Você foi aprovado')