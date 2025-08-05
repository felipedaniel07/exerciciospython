print("""Escolha uma opção:
[1] Binário
[2] Octal
[3] Hexadecimal""")
num = int(input('Escolha uma opção:'))
esc = int(input('Digite um número para a conversão:'))

if num == 1:
    print('O número convertido para binário é {} !'.format(bin(esc[2:])))
elif num == 2:
    print('O número convertido para octal é {} !'.format(oct(esc[2:])))
elif num == 3:
    print('O número convertido para hexadecimal é {} !'.format(hex(esc[2:])))
else:
    print('Escolha uma opção correta!')

