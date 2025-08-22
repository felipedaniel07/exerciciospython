from time import sleep
from random import randint
def maior(val):
    print('-='*18)
    sleep(1)
    print('Analisando os valores informados...')
    for v in val:
        sleep(0.5)
        print(f'{v}', end=' ')
    sleep(0.5)
    print(f'\nForam informados {len(val)} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {max(val)}.')



valores = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
maior(valores)
valores2 = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
maior(valores2)
valores3 = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
maior(valores3)
print('Fim Do Programa!')