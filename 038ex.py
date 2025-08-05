num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro valor: '))
if num1 > num2:
    print('O primeiro valor {} é maior!.'.format(num1))
elif num2 > num1:
    print('O segundo número {} é maior!.'.format(num2))
else:
    print('O primeiro número {}, e o segundo {}, são iguais!'.format(num1, num2))
