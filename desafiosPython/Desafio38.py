print(str('Para saber qual dos números digitas á maior, Digite as informaões'))
PrimeiroNumero = float(input('Digite o valor do primeiro número: '))
SegundoNumero = float(input('Digite o valor do segundo número: '))
if PrimeiroNumero > SegundoNumero:
    print('O primeiro número é maior')
elif PrimeiroNumero < SegundoNumero:
    print('O segundo número é maior')
else:
    print('Não existe valor maior, os dois são iguais')