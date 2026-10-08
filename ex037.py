num = int(input('Digite um número inteiro:'))
opção = int(input('''
Escolha a base de conversão:         
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal'''))

if opção == 1 :
   binário = bin(num)
   print('Em binário: {}'.format(binário)) 