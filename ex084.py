pessoas = list()
peso = list()
maiores_peso = list()
menores_peso = list()

resposta = 'S'
while resposta == 'S':
   pessoas.append(str(input('Nome: ')))
   peso.append(float(input('Peso: ')))

   resposta = str(input('Quer continuar? [S/N] ')).upper()
   
   if resposta == 'N':
     break

maior_peso = max(peso)
menor_peso = min(peso)

cont1 = 0 
while cont1 < len(peso):
   if peso[cont1] == maior_peso:
      maiores_peso.append(pessoas[cont1])

   cont1+=1

cont2 = 0
while cont2 < len(peso):
   if peso[cont2] == menor_peso:
      menores_peso.append(pessoas[cont2])

   cont2+=1

print('-='*40)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso}. Peso de {maiores_peso}')
print(f'O o menor peso foi {menor_peso}. Peso de {menores_peso}.')