def carreira(nome,gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

jogador = str(input('Nome do Jogador: ')).strip()
gol = input('Quantidade de Gols: ').strip()
carreira(jogador,gol)
