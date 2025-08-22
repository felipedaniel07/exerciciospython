lista = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if lista[pos] >= num:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print(f'A lista em forma crescente: {lista}')








