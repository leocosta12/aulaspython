print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem FORMAR TRIÂNGULO!', end='')
    if r1 == r2 == r3:
      print('EQUILATERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
      print('ISÓSCELES ')
    elif r1 != r2 or r1 != r3 and r2 != r3:
      print('ESCALENO ')
else:
    print('\33[7;30;41mOs segmentos acima não podem FORMAR TRIÂNGULO!')
