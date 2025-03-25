nome = str(input('Digite o seu nome:' )).strip()
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#find retorna a posição da primeira ocorrência do caractere, se não encontrar retorna -1
#rfind retorna a posição da última ocorrência do caractere, se não encontrar retorna -1
#count retorna a quantidade de vezes que o caractere foi encontrado
#len retorna o tamanho da string
#strip remove os espaços antes e depois da string
#split divide a string em uma lista
