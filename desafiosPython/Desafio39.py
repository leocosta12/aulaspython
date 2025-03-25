from datetime import date
atual = date.today().year
AnoNascimento = int(input('Digite o seu ano de nascimento: '))
idade = atual - AnoNascimento
if idade > 18:
    print('Já se passou {} anos para você se alistar, compareça a uma junta militar.'.format((idade - 18)))
elif idade == 18:
    print('Já é hora de se alistar, consulte a data e compareça a uma junta militar! ')
else:
    print('Falta {} anos para você se alistar.'.format((18 - idade)))