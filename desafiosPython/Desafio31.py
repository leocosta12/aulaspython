n = float(input('Digite a distância que em Km da viagem: '))
if n <= 200:
    print('O valor a ser pago será {} reais'.format(n * 0.5))
else:
    print('O valor a ser pago será {} reais'.format(n*0.45))