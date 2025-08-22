pessoa = []
galera = []
mai = men = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        if pessoa[1] < men:
            men = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()
    esc = str(input('Sair do sistema? [S/N]: ')).strip().upper()[0]
    while esc not in 'SN':
        print('ERRO: Digite apenas S ou N.')
        esc = str(input('Sair do sistema? [S/N]: ')).strip().upper()[0]
    if esc == 'S':
        break
print(f'Foram cadastrados ao todo {len(galera)} pessoas.')
print(f'O maior peso foi de {mai}Kg e são de: ', end='')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}]',end=' ')
print(f'\nO menor peso foi de {men}Kg e são de: ',end='')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}]',end=' ')




















#print(f'Foram cadastradas {len(galera)} pessoas.')





