valores = [int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')),
int(input('Digite o 3º valor: ')), int(input('Digite o 4º valor: ')), int(input('Digite o 5º valor: '))]
print('-='*25)
print(f'Você Digitou os valores {valores}!')
c = cmr = 0
for p, n in enumerate(valores):
    if n == min(valores):
        if c == 0:
            print(f'O Menor valor foi {n} e a sua posição foi de ', end='')
            print(f'{p+1}... ' , end='')
            c += 1
        else:
            print(f'{p+1}... ', end='')
    else:
        if n == max(valores):
            if cmr == 0:
                print(f'\nO Maior valor foi {n} e a sua posição foi de ', end='')
                print(f'{p+1}... ' , end='')
                cmr += 1
            else:
                print(f'{p+1}... ', end='')


