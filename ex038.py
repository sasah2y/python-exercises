num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))

if num1 > num2:
    print('{} é maior que {}' .format(num1, num2))
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais.')
elif num1 < num2:
    print('{} é maior que {}' .format(num2, num1))