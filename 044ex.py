pd = float(input('Digite o valor do produto: '))
print("""ESCOLHA A FORMA DE PAGAMENTO
[1] À VISTA NO DINHEIRO/CHEQUE
[2] À VISTA NO CARTÃO
[3] ATÉ 2 VEZES NO CARTÃO
[4] 3 VEZES OU MAIS NO CARTÃO COM JUROS""")
es = int(input('Digite o número escolhido: '))

if es == 1:
    print('O valor ficará em R${} com desconto de 10%'.format(pd * 0.90))
elif es == 2:
    print('O valor ficará em R${} com desconto de 5%'.format(pd * 0.95))
elif es == 4:
    pdcj = pd * 1.20
    print('O valor ficará em R${} com juros de 20%'.format(pdcj))
elif es == 3:
    print('O valor ficará R${} sem desconto e juros'.format(pd))
else:
    print('Digite algum número valido!')




