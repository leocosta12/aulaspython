n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo  número: '))
op = 0
while op != 5:
    op = int(input('Selecione a opção que deseja: \n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa.\n'))
    if op == 1:
        s = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, s))
    elif op == 2:
        m = n1*n2
        print('O resultado da multiplicação entre {} e {} é {}'.format(n1, n2, m))
    elif op == 3:
        if n1 > n2:
            print('entre {} e {},  o maior é {}'.format(n1, n2, n1))
        else:
            print('entre {} e {},  o maior é {}'.format(n1, n2, n2))
    elif op == 4:
        print('Informe os números novamente: ')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo  número: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Oppção inválida tente novamente!')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
        
