def dobro(n=0):
    res = n * 2
    return res

def metade(n=0):
    res = n / 2
    return res

def aumentar(n=0,t=0):
    res = n + (n * t)
    return res

def diminuir(n=0,t=0):
    res = n - (n * t / 100)
    return res

def moeda(n=0):
    res = (f'R${n:.2f}')
    res = res.replace('.', ',')
    return res