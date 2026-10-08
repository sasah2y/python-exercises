while True:
    num = int(input('Qual número você gostaria de ver a tabuada?'))
    if num < 0:
        print('PROGRAMA ENCERRADO!!')
        break
    
    for i in range(1, 11):
        print('{} x {} = {}' .format(num, i ,num * i))