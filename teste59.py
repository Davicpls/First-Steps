n = int(0)
n2 = int(0)
x = int
while x != 5:
    n = int(input('Digite um número: '))
    n2 = int(input('Digite outro: '))
    soma = n + n2
    mult = (n * n2)
    print(str('Digite 1 para somar {} + {}').format(n, n2))
    print(str('Digite 2 para multiplicar {} * {}').format(n, n2))
    print(str('Digite 3 para saber o maior número entre {} e {}').format(n, n2))
    print(str('Digite 4 para digitar novos números').format(n, n2))
    print(str('Digite 5 para sair do programa'))
    x = int(input('Escolha de 1 a 5: '))
    if x == 1:
        print(str('O resultado da soma é {}').format(soma))
        x = int(5)
    elif x == 2:
        print(str('O resultado da multiplicação é {}').format(mult))
        x = int(5)
    elif x == 3:
        if n > n2:
            print(str('O maior número entre {} e {} é {}').format(n, n2, n))
        elif n2 > n:
            print(str('O maior número entre {} e {} é {}').format(n, n2, n2))
            x = int(5)
    elif x == 4:
        print('Recomeçando o programa:')
    elif x == 5:
        print('Você escolheu sair do programa')
print('Fim')

