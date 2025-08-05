s = pra = c = menor = nome = 0
print('-'*30)
print('  LOJA SUPERMARIO ATACADISTA')
print('-'*30)
while True:
    np = str(input('DIGITE O NOME DO PRODUTO: '))
    pr = float(input('PREÇO: '))
    c += 1
    if c == 1:
        menor = pr
        nome = np
    else:
        if pr < menor:
            menor = pr
            nome = np
    s += pr
    if pr > 1000:
        pra += 1
    esc = str(input('VOCÊ QUER CONTINUAR? [S/N]: ')).strip().upper()[0]
    while esc not in 'SsNn':
        esc = str(input('VOCÊ QUER CONTINUAR? [S/N]: ')).strip().upper()[0]
    if esc == 'N':
        break
print(f'O TOTAL DA COMPRA FOI R${s}')
print(f'TEMOS {pra} CUSTANDO MAIS DE 1000 REAIS!')
print(f'O PRODUTO MAIS BARATO FOI A {nome} CUSTANDO R${menor} !')
