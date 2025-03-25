from random import choice
a1 = str(input('Digite o nome do 1° aluno: '))
a2 = str(input('Digite o nome do 2° aluno: '))
a3 = str(input('Digite o nome do 3° aluno: '))
a4 = str(input('Digite o nome do 4° aluno: '))
print('O aluno escolhido foi {}'.format(choice([a1, a2, a3, a4])))
#choice escolhe um item aleatório de uma lista (sorteia um item)
