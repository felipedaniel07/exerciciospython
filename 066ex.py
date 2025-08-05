s = c = 0
while True:
    n1 = int(input('Digite um valor, para sair [999}: '))
    if n1 == 999:
        break
    s += n1
    c += 1
print(f'O total de números digitados foi {c} e a soma deles {s} !')

