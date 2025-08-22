matriz = [ [0,0,0], [0,0,0], [0,0,0] ]
par = sm3 = mai= 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            sm3 += matriz[l][c]
    if l == 1:
        mai = max(matriz[l])
for l in matriz:
    for c in l:
        print(f'[{c:^5}] ', end='')
    print()
print('-='*25)
print(f'A soma dos valores pares são: {par}')
print(f'A soma dos valores da terceira coluna são: {sm3}')
print(f'O maior valor da segunda linha é: {mai}')
