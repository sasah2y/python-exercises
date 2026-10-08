valor = int(input('Digite o valor: '))

print('Cédulas de 100:', valor // 100)
valor = valor % 100
print('Cédulas de 50:', valor // 50)
valor = valor % 50
print('Cédulas de 20', valor // 20)
valor = valor % 20 
print('Cédulas de 10:', valor // 10)
valor = valor % 10
print('Cédulas de 5:', valor // 5)
valor = valor % 5
print('Cédulas de 1:', valor // 1)