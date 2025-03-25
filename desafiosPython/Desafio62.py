print('='*20)
print(' TERMOS DE UMA PA  ')
print('='*20)
primeiro = int(input('Digíte o primeiro termo da P.A.: '))
razão = int(input('Digíte a razão da P.A.: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA') 
    mais = int(input('Quantos termos você quer mostra a mais? '))
print('Progressão finalizada com {} termos mostrados. '.format(total))
print('FIM')
