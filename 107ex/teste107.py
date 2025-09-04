import moeda
p = float(input('Digite um preço: '))
print(f'O dobro de {p} é igual a {moeda.dobro(p)}')
print(f'A metade de {p} é igual a {moeda.metade(p)}')
print(f'O aumento de 10% em {p} fica igual a {moeda.aumentar(p, 10)}')
print(f'Diminuido 13% em {p}  fica igual a {moeda.diminuir(p, 13)}')