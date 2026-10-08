
valores = []

for i in range(1, 6):
   valor = int(input(f'Digite o {i}º valor: '))

   if i == 1 or valor > valores[-1]:
       valores.append(valor)
   else:
     pos = 0
     while pos < len(valores):
         if valor <= valores[pos]:
             valores.insert(pos, valor)
     
         break
     pos += 1
   while valor in valores:
      valor = input('Digite outro valor, por favor: ')
      valores.append(valor)


print(valores)
