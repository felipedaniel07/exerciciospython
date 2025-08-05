menor = 0
maior = 0
for p in range(0 , 5):
    peso = int(input('Digite seu peso: '))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é de {} kg!'.format(maior))
print('O menor peso é de {} kg!'.format(menor))

