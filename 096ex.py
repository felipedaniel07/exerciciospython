def area(larg, comp):
    print(f'A área de um terreno {larg}x{comp} é igual a {larg * comp}m².')


print('-'*45)
print(f'CONTROLE DE TERRENOS'.center(45))
print('-'*45)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l, c)