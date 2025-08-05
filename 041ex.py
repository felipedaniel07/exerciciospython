nasc = int(input('Digite o ano de nascimento: '))
datual = int(input('Digite a data atual: '))
idd = datual - nasc
print('Sua idade é {} anos!'.format(idd))
if idd <= 9:
    print('Sua categoria é MIRIM!')
elif idd <= 14:
    print('Sua categoria é INFANTIL!')
elif idd <= 19:
    print('Sua categoria é JUNIOR!')
elif idd <= 20:
    print('Sua categoria é SÊNIOR!')
else:
    print('Sua categoria é MASTER!')

