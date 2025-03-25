n = s = qn = 0
while True:
    n = int(input('Digíte um número (999 para parar): '))
    if n == 999:
        break
    qn += 1
    s += n
print(f'Você digitou um total de {qn} números e a soma entre eles foi {s}')

