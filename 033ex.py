n = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n > n2 and n > n3:
    print('Seu maior número é {}'.format(n))
if n2 > n and n2 > n3:
    print('Seu maior número é {}'.format(n2))
if n3 > n and n3 > n2:
    print('Seu maior número é {}'.format(n3))

if n < n2 and n < n3:
    print('O menor número é {}'.format(n))
if n2 < n and n2 < n3:
    print('O menor número é {}'.format(n2))
if n3 < n and n3 < n2:
    print('O menor número é {}'.format(n3))