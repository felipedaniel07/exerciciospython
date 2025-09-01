def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O valor a ser calculado
    :param show: (opcional) Mostra o calculo do fatorial
    :return: retorna o valor do fatorial
    """
    f = 1
    for c in range(n, 0 ,-1):
        f *= c
        if show == True :
            if c == 1 :
                print(f'{c} =', end=' ')
            else:
                print(f'{c} x' , end=' ')
    return f

print(f'{fatorial(5)}')

