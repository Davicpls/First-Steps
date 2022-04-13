n = int(input('Digite o primeiro termo de uma PA: '))
raz = int(input('Digite a razão de uma PA: '))
x = n + 10 * raz
for pa in range(n, x, raz):
    print(pa)
