lista = []
pares = []
impares = []
while True:
    num = int(input('Digite algum valor: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    esc = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while esc not in 'SN':
        esc = input('Deseja continuar [S/N]: ').strip().upper()[0]
    print()
    if esc == 'N':
        break
print('-='*20)
print(f'Conteudo da lista: {lista}')
print(f'Números pares presentes na lista: {pares}')
print(f'Números ímpares presentes na lista: {impares}')