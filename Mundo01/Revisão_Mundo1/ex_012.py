preco = float(input('Insira o preço do produto: '))
preco_final = preco - (preco * 0.05)
print(f'O produto que custava R${preco}, na promoção com desconto de 5% ficará por R${preco_final:.2f}')
