lista = []
menor = maior = 0
for c in range(0,5):
    num = int(input(f'Digite um valor para a posição {c+1}°: '))
    lista.append(num)
print(f'Você digitou os valores {lista}')
print(f'O Maior valor digitado foi {max(lista)} na Posição: ', end='')
for pos, n in enumerate(lista):
    if n == max(lista):
        print(f'...{pos +1} ', end='')
print(f'\nO Menor valor digitado foi {min(lista)} na Posição: ', end='')
for pos, n in enumerate(lista):
    if n == min(lista):
        print(f'...{pos +1} ', end='')


