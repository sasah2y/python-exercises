valorCasa = float(input('Qual o valor da casa que você deseja comprar?'));
valorSalário = float(input('Qual o valor do seu salário mensal?'));
anos = float(input('Em quanto tempo você pretende pagar essa casa?'));
prestacao = valorCasa / (anos * 12)

if prestacao < valorSalário * 0.3:
    print('Empréstimo aprovado! A prestação será de R$ {:.2f} por mês' .format(prestacao))

else:
    print('Empréstimo negado! A prestação de R$ {:.2f} ultrapassa 30% do seu salário.' .format(prestacao))