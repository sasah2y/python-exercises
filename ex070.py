print('-'*24)
print('   LOJA SUPER BARATÃO')
print('-'*24)


total = 0
milzin = 0

menor_preco = 0
produto_barato = ""

contador = 0

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    total += preco

    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == "N":
        break   

    contador += 1 

    if preco >= 1000:
       milzin += 1

    if contador == 1:
        menor_preco = preco
        produto_barato = produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            produto_barato = produto


print('-------- FIM DO PROGRAMA --------')
print('O total da compra foi R${}' .format(total))
print('Temos {} produtos custando mais de R$1000.00' .format(milzin))
print('O produto mais barato foi a(o) {} que custa R${}' .format(produto_barato, menor_preco))