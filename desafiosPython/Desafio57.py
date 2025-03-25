n = str(input('Digíte o sexo da pessoa [M/F]: ')).lower().strip()
if n != 'f':
    if n != 'm':
        print('Você digitou um valor incorreto, digite novamente')
    else:
        print('Valor salvo')
else:
    print('Valor salvo')