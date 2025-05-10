lista = []
for c in range(0, 5):
    n = int(input('Digíte um valor: '))
    if c == 0 or n > lista[-1]:  #c==0 se refere ao primeiro elemento, list[-1] se refere ao ultimo 
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digítados em ordem foram {lista}')

