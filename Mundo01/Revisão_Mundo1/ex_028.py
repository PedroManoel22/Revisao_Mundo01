from time import sleep
from random import randint
print('\033[33m-=-\033[m'*40)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m'*40)
resp = int(input('Em que número eu pensei? '))
print('\033[35mProcessando...\033[m')
sleep(2)
x = randint(0,5)
if resp == x:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!\033[m')
elif resp != x:
    print('\033[31mEu genhei hehe, tente novamente!')
print(x)
