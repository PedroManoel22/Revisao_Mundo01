dis = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {dis}km!')
if dis <= 200:
    preco = dis * 0.50
elif dis > 200:
    preco = dis * 0.45
print(f'E o preço da sua passsagem será de R${preco:.2f}')