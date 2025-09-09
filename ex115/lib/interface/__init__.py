def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(txt):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in txt:
        print(f'\033[33m{c} -\033[m \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[33mSua Opção:\033[m ')
    return opc

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

