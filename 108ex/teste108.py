import moeda
p = float(input('Digite um preço: '))
print(f'O dobro de {moeda.moeda(p)} é igual a {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é igual a {moeda.moeda(moeda.metade(p))}')
print(f'O aumento de 10% em {moeda.moeda(p)} fica igual a {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuido 13% em {moeda.moeda(p)}  fica igual a {moeda.moeda(moeda.diminuir(p, 13))}')