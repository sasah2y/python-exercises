lista = []

lista.append(int(input('Digite o valor: ')))


print('Valor adicionado com sucesso...')
resposta = str(input('Quer continuar: [S/N]')).upper()

while resposta == "S":
     valor = (int(input('Digite o valor: ')))

     if valor not in lista:
          lista.append(valor)
          print('Valor adicionado com sucesso...')
          resposta = str(input('Quer continuar: [S/N]')).upper()
     else:
          print('Este valor já está presente na lista, logo não pode ser adicionado novamente.')
          resposta = str(input('Quer continuar: [S/N]')).upper()
     
if resposta == "N":
    lista.sort()
    print(f'Você digitou os valores: {lista}')