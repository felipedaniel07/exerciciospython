num = ('''''''Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
       'Sete', 'Oito', 'Nove', 'Dez','Onze', 'Doze', 'Treze',
       'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte''')
while True:
    nesc = int(input('Escolha um valor entre 0 e 20: '))
    while nesc not in range(0, 21):
        nesc = int(input('Tente novamente!, Escolha um valor entre 0 e 20: '))
    print(f'Você escolheu o número {num[nesc]} !')
    escolha = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Erro, Tente novamente.Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
            break
print('Programa Encerrado!')




