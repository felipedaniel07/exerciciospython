import random
print('VAMOS BRINCAR DE JOKENPÔ!')
esc = str(input('Escolha pedra,papel ou tesoura:'))
l = ['pedra' , 'papel' , 'tesoura' ]
esc2 = random.choice(l)
print('EU ESCOLHI {} E VOCÊ {} !'.format(esc2, esc))
if esc == esc2:
    print('NOS EMPATAMOS!')
elif esc == 'pedra' and esc2 == 'papel' or esc == 'papel' and esc2 == 'tesoura' or esc == 'tesoura' and esc == 'pedra':
    print('EU GANHEI!!')
else:
    print('VOCÊ GANHOU!!')


