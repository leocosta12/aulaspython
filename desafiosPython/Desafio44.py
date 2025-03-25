valor = float(input('Digite o valor do produto: '))
print('''Escolha uma das opções de pagamento:
[ 1 ] A vista, dinheiro ou cheque.
[ 2 ] A vista no cartão
[ 3 ] Parcelado em até 2x
[ 4 ] Parcelado em 3x ou mais''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O valor a se pagar é {}'.format(valor - (10/100 * valor)))
elif opção == 2:
    print('O valor a se pagar é {}'.format(valor - (5/100 * valor)))
elif opção == 3:
    print('O valor a se pagar é {}'.format(valor))
elif opção == 4:
    print('O valor a se pagar é {}'.format(valor + (20/100 * valor)))