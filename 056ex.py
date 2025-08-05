iddt = 0
fm = 0
idhv = 0
idhn = 0
nomev = 0
for c in range(1 ,4+1):
    print('------- {}o PESSOA ---------'.format(c))
    nome = str(input('Digite seu nome: ')).strip().title()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()
    iddt += idade
    if sexo == 'M' and c == 1:
            idhv = idade
            nomev = nome
    if sexo in 'M' and idade > idhv:
        idhv = idade
        nomev = nome
    if sexo == 'F' and idade < 20:
        fm += 1
print('A media de idade é de {} anos!'.format(iddt /4))
print('O homem mais velho tem {} anos e se chama {} !'.format(idhv, nomev ))
print('Ao todo são {} mulheres abaixo de 20 anos!'.format(fm))

