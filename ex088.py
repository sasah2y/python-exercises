import random

games = []

print('-'*30)
print('     JOGA NA MEGA SENA')
print('-'*30)

total_games = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'==== SORTEANDO {total_games} JOGOS ====')

for jogos in range(total_games):

   numbers = random.sample(range(1, 61), 6)
   games.append(numbers)     

for numbers, jogos in enumerate(games, start=1):
   print(f'Jogo {numbers}: {jogos}')

print('====< BOA SORTE! >====')