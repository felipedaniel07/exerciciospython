c  = 0
lista = []
while c != 5:
        num = (int(input(f'Digite o {c+1}° valor: ')))
        if num in lista:
            print('Número repetido tente novamente!')
            continue
        if c == 0:
            lista.append(num)
        else:
            pos = 0
            while pos < len(lista):
                if num < lista[pos]:
                    break
                pos += 1
            lista.insert(pos, num)
        c += 1
print(f'A lista organizada: {lista}')











