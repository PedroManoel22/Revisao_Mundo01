"""solução primeiramente pensada pro mim
from random import randint
lista = []
for i in range (1,5):
    lista.append(str(input(f'Insira o {i}° aluno: ')))
numero = randint(0,3)
print(f'O aluno escolhido foi {lista[numero]}')"
"""""
#Solução feita pelo professor:

from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')
