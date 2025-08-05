palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudante', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

