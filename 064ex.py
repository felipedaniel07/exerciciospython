soma = n1 = c = 0
n1 = int(input('Digite um número [Digite 999 para sair] :'))
while n1 != 999:
    c += 1
    soma = n1 + soma
    n1 = int(input('Digite um número [Digite 999 para sair] :'))
print('voce digitou {} números e a soma deles foi de {} !'.format(c, soma))