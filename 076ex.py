lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Cardeno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*42)
titulo = 'LISTAGEM DE PREÇOS'
print(titulo.center(42))
print('-'*42)
for pos in range(0, len(lista)):
    if pos %2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f' R$  {lista[pos]:>7.2f}')
print('-'*42)





