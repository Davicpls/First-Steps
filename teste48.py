s = int(0)
for c in range(0, 500, 3):
    if c % 2 == 1:
        print(c)
        s += c
print('O somatório de todos os número ímpares múltiplos de 3 no intervalo de 0 a 500 é igual {}'.format(s))
