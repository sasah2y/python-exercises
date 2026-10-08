contador = 0
soma = 0

maior = None
menor = None

while True:
    num = int(input('Digite um número: '))
    contador += 1
    soma += num

    if contador == 1:
      maior = menor = num
    else:
       if num > maior:
            maior = num
       if num < menor:
           menor = num

    media = soma / contador
    
    resp = str(input('Quer continuar? [S/N]')).upper()
    if resp == "N":
        break


print('Você digitou {} números e a média foi {}' .format(contador, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))