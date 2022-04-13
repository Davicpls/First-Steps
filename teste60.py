import math
n = int
n2 = int
while n != 0:
    n = int(input('Digite um número para saber seu fatorial: '))
    if math.factorial(n) != 0:
        print('O fatorial do número {} é {}'.format(n, math.factorial(n)))
        n = int(0)
print('Fim')