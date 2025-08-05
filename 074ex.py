from random import randint
n1 =(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Os Valores Sorteados Foram: ', end='')
for n in n1:
    print(f' {n} ',end='')
print(f'\nO Maior valor sorteado foi {max(n1)}!')
print(f'O Menor valor sorteado foi {min(n1)}!')


