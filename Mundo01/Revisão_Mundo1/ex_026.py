frase = str(input('Digite uma frase: ')).strip().lower()
a = 0
for i in range(0, len(frase)):
    if frase[i] in 'aA':
        a += 1
#..............................................................................................................................................

'''primeiro_a = frase.find('a')
print(f'A letra "a" apareceu {a} vezes nesta frase!')
print(f'A primeira letra "a" apareceu na posição {primeiro_a + 1}')
ultimo_a = frase.rfind('a')
print(f'A ultima letra "a" apareceu na posicção {ultimo_a + 1}')'''
#..............................................................................................................................................
print(f'A letra "a" apareceu {a} vezes nesta frase!')
print('A primeira letra "a" apareceu na posição {}'.format(frase.find('a') + 1 ))
print('A ultima letra "a" apareceu na posicção {}'.format(frase.rfind('a') +1 ))
