lista = []
while True:
    lista.append(int(input('Digíte um valor: ')))
    r = str(input('Quer continuar?  [S/N]'))
    if r in 'Nn':
        break
print('=-' * 30)
print(f'Você digítou {len(lista)} números')
lista.sort(reverse=True) # deixa em ordem decresente
print(f'os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('o valor 5 não foi encontrado na lista! ')
