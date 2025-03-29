dias = int(input('Quantos dias o carro foi alugado? '))
kms = float(input('Quantos KM o carro pecorreu? '))
custo = dias * 60 + kms * 0.15
print(f'O preço final do aluguel foi de R${custo:.2f}')