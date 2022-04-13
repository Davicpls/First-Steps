sal = float(input('Digite o seu salário: '))
a1 = (sal * 110 / 100) - sal
a2 = (sal * 115 / 100) - sal
if sal > 1250.00:
    print('O seu aumento vai ser de R${}'.format(a1))
if sal <= 1250.00:
    print('O seu aumento será de R${}'.format(a2))

