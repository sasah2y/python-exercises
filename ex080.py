valores = []

for i in range(1, 6):
   valor = int(input(f'Digite o {i}º valor: '))

   while valor in valores:
     valor = int(input("Digite outro valor, por favor: "))

   pos = 0
   while pos < len(valores) and valor > valores[pos]:
      pos += 1

   valores.insert(pos, valor)

print(valores)
