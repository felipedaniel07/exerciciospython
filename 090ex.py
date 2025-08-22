ficha = {}
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Digite a média de {ficha['nome']}: '))
if ficha['media'] >= 7:
    ficha['situacao'] = 'Aprovado'
elif ficha['media'] >= 5 and ficha['media'] < 7:
    ficha['situacao'] = 'Recuperação'
else:
    ficha['situacao'] = 'Reprovado'
print('--'*20)
for k, v in ficha.items():
    print(f'- {k} é igual a {v}')
