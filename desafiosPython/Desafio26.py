nome = str(input('Digite uma frase: ' )).upper().strip()
print('A letra "a" aparece {} vezes na frase'.format(nome.count('A')))
print('A primeira letra "a" apareceu na posição {}'.format(nome.find('A')+1))
#O +1 é para não mostrar a posição 0
#O find() mostra a posição da primeira letra encontrada
print('A última letra "a" apareceu na posição {}'.format(nome.rfind('A')+1))
#O rfind() mostra a posição da última letra encontrada
