l1 = float(input('Digite o primeiro lado do triangulo: '))
l2 = float(input('Digite o segundo lado do triangulo: '))
l3 = float(input('Digite o terceiro lado do triangulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Com as medidas podemos formar um triangulo!')
    if l1 == l2 and l2 == l3:
        print('Seu triangulo é EQUILÁTERO!')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Seu triangulo é ISÓSCELES!')
    else:
        print('Seu triangulo é ESCALENO!')
else:
    print('Com as medidas não podemos formar um triangulo!')
