tot = 0
num = int(input('Digite um numero: '))
for c in range(1, num + 1):
    print(c, end=' ')

    if num % c == 0:

        tot += 1
    else:
        print( end=' ')
print('\nO seu número foi divisivel {} vezes!'.format(tot))
if tot == 2:
    print('Por isso ele é primo!')
else:
    print('Por isso ele não é primo!')













