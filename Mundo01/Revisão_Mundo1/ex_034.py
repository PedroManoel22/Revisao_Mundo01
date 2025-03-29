salario = float(input('Insira o salário do funcionário? R$'))
if salario > 1250:
    salario_reajustado = salario + (salario * 0.10)
elif salario <= 1250:
    salario_reajustado = salario + (salario * 0.15)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario_reajustado:.2f} agora')