pr1 = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
ter = int(input('Digite a quantidade de termos: '))
termo = pr1 + (ter - 1) * raz
for c in range(pr1, termo + raz, raz):
    print(c , end=' -> ')
print('Fim')

