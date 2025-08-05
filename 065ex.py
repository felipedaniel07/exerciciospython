co = sm =  menor = maior = 0
c = 'S'
while c  in  'S':
    n1 = int(input('Digite um número: '))
    co += 1
    if co == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    sm += n1
    c = str(input('Deseja continuar: [S/N]: ')).strip().upper()[0]
print('O maior valor foi de {} e o menor {} !'.format(maior,menor))
print('Você digitou {} números e a média deles foi {} !'.format(co, sm / co))
