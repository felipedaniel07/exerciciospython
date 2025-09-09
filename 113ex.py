def leiaint(n):
    while True:
        try:
            n = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mError:Por favor insira um Número Inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print("\n\033[31mO Úsuario não digitou o número então automaticamente ele receberá o valor 0.\033[m")
            n = 0
            return n
        else:
            return n

def leiafloat(n):
    while True:
        try:
            n = float(input(n))
        except (ValueError, TypeError):
            print('\033[31mERROR:Por favor insira um número Real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print("\n\033[31mO Úsuario não digitou o número então automaticamente ele receberá o valor 0.\033[m")
            return 0
        else:
            return n

n_int = leiaint('Digite um número inteiro : ')
n_float = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n_int} e o real foi {n_float}')