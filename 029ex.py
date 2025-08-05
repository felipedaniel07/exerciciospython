km = int(input('Qual a velocidade de um carro: '))
if km > 80:
    print('Você passou do limite e será multado!')
    print('Você será multado no valor de {}R$!'.format(int((km - 80)*7)))
else:
    print('Você está dentro do limite,Tenha um bom dia!')



