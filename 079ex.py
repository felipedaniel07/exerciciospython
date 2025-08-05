num = []
c = 0
while True:
    n = int(input(f'Digite {c+1}° valor: '))
    if c == 0:
        num.append(n)
        print('Número adicionado com sucesso!')
    else:
        if n in num:
            print('Número já existe na lista. Tente outro.')
            continue
        else:
            num.append(n)
            print('Número adicionado com sucesso!')
    c += 1
    opcao = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    while opcao not in 'NS':
        print('OPÇÃO INVALIDA, TENTE NOVAMENTE!')
        opcao = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
    print()
print(f'Os valores em ordem crescente são: {sorted(num)}')










