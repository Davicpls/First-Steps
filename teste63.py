print('\033[1mSequência de Fibonacci\033[m')
número = int(input('Digite quantos elementos da sequência você quer: '))
n = número
último = 0
penúltimo = 1
termo = último + penúltimo
count = 0
for count in range(0, n):
    termo = último + penúltimo
    penúltimo = último
    último = termo
    count += 1
    print('{} -> '.format(termo), end='')
