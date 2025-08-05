n = int(input('Digite um valor: '))
c = n
f = 1
print('O factorial de {}! é:'.format(n))
while c != 0:
    f *= c
    print(' {} '.format(c) , end='')
    print('x' if c > 1  else '= ', end='')
    c -= 1
print(f)


