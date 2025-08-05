c = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n <= -1:
        break
    for co in range(1, 11):
        print(f'{n} x {co} = {n * co}')
        co += 1
print('Programa tabuada finalizado com sucesso, volte sempre!')
