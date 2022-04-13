s = 0
for t in range(1, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
print('A soma dos números pares são: {}'.format(s))