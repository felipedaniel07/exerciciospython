sexo = str(input('Digie seu sexo (M/F): ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Informação Inválida. Digite seu sexo (M/F): ')).strip().upper()[0]
print('Sexo {} Foi registrado com sucesso!'.format(sexo))
