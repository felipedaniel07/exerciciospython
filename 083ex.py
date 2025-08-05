lista = []
exp = str(input('Digite a expresão: '))
for l in exp:
    if l == '(':
        lista.append('(')
    elif l == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão Valida!')
else:
    print('Expressão Invalida!')




