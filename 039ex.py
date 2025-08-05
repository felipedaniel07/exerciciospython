nac = int(input('Informe sua data de nascimento: '))
dataatual = int(input('Informe o ano atual: '))
idd = dataatual - nac
print(idd)
if idd < 18:
    print('Você ainda vai se alistar!')
elif idd == 18:
    print('Você está na hora de se alistar!')
else:
    print('Você passou da hora de se alistar!')

