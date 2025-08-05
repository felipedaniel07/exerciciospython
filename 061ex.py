pr1 = int(input('Digite o primeiro termo:'))
raz = int(input('Digite a razão:'))
dec = pr1 + (10 - 1 )* raz
c = pr1
while c != dec + raz:
    print(c , end=' -> ')
    c += raz
print('FIM')


