from time import sleep
while True:
    print('\033[0;0;43mSISTEMA DE AJUDA HELP')
    esc = str(input('\033[mFunção ou biblioteca > '))
    if esc == 'fim' or esc == 'Fim':
        break
    sleep(0.5)
    print(f'\033[0;0;46mAcessando o Manual do {esc} .....')
    print(f'\033[0;0;47m')
    help(esc)
print('Programa encerrado!!')