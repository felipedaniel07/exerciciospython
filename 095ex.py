ficha = {}
gol = []
listas = []
while True:
    ficha['nome'] = str(input('Nome: ')).strip()
    np = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))
    for c in range(1, np+1):
        gol.append(int(input(f'  Quantos gols na partida {c}? ')))
    ficha['gols'] = gol[:]
    ficha['total'] = sum(gol)
    listas.append(ficha.copy())
    ficha.clear()
    gol.clear()
    esc = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while esc not in 'SN':
        print('Digite apenas S ou N.')
        esc = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if esc == 'N':
        break
print('-='*30)
print('cod ', end='')
for p in listas:
    for k in p.keys():
        print(f'{k:<15}', end= '')
    print()
for pos,p in enumerate(listas):
    print(f'{pos:>3} ' , end='')
    for d in p.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    esc2 = int(input('Deseja mostrar dados de qual jogador? [999] para interromper: '))
    if esc2 == 999:
        break
    if esc2 > len(listas) or esc2 < 0:
        print(f'Error !,Não existe jogador com o código {esc2}, tente novamente.')
    else:
        print(f'Levantamento do jogador {listas[esc2]["nome"]}')
        for pos,gol in enumerate(listas[esc2]['gols']):
            print(f'Na partida {pos +1} fez {gol} gols.')




