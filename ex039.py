from datetime import date 

atual = date.today().year 
ano_nascimento = int(input('Digite seu ano de nascimento:'))
idade = atual - ano_nascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, atual))


if idade == 18:
     print('Você deve se alistar esse ano!')
elif idade < 18:
    faltam = 18 - idade
    ano_alistamento = atual + faltam
    print('Ainda faltam {} anos para o alistamento.' .format(faltam) )
    print('Seu alistamento será em {}.' .format(ano_alistamento))

else:
   passou = idade - 18
   ano_alistamento = atual - passou
   print('Você já deveria ter se alistado fazem {} anos.' .format(passou))
   print('Seu alistamento foi em {}.' .format(ano_alistamento))
