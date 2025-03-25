a = float(input('Digite o salário do funcionarío: '))
if a >= 1250.00:
    b = a + (10/100)*a
else:
    b = a + (15/100)*a
print('O novo salário do funcionário é : {}'.format(b))
