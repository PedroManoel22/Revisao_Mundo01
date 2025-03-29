import math 
oposto = float(input('comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.sqrt((oposto * oposto) + (adjacente * adjacente))
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
