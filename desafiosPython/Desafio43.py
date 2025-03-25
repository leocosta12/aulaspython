altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura ** 2)
print('O seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')