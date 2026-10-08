frase = str(input('Digite uma frase:')).strip()
minus = frase.lower()
sem_espaços = minus.replace(" ", "")
invertido = sem_espaços[::-1]

if sem_espaços == invertido:
    print('{} temos um palíndromo.' .format(invertido))
else:
    print('{} não temos um palíndromo.' .format(invertido))
