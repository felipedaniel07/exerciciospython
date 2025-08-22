ficha = []
lista =[]
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, nota1, nota2, media])
    lista.append(ficha[:])
    ficha.clear()
    esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if esc == 'N':
        break
print()
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for pos, al in enumerate(lista):
    print(f'{pos:<4}{al[0][0]:<10}{al[0][3]:>8.1f}')
while True:
    print()
    esc = int(input('Mostrar notas de qual aluno [999 para sair]: '))
    if esc == 999:
        print('Finalizando...')
        break
    else:
        for p in lista[esc]:
            print(f'Notas de {p[0]} são [{p[1]}, {p[2]}]')
print('FIM DO PROGRAMA!')


















