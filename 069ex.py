ci = ch = cm = 0
while True:
    print('--'* 20)
    print('         CADASTRE UMA PESSOA')
    print('--' * 20)
    idd = int(input('DIGITE A IDADE: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('DIGITE SEU SEXO [M/F]: ')).strip().upper()[0]
    print('--' *20)
    if idd > 18:
        ci += 1
    if sexo == 'M':
        ch += 1
    if sexo == 'F' and idd < 20:
        cm += 1
    esc = ' '
    while esc not in 'SsNn':
        esc = str(input('VOCÊ QUER CONTINUAR? [S/N]: ')).strip().upper()[0]
    if esc == 'N':
            break
print(f'{ci} PESSOAS TEM MAIS DE 18 ANOS!')
print(f'FOREM CADASTRADOS {ch} HOMENS!')
print(f'FORAM CADASTRADAS {cm} MULHERES MENORES DE 20 ANOS!')