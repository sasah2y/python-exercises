soma_idades = 0
mulheres_menos_20 = 0
nome_homem_mais_velho = ""
homem_mais_velho = 0
homens = 0

for i in range(4):
    print('{}ª Pessoa' .format(i+1))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    soma_idades += idade

    while sexo != "M" and sexo != "F":
        sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()

    if sexo == "M":
       if idade > homem_mais_velho:
           homem_mais_velho = idade
           nome_homem_mais_velho = nome

    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idades / 4


print('A média de idade do grupo é {} anos' .format(media_idade))
print('{} mulheres têm menos de 20 anos de idade.' .format(mulheres_menos_20))
print('O homem mais velho do grupo é o {}, e ele tem {} anos de idade.' .format(nome_homem_mais_velho, homem_mais_velho ))