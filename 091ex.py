from random import randint
from operator import itemgetter
from time import sleep
dic = {'jogador1': randint(1, 6),'jogador2': randint(1, 6),
       'jogador3': randint(1, 6),'jogador4': randint(1, 6),}
print('SORTEANDO VALORES:')
for k, v in dic.items():
    sleep(1)
    print(f'  - {k} tirou {v} no dado.')
ranking = sorted(dic.items(),key=itemgetter(1),reverse=True)
print('-='*20)
print('RANKING DOS VALORES:')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'  - {i+1}° lugar: {v[0]} com {v[1]} no dado.')

