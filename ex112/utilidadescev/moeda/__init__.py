def dobro(n=0, sit=True):
    res = n * 2
    if sit == True:
        res = moeda(res)
    return res

def metade(n=0,sit=True):
    res = n / 2
    if sit == True:
        res = moeda(res)
    return res

def aumentar(n=0,t=0,sit=True):
    res = n + (n * t)
    if sit == True:
        res = moeda(res)
    return res

def diminuir(n=0,t=0,sit=True):
    res = n - (n * t / 100)
    if sit == True:
        res = moeda(res)
    return res

def moeda(n=0,sit=True):
    res = (f'R${n:.2f}')
    res = res.replace('.', ',')
    return res

def resumo(n=0,a=0,d=0):
    print('-'*30)
    print('Resumo do Valor'.center(30))
    print('-'*30)
    print(f'Preço Analisado: \t{moeda(n,True)}')
    print(f'Dobro do preço: \t{dobro(n,True)}')
    print(f'Metade do preço: \t{metade(n,True)}')
    print(f'Aumento de {a}%: \t{aumentar(n,a,True)}')
    print(f'Desconto de {d}%: \t{diminuir(n,d,True)}')
    print('-'*30)