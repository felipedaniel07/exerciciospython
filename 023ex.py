num = int(input('Digite um número entre 0 a 9999: '))

#print('A unidade:{}'.format(n[3]))
#print('A dezena:{}'.format(n[2]))
#print('A centena:{}'.format(n[1]))
#print('A milha:{}'.format(n[0]))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A unidade: {}'.format(u))
print('A dezena: {}'.format(d))
print('A centena: {}'.format(c))
print('A milhar: {}'.format(m))





