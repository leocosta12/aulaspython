from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    AnoNascimento = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    idade = atual - AnoNascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maíores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
