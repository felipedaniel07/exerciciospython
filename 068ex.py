from random import randint
s = c = 0
print('-=' *30)
print(' VAMOS JOGAR PAR OU IMPAR!')
print('-='*30)
while True:
    pc = randint(1, 10)
    es = str(input('ESCOLHA PAR OU ÍMPAR[P/I]: ')).strip().upper()[0]
    n = int(input('DIGITE O SEU NÚMERO: '))
    s = n + pc
    print('--'*30)
    if s %2 == 0:
        print(f'VOCÊ JOGOU {n} E O COMPUTADOR {pc},TOTAL DE {s} DEU PAR!')
        if  es == 'P' :
            print('--' * 30)
            print('VOCÊ GANHOU!')
            print('VAMOS JOGAR NOVAMENTE ......')
            print('--' * 30)
            c += 1
        else:
            break
    else:
        print(f'VOCÊ JOGOU {n} E O COMPUTADOR {pc},TOTAL DE {s} DEU ÍMPAR!')
        if es == 'I':
            print('--' * 30)
            print('VOCÊ GANHOU!')
            print('VAMOS JOGAR NOVAMENTE ......')
            print('--' * 30)
            c += 1
        else:
            break
print('-=' *30)
print(f'GAME OVER, VOCÊ VENCEU {s} VEZES! ')



