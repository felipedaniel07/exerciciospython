par = 0
n =    (int(input('Digite o 1° Valor: ')),
     int(input('Digite o 2° Valor: ')),
     int(input('Digite o 3° Valor: ')),
     int(input('Digite o 4° Valor: ')))

print(n)
print(f'O 9 apareceu {n.count(9)} Vezes!')
if 3 in n:
    print(f'O Três apareceu na posição {n.index(3) + 1}°')
else:
    print('O número Três não foi digitado nenhuma vez!')
print(f'Os valores pares digitados foram: ',end='')
for ns in n:
    if ns %2 == 0:
        print(ns, end=' ')

