from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resp = menu(['Ver Pessoas Arquivadas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resp == 1:
        cabecalho('Opção 1')
        lerarquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        print('Saindo do sistema.... Até mais!')
        break
    else:
        print('\033[31mError: Digite alguma opção inválida.\033[m')
    sleep(2)

