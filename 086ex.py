matriz = [ [0,0,0], [0,0,0], [0,0,0] ]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l},{c}]: '))
for l in matriz:
    for c in l:
        print(f'[{c:^5}] ', end='')
    print()



