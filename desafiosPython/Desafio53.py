frase = str(input('Digíte a palavra para saber se ela é um palindromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]''' # solução com for e sem for
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo')