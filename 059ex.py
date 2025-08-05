op = 0
print('----------------------')
n1 = int(input('Digite um valor: '))
print('----------------------')
n2 = int(input('Digite outro valor: '))
while op != 5:
    print('''----------------------
------- OPÇÕES -------
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
----------------------''')
    op = int(input('DIGITE SUA OPÇÃO: '))
    if op == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1,n2, soma))
    elif op == 2:
        vezes = n1 * n2
        print('{} x {} = {}'.format(n1, n2, vezes))
    elif op == 3:
        if n1 > n2:
            print('O NÚMERO MAIOR É {}'.format(n1))
        elif n1 < n2:
            print('O NÚMERO MAIOR É {}'.format(n2))
        else:
            print('OS NÚMEROS SÃO IGUAIS !')
    elif op == 5:
        op = 5
    elif op == 4:
        print('----------------------')
        print('INSIRA OS NÚMEROS NOVAMENTE!')
        print('----------------------')
        n1 = int(input('Digite um valor: '))
        print('----------------------')
        n2 = int(input('Digite outro valor: '))
    else:
        print('Opção invalida!')
print('FIM DO PROGRAMA!')
