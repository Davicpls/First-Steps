print('\033[1mTabuada de qualquer número (valor negativo interrompe): -->')
n = 0
count = 0
while True:
    n = int(input('\nQuer ver a tabuada de qual valor?: '))
    if n < 0:
        break
    for t in range(1, 11):
        print(f'{n} x {t} = {n * t}')
print('\nO valor que você digitou foi negativo e o programa parou')
