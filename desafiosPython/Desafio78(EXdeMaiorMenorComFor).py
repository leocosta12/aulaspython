listanum = []
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f'Digíte um valor para a posição: {c}:  ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-' * 30)
print(f'Você digítou os valores {listanum}')
print(f'O maior valor digítado foi {maior}, nas posições ', end='')
for i, v, in enumerate(listanum):
    if listanum[i] == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digítado foi {menor} nas posições ', end='')
for i, v, in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')
print()