s = 0
sm = 0
for c in range(1 , 7+1):
    n = int(input('Digite o ano de nascimento da {}o pessoa:'.format(c)))
    idd = 2025 - n
    if idd >= 21:
        s += 1
    else:
        sm += 1
print('{} já são maiores de idade!'.format(s))
print('{} ainda são menores de idade!'.format(sm))

