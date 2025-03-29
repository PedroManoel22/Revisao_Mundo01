velocidade_atual = int(input('Qual é a velocidade atual do carro? '))

if velocidade_atual <= 80:
    print('Dirija com cuidado!, tenha um bom dia! ')
elif velocidade_atual > 80:
    multa = (velocidade_atual - 80) * 7
    print(f'MULTADO! Você excedeu a velocidade permitida de 80KM/H!\nPor ta dirigindo á {velocidade_atual}KM/H sua multa será de R${multa} ')