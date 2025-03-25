print('='*20)
print('10 TERMOS DE UMA PA  ')
print('='*20)
t = int(input('Digíte o primeiro termo da P.A.: '))
r = int(input('Digíte a razão da P.A.: '))
dt = t + (10-1) * r
for c in range(t, dt + r, r):
    print('{} '.format(c), end='-> ')
print('ACABOU')