def nota(*num, sit=True):
    """
    -> Função para analisar várias notas de alunos e suas situações
    :param num: uma ou mais notas para alunos (Aceita várias)
    :param sit: Situação que o aluno se encontra pela sua nota média
    :return: Dicionário com várias informações da turma
    """
    soma = 0
    dados = {}
    for n in num:
        soma += n
    media = soma/len(num)
    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['média'] = media
    if sit == True:
        if media >= 7:
            dados['situacao'] = 'BOA'
        elif media >= 4 and media <7:
            dados['situacao'] = 'RAZOAVEL'
        else:
            dados['situacao'] = 'PESSIMA'
    return dados

ficha = nota(6,10,10,1)
for k, v in ficha.items():
    print(f'[{k}: {v}]', end=' ')