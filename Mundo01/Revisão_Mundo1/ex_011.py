largura = float(input('Insira a largura da parede a ser pintada: '))
altura = float(input('Agora insira a altura da parede a ser pintada: '))
area = largura * altura
tinta_usada = area / 2
print(f'Sua parede de {largura}X{altura} tem uma área igual a {area}m²')
print(f'Para pintar essa parede, você precisará de {tinta_usada}l de tinta.')