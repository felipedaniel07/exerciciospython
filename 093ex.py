gol = []
carreira = {}
carreira['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Partidas em que ele jogou: '))
for c in range(1, partidas +1):
    gol.append(int(input(f'Quantos gols na {c}° partida?')))
carreira['gols'] = gol[:]
carreira['total'] = sum(gol)
print('--'*30)
print(carreira)
print('--'*30)
for k, v in carreira.items():
    print(f'O campo {k} tem o valor {v}')
print('--'*30)
print(f'O jogador {carreira["nome"]} fez {partidas} partidas')
for pos,v in enumerate(carreira['gols']):
    print(f'=> Na {pos + 1}° partida fez {v} gols')
print(f'Total de {carreira["total"]} gols')


