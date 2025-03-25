cont = media = soma = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números, a media entre eles foi {}.'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))