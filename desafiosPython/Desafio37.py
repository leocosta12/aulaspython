num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para coversão:
[ 1 ] coverter para BÍNARIO
[ 2 ] coverter para OCTAL
[ 3 ] coverter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} covertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} covertido para OCTAL é igual a {} '.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} covertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente! ')