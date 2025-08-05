pr1 = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
c = ct = 0
ter = pr1
ter2 = pr1
qnt = 10
while c != qnt:
    c +=1
    ct += 1
    print(ter, '-> ' if c < qnt else '-> Pausa' , end='')
    ter += raz
    if c == qnt:
        term2 = int(input(('\nQuer mostrar mais quantos? ')))
        qnt += term2
print('Fim do Programa!')
print('Progressão finalizada com {} termos mostrados.'.format(ct))


