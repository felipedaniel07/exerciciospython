print('Minha versão')
print('               ')
cdd = input('Cidade que você nasceu: ').upper()
cdd1 = cdd.split()
print('A sua cidade começa com a palavra santo: {}'.format('SANTO' in cdd1[0]))
print('               ')
print('Versão Guanabara')
cd = input('Em que cidade você nasceu? ').strip()
print(cd[:5].upper() == 'SANTO')


