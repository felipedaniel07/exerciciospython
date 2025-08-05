s = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count += 1
        s += c
print('O valor total dos multipos de 3 que sao {} valores, a soma é de {} !'.format(count,s))

