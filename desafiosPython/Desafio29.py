v = float(input('Digíte a velocidade do carro: '))
if v <= 80:
   print('Você está na velocidade da via')
else:
   print('Você ultrapassou a velocidade da via, tera que pagar a multa no valor de {:.2f} reais!'.format((v - 80) * 7.0))