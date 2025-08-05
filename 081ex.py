lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    esc = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while esc not in 'SN':
        esc = input('Digite novamente [S/N] ').strip().upper()[0]
    if esc == 'N':
        break
print('-='*20)
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'A lista está organizada de forma  decrescente: {lista}')
if 5 in lista:
    print('O número 5 está presente na lista.')
else:
    print('O número 5 não está presente na lista.')


