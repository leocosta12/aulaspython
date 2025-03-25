cores = {'limpa':'\33[m',
         'azul':'\33[34m',
         'amarelo':'\33[33m'}
n = float(input('Digite um número: '))
print('O dobro do seu número é {}{}{}, \no tripo do seu número é {}{}{}, \na raiz quadrada do seu número é {}{:.3}{}'.format(cores['azul'], n*2, cores['limpa'], cores['amarelo'], n*3, cores['limpa'], cores['azul'], pow(n, (1/2))))
