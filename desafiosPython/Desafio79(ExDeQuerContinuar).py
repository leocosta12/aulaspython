numeros = []
while True:
    n = int(input('Digíte um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não adicionado ')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
numeros.sort() # deixa em ordem crescente
print(f'Você digitou os valores {numeros}')