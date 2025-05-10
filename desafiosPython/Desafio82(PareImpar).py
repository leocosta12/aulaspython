num = []
pares = []
impares = []
while True:
    num.append(int(input('Digíte um valor: ')))
    r = str(input('Quer continuar [S/N]: '))
    if r in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=-' * 30)
print(f'lista completa: {num}')
print(f'lista de números pares: {pares}')
print(f'lista de números impares: {impares}')