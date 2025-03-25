from datetime import date
atual = date.today().year
AnoNascimento = int(input('Digite o seu ano de nascimento: '))
idade = atual - AnoNascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Sua caregoria é: MIRIM! ')
elif idade <= 14:
    print('Sua categoria é: INFANTIL! ')
elif idade <= 19 :
    print('Sua categoria é: JUNIOR!')
elif idade <= 25:
    print('Sua categoria é: SÊNIOR! ')
else:
    print('Sua categoria é: MASTER! ')
