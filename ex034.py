salario = float(input('Quanto o salário do funcionário? R$'))

if salario > 1250.00:
    aumento = salario + (salario * 0.1)
    print('O salário que era R${}, agora passa a ser R${}.' .format(salario, aumento))
if salario <= 1250.00:
    aumento = salario + (salario * 0.15)
    print('O salário que era R${}, agora passa a ser R${}.'.format(salario, aumento))