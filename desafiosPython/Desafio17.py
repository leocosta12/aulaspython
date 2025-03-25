import math
ca = float(input('Digite o valor do cateto adjascente: '))
co = float(input('Digite o valor do cateto oposto: '))
h = math.hypot(co, ca)
print ('O valor da hipotenusa é {:.2f}'.format(h))
#hipotenusa = sqrt(co**2 + ca**2)
#hipotenusa = hypot(co, ca)
#hypot é uma função que calcula a hipotenusa de um triângulo retângulo
