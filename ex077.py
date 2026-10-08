palavras = (
    ('APRENDER'),
    ('PROGRAMAR'),
    ('LINGUAGEM'),
    ('PYTHON'),
    ('CURSO'),
    ('GRATIS'),
    ('ESTUDAR'),
    ('PRATICAR'),
    ('TRABALHAR'),
    ('MERCADO'),
    ('PROGRAMADOR'),
    ('FUTURO')
)

vogais = ("a", "e", "i", "o", "u")

for palavra in palavras:
    print(f'Na palavra {palavra} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in vogais:
           print(letra, end = ' ')
    print()