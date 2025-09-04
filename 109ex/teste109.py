import moeda
p = float(input('Digite um preço: '))
print(f'O dobro de {moeda.moeda(p)} é igual a {moeda.dobro(p,False)}')
print(f'A metade de {moeda.moeda(p)} é igual a {moeda.metade(p,True)}')
print(f'O aumento de 10% em {moeda.moeda(p)} fica igual a {moeda.aumentar(p, 10,False)}')
print(f'Diminuido 13% em {moeda.moeda(p)}  fica igual a {moeda.diminuir(p, 13,True)}')
