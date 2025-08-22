lista = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor Repetido,Tente Novamente!')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while escolha not in 'SN':
        print('Opção Invalida, Tente Novamente!')
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
lista.sort()
print(f'Todos os valores em ordem crescente: {lista}')










