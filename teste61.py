n = int
raz = int
pa = str
x = 0
while pa != 0:
    n = int(input('Digite o primeiro termo de uma PA: '))
    raz = int(input('Digite a razão de uma PA: '))
    print('O primeiro termo da sua PA é {}'.format(n))
    print('O segundo termo da sua PA é {}'.format(n + raz))
    print('O terceiro termo da sua PA é {}'.format(n + raz * 2))
    print('O quarto termo da sua PA é {}'.format(n + raz * 3))
    print('O quinto termo da sua PA é {}'.format(n + raz * 4))
    print('O quinto termo da sua PA é {}'.format(n + raz * 5))
    print('O sexto termo da sua PA é {}'.format(n + raz * 6))
    print('O sétimo termo da sua PA é {}'.format(n + raz * 7))
    print('O oitavo termo da sua PA é {}'.format(n + raz * 8))
    print('O nono termo da sua PA é {}'.format(n + raz * 9))
    print('O décimo termo da sua PA é {}'.format(n + raz * 10))
    pa = 0
print('FIM')