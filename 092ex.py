import datetime 
dic = {}
dic['Nome'] = input('Nome: ')
idd = int(input('Ano de nascimento: '))
dic['idade'] = datetime.date.today().year - idd
dic['ctps'] = int(input('Digite sua Carteira de Trabalho (0 não tem): '))
if dic['ctps'] > 0:
    dic['contratação'] = int(input('Ano de contratação: '))
    dic['sálario'] = float(input('Sálario: '))
    dic['aposentadoria'] = (dic['contratação'] - idd) + 32
for k, v in dic.items():
    print(f'{k} tem o valor {v}')
