times = (
    "Flamengo",
    "Palmeiras",
    "Athletico-PR",
    "Fluminense",
    "Bahia",
    "Cruzeiro",
    "Coritiba",
    "Atlético-MG",
    "Red Bull Bragantino",
    "São Paulo",
    "Corinthians",
    "Santos",
    "Botafogo",
    "Vitória",
    "Grêmio",
    "Mirassol",
    "Vasco da Gama",
    "Internacional",
    "Remo",
    "Chapecoense"
)

#tabela no geral
print('-='*60)
print("TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL:")
print(times)
print('-'*60)

#5 primeiros
print("Os 5 primeiros:")
print(times[0:5])
print('-'*60)

#últimos 4 
print("Os últimos 4:")
print(times[-4:])
print('-'*60)

times_ordenados = tuple(sorted(times))

#ordem alfabética
print("Em ordem alfabética:")
print(times_ordenados)
print('-'*60)

#posição chapecoense
print("O chapecoense está na 20º posição")