s = 0
count = 0
for c in range(1 , 7):
    n = int(input('Digite um valor:'))
    if n % 2 == 0:
        s += n
        count += 1
print('Voce informou {} numeros pares e a  somatoria de todos os números pares são {} !'.format(count,s))

