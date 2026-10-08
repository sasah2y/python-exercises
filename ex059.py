n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

opção = 0

while opção != 5:
  opção = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
>>>>>> Qual é a sua opção?'''))
  if opção == 1:
        soma = n1 + n2 
        print('A soma de {} e {} tem como resultado {}.' .format(n1, n2, soma))
  elif opção == 2:
        multi = n1 * n2
        print('A multiplicação de {} e {} tem como resultado {}.' .format(n1, n2, multi))
  elif opção == 3:
       if n1 > n2:
            print('{} é maior que {}' .format(n1, n2))
       elif n1 < n2:
            print('{} é maior que' .format(n2, n1))
       else:
            print('São os mesmos números.')   
  elif opção == 4:
       print('Informe os novos números: ')
       n1 = int(input('Digite o primeiro valor: '))
       n2 = int(input('Digite o segundo valor: '))

  else:
       print('Opss... opção inválida.')


if opção == 5:
   print('Saindo do programa.') 