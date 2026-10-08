print('-' *40)
print('Sequência de Fibonacci')
print('-' *40)

num = int(input('Quantos termos você quer mostrar? '))

a = 0 
b = 1

contador = 0 

while contador < num:
    print(a, end=' → ')
    proximo = a + b 
    a = b
    b = proximo
    contador += 1


print('Fim')