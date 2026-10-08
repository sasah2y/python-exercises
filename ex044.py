preço_das_compras = float(input('Digite o preço total das compras: R$'))
print('''FORMAS DE PAGAMENTO
 [ 1 ] à vista dinheiro/cheque
 [ 2 ] à vista cartão   
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão.''')
opção = int(input('Qual é a opção? '))

if opção == 1:
  desconto10 = preço_das_compras * 0.10
  preço_final = preço_das_compras - desconto10

  print('Sua compra de R${} vai custar R${} no final.' .format(preço_das_compras, preço_final))
elif opção == 2:
  desconto5 = preço_das_compras * 0.05
  preço_final2 = preço_das_compras - desconto5
  print('Sua compra de R${}, vai custar R${}' .format(preço_das_compras, preço_final2))
elif opção == 3:
    print('Sua compra vai custar R${}' .format(preço_das_compras))
else:
  parcelas = int(input('Quantas parcelas?'))
  juros = preço_das_compras * 0.20
  preço_final4 = preço_das_compras + juros
  preço_parcelas = preço_final4 / parcelas
  print('Sua compra foi parcelada em {}x de R${} com juros' .format(parcelas, preço_parcelas ))
  print('Sua compra de R${} vai custar R${} no final.' .format(preço_das_compras, preço_final4))