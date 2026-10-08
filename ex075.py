v1 = int(input("Digite um número: "))
v2 = int(input("Digite outro número: "))
v3 = int(input("Digite mais um número: "))
v4 = int(input("Digite só mais um número: "))

valores = (v1, v2, v3, v4)
#print dos valores digitados
print("Você digitou os valores: {}" .format(valores))

#quantas vezes aparece o número nove
nove = 9
ocorrencias = valores.count(nove)
print("O número {} aparece {} vezes." .format(nove, ocorrencias))

#posição do primeiro três
while True:
   if 3 in valores:
     posicao = valores.index(3)
     print("O número 3 aparece pela primeira vez na {}º posição" .format(posicao+1))
     break
 

#números pares
pares = []

for x in valores:
    if x % 2 == 0:
        pares.append(x)

resultado = tuple(pares)

print("Os valores pares digitados são {}." .format(pares))