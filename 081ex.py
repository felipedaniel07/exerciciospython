lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    esc = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while esc not in 'SN':
        print('Opção Invalida, Tente novamente!')
        esc = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if esc == 'N':
        break
print(f'Foram digitados {len(lista)} Valores ao todo!')
if 5 in lista:
    print('O Número 5 está na lista!')
else:
    print('O número 5 não está na lista.')
lista.sort(reverse=True)
print(f'A lista em forma descrecente: {lista}')



