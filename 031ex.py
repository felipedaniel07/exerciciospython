n = float(input('Qual vai ser a distancia em km da sua viagem? '))
if float(n <= 200):
    print('Você pagará {}R$ de passagem'.format(n * 0.50))
else:
    print('Você pagará {}R$ de passagem'.format(n * 0.45))
