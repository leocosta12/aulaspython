from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador 
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ìmpar? [P/I] ')).strip().upper()[0]
    print(f'Voçê jogou {jogador} e o computador {computador}. total de {total}', end='')
    print(' DEU PAR' if total % 2 == 0 else ' DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voçê VENCEU!')
            v += 1
        else:
            print('Voçê PERDEU! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voçê VENCEU! ')
            v += 1
        else:
            print('Voçê PERDEU! ')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voçê venceu {v} vezes. ')
