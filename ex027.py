nome = str(input('Digite seu nome completo: '))

partes = nome.split()
primeiro = partes[0]
ultimo = partes[-1]

print('''Nome: {}
Primeiro: {}
Último: {}''' .format(nome, primeiro, ultimo))