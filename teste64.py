n = 0
count = -1
soma = 0
while n != 999:
    n = int(input('Digite um número inteiro: '))
    count += 1
    soma += n
    s = soma - 999
    if n == 999:
        print('Foram digitados {} números e a soma deles foi {}'.format(count, s))