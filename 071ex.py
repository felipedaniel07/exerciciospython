print('='*30)
print('          Banco FD')
print('='*30)
ced = 50
c = 0
saque = int(input('Digite o valor do saque: '))
total = saque
while True:
    if total >= ced:
        total -= ced
        c += 1
    else:
        if c > 0:
            print(f'Total de {c} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        elif ced == 1:
            ced = 0
        c = 0
        if ced == 0:
            break
print('='*30)
print('    FINALIZADO COM SUCESSO!')
print('='*30)
