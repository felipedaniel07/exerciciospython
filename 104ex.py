def leiaint(num):
    num = input(num).strip()
    while True:
        if num.isnumeric():
            return num
        else:
            print(f'''Valor Invalido!
Digite apenas algum valor inteiro!''')
            num = input('Digite um valor:').strip()



print('-'*40)
n = leiaint('Digite um valor:')
print(f'O número {n} é inteiro.')
