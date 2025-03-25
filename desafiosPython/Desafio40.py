nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
print('tirando {:.1f} e {:.1f}, á média do aluno é {:.1f}'.format(nota1,nota2,media))
if media >= 7:
    print('Aprovado')
elif media < 5:
    print('Reprovado')
else:
    print('Recuperação')