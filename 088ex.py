from random import randint
from time import sleep
lista = []
prov = []
tot = 1
print('-='*20)
titulo = 'MEGA SENA'
print(titulo.center(40))
print('-='*20)

esc = int(input('Quantos jogos você quer que eu sorteie? '))
print('-'*10,f'Sorteando {esc} Jogos','-'*11)
while tot <= esc:
    count = 0
    while True:
        pc = randint(1, 60)
        if pc not in lista:
            prov.append(pc)
            count += 1
        if count >= 6:
            break
    lista.append(prov[:])
    prov.clear()
    tot += 1
for pos,j in enumerate(lista):
    print(f'Jogo {pos+1}: {j}')
    sleep(1)
print('-='*7, 'BOA SORTE', '-='*7)





