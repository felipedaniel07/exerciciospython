frase = str(input('Digite uma frase: ')).strip().upper()
junto = ''.join(frase.split())
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um polimedro!')
else:
    print('Não temos um polimedro!')

