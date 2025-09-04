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