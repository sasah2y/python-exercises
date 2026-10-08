print('-' *24)
print('  CADASTRE UMA PESSOA')
print('-' *24)

homens = 0
mulheres_mais20 = 0
pessoas_mais18 =  0

while True:
   idade = int(input('Idade:'))
   sexo = str(input('Sexo: [M/F] ')).upper()

   while sexo != "M" and sexo != "F":
     sexo = str(input('Digite o seu sexo: [M/F] ')).upper()
   
   print('-' *24)
   
   resp = str(input('Quer continuar? [S/N] ')).upper()

   while resp != "S" and resp != "N":
     resp = str(input('Quer continuar? [S/N] ')).upper()

   print('-' *24)

   if idade >= 18:
      pessoas_mais18 += 1

   if sexo == "M":
      homens += 1 

   if sexo == "F" and idade > 20:
      mulheres_mais20 += 1
   if resp == "N":
      break

print('Total de pessoas com mais de 18 anos: {}' .format(pessoas_mais18))
print('Ao todo temos {} homem(ns) cadastrados.' .format(homens))
print('E temos {} mulher(es) com menos de 20 anos de idade.' .format(mulheres_mais20))