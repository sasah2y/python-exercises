lista = []
aberto = fechado = 0

expressão = str(input('Digite a expressão: '))

if expressão == "(":
    aberto += 1
elif expressão == ")":
    fechado += 1

if aberto == fechado:
    lista.append(expressão)
    print(f'A espressão {lista} está correta!')
else:
    print(f'A expressão {lista} está incorreta, verifique os parênteses.')