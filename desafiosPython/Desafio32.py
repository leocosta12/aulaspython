a = int(input('Digíte o ano que deseja saber se é bissexto: '))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
    
