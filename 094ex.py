lista = []
ficha = {}
md = 0
while True:
    ficha['nome'] = str(input('Nome: ')).strip()
    ficha['sexo'] = str(input('Sexo: [F/M]: ')).strip().upper()[0]
    while ficha['sexo'] not in 'FM':
        print('Digite M ou F.')
        ficha['sexo'] = str(input('Sexo: [F/M]: ')).strip().upper()[0]
    ficha['idade'] = int(input('Idade: '))
    lista.append(ficha.copy())
    md += ficha['idade']
    ficha.clear()
    opc = str(input('Quer continuar? [S/N]: ')).upper()[0]
    while opc not in 'SN':
        print('Error, Digite apenas [S/N]: ')
        opc = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if opc == 'N':
        break
md = md / len(lista)
print(f'A) Ao todos temos {len(lista)} pessoas cadastradas')
print(f'B) A média de idade é de {md:.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p['nome']}', end=' ')
print('\nD) Lista de pessoas acima da idade média.')
for p in lista:
    if p['idade'] > md:
        print(f'Nome == {p['nome']}; Sexo == {p["sexo"]}; Idade == {p["idade"]}')
print('Programa Encerrado!')

