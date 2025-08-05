nome = str(input('Digite o seu nome completo:')).strip()
print('O seu nome todo em maiúsculo: {}'.format(nome.upper()))
print('O seu nome todo em minúsculo: {}'.format(nome.lower()))
nome2 = nome.split()
nome3 = len(nome2[0])
nome4 = nome2[0]
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome4, nome3))
print('Seu nome tem ao todo {} letras'.format(len(nome2) - nome.count(' ')))









