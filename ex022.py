nome = str(input('Digite seu nome completo:'))

nomeUpper = nome.upper()
nomeLower = nome.lower()
nomeJunto = "".join(nome.split())
nomeCont = len(nomeJunto)
parteNome = nome.split()
primeiroNome = parteNome[0]
primeiroNomeJunto = "".join(nome.split())
primeiroNomeCont = len(primeiroNome)

print('''Este é seu nome em maiúsculas: {}
Este é seu nome em minúsculas: {}
Esta é a quantidade de letras do seu nome: {}
Seu primeiro nome é {} e ele tem {} letras'''.format(nomeUpper, nomeLower, nomeCont, primeiroNome, primeiroNomeCont))