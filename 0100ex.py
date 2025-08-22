from random import randint
from time import sleep
lista = []
def sortear(val):
    for c in range(0, 5):
        val.append(randint(1, 10))
    print('Sorteando os 5 valores da lista: ', end=' ')
    for v in val:
        print(v, end=' ')
        sleep(0.5)
    print('PRONTO!')


def somapar(num):
    soma = 0
    sleep(0.5)
    print(f'Somando os valores pares de {num} temos: ', end='')
    for n in num:
        if n % 2 == 0:
            soma += n
    sleep(0.5)
    print(soma)


sortear(lista)
somapar(lista)
