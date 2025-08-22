from time import sleep
def contador(inicio, fim, passo):
    print('-='*20)
    sleep(1)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio <= fim:
        for c in range(inicio, fim +1, passo):
            sleep(0.5)
            print(c, end=' ')
    else:
        for c in range(inicio, fim -1 , -passo):
            sleep(0.5)
            print(f'{c:2}', end=' ')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é a sua vez de Personalizar a contagem!')
ini = int(input('Ínicio: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fi, pas)
