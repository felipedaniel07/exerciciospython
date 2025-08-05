sa = float(input('Qual o seu sálario? '))
if sa >= 1250:
    print('Seu novo sálario com aumento de 10% será de {:.2f}R$'.format(float(sa *1.10)))
else:
    print('Seu novo sálario com aumento de 15% será de {:.2f}R$'.format(float(sa *1.15)))

