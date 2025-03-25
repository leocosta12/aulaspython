from random import randint
r = randint(0, 5)
n = int(input('Digíte um número entre 0 e 5: '))
print('O número escolhido foi {}'.format(n))
if r == n:
    print('Você acertou, parabéns! ')
else:
    print('você errou, tente novamente')
