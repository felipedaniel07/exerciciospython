from random import randint
pc = randint(0 , 10)
s = 0
print('Vamos brincar de um jogo!')
print('Tente adivinhar o número que estou pensando...')
print('Você consegue?')
acertou = False
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    s += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais ... Tente novamente!')
        else:
            print('Menos ... Tente novamente!')
print('Você levou {} tentativas, Párabens!'.format(s))
