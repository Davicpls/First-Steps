import math
n = 0
c = 0
f = 1
for c in range(0, 1):
    n = int(input('Digite um número: '))
    f = math.factorial(n)
    print('O fatorial do número {} é {}'.format(n, f))
print('FIM')