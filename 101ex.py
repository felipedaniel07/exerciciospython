import datetime
def voto(ano):
    global idd
    idd = datetime.date.today().year - idd
    if idd < 16:
        return  'NEGADO'
    elif idd >= 65 or idd <18:
        return  'OPCIONAL'
    else:
        return  'OBRIGATORIO'
print('-'*40)
idd = int(input('Em que ano você nasceu: '))
status = voto(idd)
print(f'Com {idd} anos o voto é: {status}.')
