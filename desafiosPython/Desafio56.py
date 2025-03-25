somaidade = 0
mediaidade = 0
maioridadedehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print('---------{}ª PESSOA-------'.format(p))
    nome = str(input('nome: '.format(p))).strip()
    idade = int(input('Idade: '.format(p)))
    sexo = str (input('Sexo [F] ou [M]:'.format(p))).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadedehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        totmulher20 += 1
m = somaidade / 4
print('A média de idade das pessoas é {}'.format(m))
print('{} mulheres tem menos de 20 anos'.format(totmulher20))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadedehomem, nomevelho))