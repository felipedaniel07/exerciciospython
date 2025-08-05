r1 = float(input('Digite um comprimento de uma reta: '))
r2 = float(input('Digite um comprimento de uma reta: '))
r3 = float(input('Digite um comprimento de uma reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Suas retas da para fazer um triangulo!')
else:
    print('Suas retas não da para fazer um triangulo!')
