n1 = int(input('Digite o valor da primeira nota: '))
n2 = int(input('Digite o valor da segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Você está reprovado!')
elif m >= 5 and m < 7:
    print('Você está em recuperação!')
else:
    print('Você está aprovado!')
