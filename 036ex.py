casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu sálario: '))
anos = float(input('Digite em quantos anos você deseja vai pagar: '))
prestacao = casa / (anos * 12)
prc = salario * 0.30
print(prc)
if prestacao <= prc :
    print('Emprestimo aceito!, seja feliz com a sua nova casa!')
    print('O valor da parcela é de {} e você pagará durante {} messes.'.format(prestacao, anos * 12))
else:
    print('Emprestimo negado!, parcelas acima de 30% do seu sálario!')
