print('='*20)
print('10 TERMOS DE UMA PA  ')
print('='*20)
primeiro = int(input('Digíte o primeiro termo da P.A.: '))
razão = int(input('Digíte a razão da P.A.: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')