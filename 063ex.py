t1 = t3 = 0
t2 = 1
c = 3
print('_' * 30)
print(' SEQUÊNCIA DE FIBONACCI ')
print('_' * 30)
ter = int(input('QUANTOS TERMOS DESEJA MOSTRAR: '))
print('~'* 30)
print('{} -> {} -> '.format(t1, t2), end='')
while c != ter +1:
    c += 1
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
print('FIM')
print('~'* 30)
