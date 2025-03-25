from math import radians, sin, cos, tan
angulo = float(input('informe o angulo o qual deseja saber o seno, cosseno e a tangente: '))
seno = sin(radians(angulo))
#radians converte o angulo para radianos
#sin calcula o seno do angulo
print('O angulo de {}, tem o seno de: {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
#cos calcula o cosseno do angulo
print('O angulo de {}, tem o cosseno de: {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
#tan calcula a tangente do angulo
print('O angulo de {}, tem a tangente de: {:.2f}'.format(angulo, tangente))
#tangente = seno/cosseno
#seno = cateto oposto/hipotenusa
#cosseno = cateto adjascente/hipotenusa
#poderia calular a hipotenusa com hypot(co, ca) e depois calcular a tangente com seno/hipotenusa
