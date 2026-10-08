numeros = []

resposta = "S"
while resposta == "S":
   numero = int(input("Digite um número: "))
   numeros.append(numero)
   resposta = str(input("Quer continuar? [S/N]")).upper()
   if resposta == "N":
      break

decrescente = sorted(numeros, reverse=True)

print('-'*40)
print(f"Você digitou {len(numeros)} elementos.")
print(f"Os valores em ordem decrescente são {decrescente}")
if 5 in numeros: 
   print("O número 5 faz parte da lista!")
else:
   print("O número 5 não faz parte da lista")