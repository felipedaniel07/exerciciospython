l = float(input('Largura da parede:'))
a = float(input('Altura da parede:'))
#s = l * a
print('Sua parede tem a dismensão igual {}x{} e sua área é de {}m2'.format(l, a, l*a))
print('Para pintar essa parede você precisará de {:.2f}l de tintas.'.format((l*a) /2))
