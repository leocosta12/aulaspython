from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha uma das opções:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('Sua opção é: '))
print ('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE') 
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        pint('Jogada inválida')
    
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        pint('Jogada inválida')