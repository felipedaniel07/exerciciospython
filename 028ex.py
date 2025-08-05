import random
n = int(random.randint(1,5))


n2 = int(input('Tente adivinhar um número que pensei entre 1 e 5: '))
print('Eu pensei no número {} e você no {}!'.format(n, n2))
if n2 == n:
    print('Parabens você acertou!')
else:
    print('Você errou tente novamente!')
