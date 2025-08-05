peso = float(input('Digite seu peso atual: '))
altura = float(input('Digite sua altura atual: '))
imc = peso / (altura **2)
print('Seu IMC {:.2f} !'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Você está com Obesidade!')
else:
    print('Você está com obesidade mórbida!')