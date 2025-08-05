ano = int(input('Digite algum ano qualquer: '))
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('Seu ano é bissexto!')
else:
    print('Seu ano não é bissexto!')

