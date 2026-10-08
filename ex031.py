distancia = float(input('Digite a distancia da sua viagem em quilômetros:'))

if distancia <= 200:
    passagem = distancia * 0.50
    print('Sua passagem custa R${:.2f}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('Sua passagem custa R${:.2f}'.format(passagem))
