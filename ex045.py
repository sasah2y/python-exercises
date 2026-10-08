import random 

opções = ['pedra', 'papel', 'tesoura']
escolha_computador = random.choice(opções)

print('''
  Suas opções:
  [ 0 ] Pedra
  [ 1 ] Papel
  [ 2 ] Tesoura 
 ''')

escolha_user = int(input('Escolha uma opção:'))

if escolha_computador == 0:
    if escolha_user == 0 :
      print('''
      -----------------------
       Computador jogou pedra
      -----------------------
       EMPATE!''') 
    elif escolha_user == 1:
      print('''
      -----------------------
       Computador jogou pedra
      -----------------------
       VOCÊ GANHOU!''') 
    elif escolha_user == 2:
      print('''
      -----------------------
       Computador jogou pedra
      -----------------------
       COMPUTADOR GANHOU!''') 
elif escolha_computador == 1:
    if escolha_user == 0 :
      print('''
      -----------------------
       Computador jogou papel
      -----------------------
       COMPUTADOR GANHOU!''') 
    elif escolha_user == 1:
      print('''
      -----------------------
       Computador jogou papel
      -----------------------
       EMPATE!''') 
    elif escolha_user == 2:
      print('''
      -----------------------
       Computador jogou papel
      -----------------------
       VOCÊ GANHOU!''') 
else:
    if escolha_user == 0:
      print('''
      -----------------------
       Computador jogou tesoura
      -----------------------
       VOCÊ GANHOU!''') 
    elif escolha_user == 1:
      print('''
      -----------------------
       Computador jogou tesoura
      -----------------------
       COMPUTADOR GANHOU!''') 
    elif escolha_user == 2:
      print('''
      -----------------------
       Computador jogou tesoura
      -----------------------
       EMPATE!''') 