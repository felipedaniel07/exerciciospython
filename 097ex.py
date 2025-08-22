def linha(valores):
    taml = len(valores) + 4
    print('~' * taml)
    print(valores.center(taml))
    print('~' * taml)

texto = 'Aula de python'
linha(texto)
texto2 = 'Programando em Python!'
linha(texto2)
texto3 = 'Desenvolvedor Python'
linha(texto3)

