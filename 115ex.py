
while True:
    print('-'*40)
    print('MENU'.center(40))
    print('-'*40)
    print('1- Ver Pessoas Cadastradas')
    print('2- Cadastrar Pessoas')
    print('3- Sair do sistema')
    print('-'*40)
    while True:
        try:
            esc = int(input('Digite sua escolha: '))
            while esc not in [1,2,3]:
                print('OPÇÃO INVÁLIDA!')
                esc = int(input('Digite sua escolha: '))




