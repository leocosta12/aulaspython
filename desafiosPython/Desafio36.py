print('Para aprovar seu empréstimo precisaremos de algumas informações! ')
ValorCasa = float((input('Digite o valor da casa: ')))
salario = float(input('Ok, agora digite o seu salário: '))
anos = int(input('Digite em quantos anos deseja pagar a casa: '))
ValorPrestacao = (ValorCasa / anos) / 12
if ValorPrestacao <= (30 / 100) * salario:
    print('O seu empréstimo foi aprovado e o valor da prestação mensal fica em {:.2f}'.format(ValorPrestacao))
else:
    print('O valor da prestação ultrapassa 30% do valor da casa e por conta disso foi negado')